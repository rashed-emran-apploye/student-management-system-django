# Student Management System Created Using Django
This is a Simple Student Management System Developed While Learning Django.
Feel free to make changes based on your requirements.

[Front-end Template](http://adminlte.io "Admin LTE.io")




## Features of this Project

### What can User's Do ?

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
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```
For Linux
```
$  virtualenv .
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```

For Mac
```
$  source venv/bin/activate
```

For Linux
```
$  source bin/activate
```


**3. Install Requirements from 'requirements.txt'**
```python
$  pip3 install -r requirements.txt
```

**5. Add the hosts**

- Got to settings.py file 
- Then, On allowed hosts, Use **[]** as  host. 
```python
ALLOWED_HOSTS = []
```



**6. Now Run Server**

Command for PC:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver
```

Command for Linux:
```python
$ python3 manage.py runserver
```

**7. Login Credentials**

Create Super User (HOD)
Command for PC:
```
$  python manage.py createsuperuser
```

Command for Mac:
```
$  python3 manage.py createsuperuser
```

Command for Linux:
```
$  python3 manage.py createsuperuser
```






## Project's Utility

- [x] Admin/teacher/Student Login
- [x] Add and Edit Course
- [x] Add and Edit teacher
- [x] Add and Edit Student
- [x] Add and Edit Subject
- [x] Upload teacher's Picture
- [x] Upload Student's Picture
- [x] Sidebar Active Status
- [x] Model Forms for all
- [x] Attendance and Update Attendance
- [x] Password Reset Via Email
- [x] Apply For Leave
- [x] Students Can Check Attendance
- [x] Check Email Availability
- [x] Reply to Leave Applications
- [x] Reply to Feedback
- [x] Admin View Attendance
- [x] Admin Profile Edit
- [x] teacher Profile Edit
- [x] Student Profile Edit
- [x] Student Dashboard
- [x] Passing Page Title From View
- [x] teacher Dashboard
- [x] Admin Dashboard
- [x] teacher Add Student's Result
- [x] teacher Edit Result 
- [x] Google CAPTCHA
- [x] Student View Result


