#  College Leave & Permission Management System 

## Project Overview
A web application that allows students to manage leave and permission requests efficiently. The system checks eligibility based on attendance, suggests required documents, displays the approval hierarchy, and generates official permission letters as PDFs.

## Team
- **Team Name:** Team Fortune  
- **Member 1:** Gayathri R - Saintgits College Of Engineering
- **Member 2:** Elizabeth Joe - Saintgits College Of Engineering
- 
## Hosted Project Link
https://github.com/gayathricsa2428-byte/Edupermit

## Problem Statement
Students often face delays or confusion in applying for leave or permissions. Manual processes make it difficult to track attendance and approval status.

## Solution
This web application automates leave management by:
- Checking attendance eligibility.
- Suggesting necessary documents.
- Displaying the approval hierarchy (Advisor → HOD → Principal).
- Generating official permission letters in PDF format.

## Features
- Student Registration & Login
- Attendance-based eligibility check
- Multiple leave types: General, Medical, On-Duty, Event
- Dynamic document suggestions
- Approval hierarchy visualization
- Downloadable PDF permission letters
- Responsive design for all devices

## Technical Details

### Technologies / Components Used

**Backend:**
- Python (Flask)  
- SQLite (Database)  
- ReportLab (PDF Generation)  

**Frontend:**
- HTML / CSS  
- JavaScript  
- Font Awesome Icons  

**Tools:**
- VS Code  
- Git  
- Python environment  

## Installation & Setup

1. **Clone the repository**
```bash
git clone [repo-link]
cd [repo-folder]

##2. **Install dependencies**
pip install flask reportlab

##3.**Run the application**
pip install flask reportlab

##4.**Oen the browser and go to:
 http://127.0.0.1:5000/

##Usage
Visit the welcome page and navigate to login/registration.

Register as a student with your details.

Check leave eligibility by filling in attendance, leave type, dates, and other details.

View application status, required documents, and approval hierarchy.

Download the official permission letter as a PDF if approved.

##Future Enhancements

Admin panel for approving/rejecting requests.

Email notifications for students on approval.

Integration with college attendance system.

Mobile-friendly interface improvements.

##License

This project is licensed under the MIT License - see the LICENSE file for details.
