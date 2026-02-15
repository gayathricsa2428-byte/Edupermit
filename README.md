COLLEGE LEAVE & PERMISSION MANAGEMENT SYSTEM
PROJECT OVERVIEW

A web-based system that helps students apply for leave and permission requests efficiently. It automatically checks eligibility based on attendance, suggests required documents, shows the approval workflow, and generates official permission letters as PDF files.

TEAM

Team Name: Team Fortune

Gayathri R — Saintgits College Of Engineering

Elizabeth Joe — Saintgits College Of Engineering

HOSTED REPOSITORY

https://github.com/gayathricsa2428-byte/Edupermit

PROBLEM STATEMENT

Students often face confusion and delays while applying for leave due to manual verification, unclear approval hierarchy, and lack of status tracking.

SOLUTION

This system digitizes the process by:

Checking attendance eligibility automatically

Suggesting necessary documents

Showing approval flow (Advisor → HOD → Principal)

Generating official permission letters in PDF

Providing a clear and fast workflow for students

FEATURES

Student Registration & Login

Attendance-Based Eligibility Check

Multiple Leave Types:

General Leave

Medical Leave

On-Duty Leave

Event Permission

Dynamic Document Suggestions

Approval Hierarchy Visualization

Downloadable PDF Permission Letters

Fully Responsive User Interface

TECHNOLOGIES USED
Backend

Flask

SQLite

ReportLab

Frontend

HTML / CSS / JavaScript

Font Awesome Icons

Tools

Visual Studio Code

Git & GitHub

LOCAL INSTALLATION & SETUP
1. Clone Repository
git clone https://github.com/gayathricsa2428-byte/Edupermit.git
cd Edupermit

2. Create Virtual Environment (Recommended)
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3. Install Dependencies
pip install flask reportlab

4. Run Application
python app.py

5. Open in Browser
http://127.0.0.1:5000/

USAGE

Register/Login as a student.

Enter attendance and leave details.

System checks eligibility automatically.

View required documents and approval flow.

Generate and download the official permission letter.

DEPLOYMENT (FOR LIVE HOSTING)

The project can be deployed using Render for hosting Flask applications.

Deployment Steps

Push the latest code to GitHub.

Create a requirements.txt file:

flask
reportlab
gunicorn


Ensure app.py contains:

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


Create a new Web Service in Render and connect the GitHub repository.

Use the following settings:

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

Deploy to get a public project link.

FUTURE ENHANCEMENTS

Admin Dashboard for approvals and rejections

Email notifications for students

Integration with college attendance systems

Analytics for faculty monitoring

Mobile-friendly enhancements or dedicated app

LICENSE

This project is licensed under the MIT License.
