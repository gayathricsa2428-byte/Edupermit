from flask import Flask, render_template, request, redirect, url_for, session, send_file
import sqlite3
import uuid
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# ---------------- Global Variables ----------------
DATABASE = "database.db"
COLLEGE_NAME = "ABC College of Engineering"
COLLEGE_ADDRESS = "Kottayam, Kerala"

# ---------------- Database Setup ----------------
def init_db():
    """Initialize the database and create students table if not exists"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            reg_no TEXT,
            phone TEXT,
            department TEXT,
            roll_no TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------------- Routes ----------------
@app.route("/")
def welcome():
    """Landing page / welcome page"""
    return render_template("welcome.html")  # Only one welcome page

@app.route("/login")
def login():
    """Login / Registration page"""
    return render_template("login.html")

@app.route("/register", methods=["POST"])
def register():
    """Handle student registration and redirect to dashboard"""
    name = request.form["name"]
    reg_no = request.form["reg_no"]
    phone = request.form["phone"]
    department = request.form["department"]
    roll_no = request.form["roll_no"]

    # Insert student details into DB
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, reg_no, phone, department, roll_no) VALUES (?, ?, ?, ?, ?)",
        (name, reg_no, phone, department, roll_no)
    )
    conn.commit()
    conn.close()

    # Save student info in session
    session["student"] = name
    session["department"] = department
    session["roll"] = roll_no

    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    """Show dashboard if student is logged in"""
    if "student" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

@app.route("/check", methods=["POST"])
def check():
    """Process leave / permission requests"""
    attendance = int(request.form["attendance"])
    req_type = request.form["type"]
    days = int(request.form["days"])
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]

    event_name = request.form.get("event_name", "")
    event_details = request.form.get("event_details", "")

    status = "Approved"
    message = "Eligible for Permission"
    documents = []
    hierarchy = ["Advisor"]
    suggested_days = 0

    # Attendance check
    if attendance < 75 and req_type != "medical":
        status = "Rejected"
        message = "Attendance below 75%"
        suggested_days = max(0, int(attendance * 0.05))
        return render_template("result.html",
                               status=status,
                               message=message,
                               documents=[],
                               hierarchy=[],
                               vid="N/A",
                               suggested_days=suggested_days)

    # Determine document & hierarchy rules
    if req_type == "medical":
        documents.append("Medical Certificate")
        hierarchy = ["Advisor", "HOD", "Principal"]
        suggested_days = days
    elif req_type == "leave":
        if days <= 2:
            hierarchy = ["Advisor"]
            suggested_days = 2
        elif 3 <= days <= 5:
            hierarchy = ["Advisor", "HOD"]
            suggested_days = 5
        else:
            status = "Rejected"
            message = "Leave more than 5 days not allowed"
            suggested_days = 5
    elif req_type in ["od", "event"]:
        hierarchy = ["Advisor", "HOD", "Principal"]
        documents.append("Event Proof" if req_type == "od" else "Event Participation Proof")
        suggested_days = days

    verification_id = str(uuid.uuid4())[:8]

    # Save data for PDF generation
    session["pdf_data"] = {
        "name": session["student"],
        "department": session["department"],
        "roll": session["roll"],
        "type": req_type,
        "days": days,
        "start": start_date,
        "end": end_date,
        "attendance": attendance,
        "status": status,
        "authority": hierarchy[-1] if hierarchy else "Advisor",
        "event_name": event_name,
        "event_details": event_details
    }

    return render_template("result.html",
                           status=status,
                           message=message,
                           documents=documents,
                           hierarchy=hierarchy,
                           vid=verification_id,
                           suggested_days=suggested_days)

# ---------------- PDF Generation ----------------
@app.route("/generate_pdf")
def generate_pdf():
    """Generate leave / permission PDF"""
    if "pdf_data" not in session:
        return redirect(url_for("dashboard"))

    data = session["pdf_data"]
    file_path = "permission_letter.pdf"

    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=60,
        leftMargin=60,
        topMargin=70,
        bottomMargin=50
    )

    elements = []

    # Styles
    normal_style = ParagraphStyle(name="NormalStyle", fontName="Times-Roman", fontSize=12, leading=18)
    bold_style = ParagraphStyle(name="BoldStyle", fontName="Times-Bold", fontSize=14, leading=20)
    center_bold = ParagraphStyle(name="CenterBold", fontName="Times-Bold", fontSize=16, alignment=1, leading=22)
    today = datetime.today().strftime("%d %B %Y")

    # Header
    elements.append(Paragraph(COLLEGE_NAME, center_bold))
    elements.append(Paragraph(COLLEGE_ADDRESS, normal_style))
    elements.append(Spacer(1, 0.3 * inch))
    elements.append(Paragraph(f"<para alignment='right'>{today}</para>", normal_style))
    elements.append(Spacer(1, 0.2 * inch))

    # From Section
    elements.append(Paragraph("From,", normal_style))
    elements.append(Paragraph(data['name'], normal_style))
    elements.append(Paragraph(f"Roll No: {data['roll']}", normal_style))
    elements.append(Paragraph(f"Department of {data['department']}", normal_style))
    elements.append(Spacer(1, 0.3 * inch))

    # To Section
    elements.append(Paragraph("To,", normal_style))
    elements.append(Paragraph(f"The {data['authority']},", normal_style))
    elements.append(Paragraph(COLLEGE_NAME + ",", normal_style))
    elements.append(Paragraph(COLLEGE_ADDRESS + ".", normal_style))
    elements.append(Spacer(1, 0.3 * inch))

    # Subject
    elements.append(Paragraph(f"<b>Subject: Request for {data['type'].capitalize()} Leave</b>", normal_style))
    elements.append(Spacer(1, 0.3 * inch))

    # Body
    body_text = f"I respectfully submit that I am a student of the Department of {data['department']}.\n"
    body_text += f"I request permission to avail {data['type']} leave for {data['days']} day(s) from {data['start']} to {data['end']}.\n"
    body_text += f"My current attendance percentage is {data['attendance']}%.\n"
    if data['type'] == "event" and data.get("event_name"):
        body_text += f"I am participating in the event: {data['event_name']}.\n"
        if data.get("event_details"):
            body_text += f"Event Details: {data['event_details']}\n"
    body_text += "I assure you that I shall complete all academic responsibilities upon my return.\n"
    body_text += "I kindly request you to grant me permission for the above-mentioned period."
    elements.append(Paragraph(body_text, normal_style))
    elements.append(Spacer(1, 0.4 * inch))

    # Closing
    elements.append(Paragraph("Thanking you.", normal_style))
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph("Yours faithfully,", normal_style))
    elements.append(Spacer(1, 0.3 * inch))
    elements.append(Paragraph(data['name'], normal_style))
    elements.append(Paragraph(f"Roll No: {data['roll']}", normal_style))
    elements.append(Spacer(1, 0.4 * inch))

    # Office Use
    official_signatures = KeepTogether([
        Paragraph("<b>FOR OFFICE USE ONLY</b>", bold_style),
        Spacer(1, 0.2 * inch),
        Paragraph("Advisor Signature: ___________________________", normal_style),
        Spacer(1, 0.2 * inch),
        Paragraph("HOD Signature: ___________________________", normal_style),
        Spacer(1, 0.2 * inch),
        Paragraph("Principal Signature: ___________________________", normal_style)
    ])
    elements.append(official_signatures)

    doc.build(elements)
    return send_file(file_path, as_attachment=True)

# ---------------- Main ----------------
if __name__ == "__main__":
    app.run(debug=True)
