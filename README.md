# Student Management System Created Using Django
###This is a Final Year Project:

##Project Name:Student Management System in Django

##Project Supervisor: Huo Mao

##Project done by: 
###Name: Erman Hossain Rashed


###Student Id: 2017521460044

###Batch 2017, Software Engineering

###Sichuan University,Chengdu,Sichuan,China





###Module Functionalities

### 

### A. Admin

1. See Overall Summary Charts of Students Performances, teacher Performances, Courses, Subjects, Leave, etc.
2. Manage teacher (Add, Update and Delete)
3. Manage Students (Add, Update and Delete)
4. Manage Course (Add, Update and Delete)
5. Manage Subjects (Add, Update and Delete)
6. Manage Sessions (Add, Update and Delete)
7. View Student Attendance
8. Review and Reply Student/teacher Feedback
9. Review (Approve/Reject) Student/teacher Leave

### B. teacher/Teachers

1. See the Overall Summary Charts related to their students, their subjects, leave status, etc.
2. Take/Update Students Attendance
3. Add/Update Result
4. Apply for Leave
5. Send Feedback to HOD

### C. Students 

1. See the Overall Summary Charts related to their attendance, their subjects, leave status, etc.
2. View Attendance
3. View Result
4. Apply for Leave
5. Send Feedback to HOD




## How to Install and Run this project?

### Pre-Requisites:

1. Install Python Latest Version


2. Install Pip (Package Manager)



### Installation
**1. Create a Folder to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
pip install virtualenv
```

Create Virtual Environment

For Windows
```
python -m venv env
```
For Mac
```
python3 -m venv env
```
For Linux
```
virtualenv .
```

Activate Virtual Environment

For Windows
```
source env/scripts/activate
```

For Mac
```
source env/bin/activate
```

For Linux
```
source bin/activate
```


**3. Install Requirements from 'requirements.txt'**
```python
pip install -r requirements.txt
```

**5. Add the hosts**

- Got to settings.py file 
- Then, On allowed hosts, Use **[]** as  host. 
```python
ALLOWED_HOSTS = []
```



**6. Now Run Server**

Command for Windows:
```python
python manage.py runserver
```

Command for Mac:
```python
python manage.py runserver
```

Command for Linux:
```python
python manage.py runserver
```

**7. Login Credentials**

Create Super User (HOD)
Command for Windows:
```
python manage.py createsuperuser
```

Command for Mac:
```
python manage.py createsuperuser
```

Command for Linux:
```
python manage.py createsuperuser
```






## Project's Utility

- [x] Admin/Teacher/Student Login
- [x] CURD (Create, Update, Read, Delete) operations in Course
- [x] CURD (Create, Update, Read, Delete) operations in teacher
- [x] CURD (Create, Update, Read, Delete) operations in Student
- [x] CURD (Create, Update, Read, Delete) operations in Subject
- [x] Upload admin, student, teacher's Picture
- [x] Sidebar Active Status
- [x] Password Reset Via Email
- [x] Apply For Leave both for Teachers and Students
- [x] Students Can Check Attendance
- [x] Check Email Availability
- [x] Reply to Leave Applications
- [x] Reply to Feedback
- [x] Admin View Attendance
- [x] Admin Profile Edit
- [x] teacher Profile Edit
- [x] Student Profile Edit
- [x] Student Dashboard
- [x] Teacher Dashboard
- [x] Admin Dashboard
- [x] Teacher Add Student's Result
- [x] Teacher Edit Result 
- [x] Google CAPTCHA
- [x] Student View Result


