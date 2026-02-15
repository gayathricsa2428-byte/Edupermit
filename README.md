College Leave & Permission Management System
 Project Overview

A web-based system that helps students apply for leave and permission requests efficiently.
It automatically checks eligibility based on attendance, suggests required documents, shows the approval workflow, and generates official permission letters as PDF files.

 Team

Team Name: Team Fortune

Gayathri R — Saintgits College Of Engineering

Elizabeth Joe — Saintgits College Of Engineering

 Hosted Repository

 https://github.com/gayathricsa2428-byte/Edupermit

 Problem Statement

Students often face confusion and delays while applying for leave due to manual verification, unclear approval hierarchy, and lack of status tracking.

 Solution

This system digitizes the process by:

  * Checking attendance eligibility automatically

 * Suggesting necessary documents

 * Showing approval flow (Advisor → HOD → Principal)

 * Generating official permission letters in PDF

 * Providing a clear and fast workflow for students

Features

* Student Registration & Login

* Attendance-Based Eligibility Check

* Multiple Leave Types:

* General Leave

* Medical Leave

* On-Duty Leave

* Event Permission

* Dynamic Document Suggestions

* Approval Hierarchy Visualization

* Downloadable PDF Permission Letters

* Fully Responsive UI

 Technologies Used
* Backend

Flask

SQLite

ReportLab

* Frontend

HTML / CSS / JavaScript


Tools

Visual Studio Code

Git & GitHub

⚙️ Local Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/gayathricsa2428-byte/Edupermit.git
cd Edupermit

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

 Install Dependencies
pip install flask reportlab

 Run Application
python app.py

 Open in Browser
http://127.0.0.1:5000/

 Usage

Register/Login as student

Enter attendance & leave details

System checks eligibility

Shows required documents & approval flow

Generate/download official permission letter

 Future Enhancements

Admin Dashboard for approvals

Email Notifications

Attendance System Integration

Analytics for faculty

Mobile App Version

License
MIT License 

MIT License
