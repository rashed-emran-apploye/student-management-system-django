"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from main_app.EditResultView import EditResultView

from . import admin_views, teacher_views, student_views, views

urlpatterns = [
    path("", views.login_page, name='login_page'),
    path("get_attendance", views.get_attendance, name='get_attendance'),
    path("doLogin/", views.doLogin, name='user_login'),
    path("logout_user/", views.logout_user, name='user_logout'),
    path("home/admin/", admin_views.admin_home, name='admin_home'),
    path("add/teacher", admin_views.add_staff, name='add_staff'),
    path("add/course", admin_views.add_course, name='add_course'),
    path("send_student_notification/", admin_views.send_student_notification, name='send_student_notification'),
    path("send_staff_notification/", admin_views.send_staff_notification, name='send_staff_notification'),
    path("add_session/", admin_views.add_session, name='add_session'),
    path("admin_notify_student", admin_views.admin_notify_student, name='admin_notify_student'),
    path("admin_notify_teacher", admin_views.admin_notify_staff, name='admin_notify_staff'),
    path("admin_view_profile", admin_views.admin_view_profile, name='admin_view_profile'),
    path("check_email_availability", admin_views.check_email_availability, name="check_email_availability"),
    path("manage/session/", admin_views.manage_session, name='manage_session'),
    path("edit/session/<int:session_id>", admin_views.edit_session, name='edit_session'),
    path("student/view/feedback/", admin_views.student_feedback_message, name="student_feedback_message", ),
    path("teacher/view/feedback/", admin_views.staff_feedback_message, name="staff_feedback_message", ),
    path("student/view/leave/", admin_views.view_student_leave, name="view_student_leave", ),
    path("teacher/view/leave/", admin_views.view_staff_leave, name="view_staff_leave", ),
    path("attendance/view/", admin_views.admin_view_attendance, name="admin_view_attendance", ),
    path("attendance/fetch/", admin_views.get_admin_attendance, name='get_admin_attendance'),
    path("student/add/", admin_views.add_student, name='add_student'),
    path("subject/add/", admin_views.add_subject, name='add_subject'),
    path("manage/teacher/", admin_views.manage_staff, name='manage_staff'),
    path("manage/student/", admin_views.manage_student, name='manage_student'),
    path("manage/course/", admin_views.manage_course, name='manage_course'),
    path("manage/subject/", admin_views.manage_subject, name='manage_subject'),
    path("edit/teacher/<int:staff_id>", admin_views.edit_staff, name='edit_staff'),
    path("edit/student/<int:student_id>", admin_views.edit_student, name='edit_student'),
    path("edit/course/<int:course_id>", admin_views.edit_course, name='edit_course'),
    path("edit/subject/<int:subject_id>", admin_views.edit_subject, name='edit_subject'),
    
    
    # Staff
    path("home/teacher/", teacher_views.staff_home, name='staff_home'),
    path("teacher/apply/leave/", teacher_views.staff_apply_leave, name='staff_apply_leave'),
    path("teacher/feedback/", teacher_views.staff_feedback, name='staff_feedback'),
    path("teacher/view/profile/", teacher_views.staff_view_profile, name='staff_view_profile'),
    path("teacher/attendance/take/", teacher_views.staff_take_attendance, name='staff_take_attendance'),
    path("teacher/attendance/update/", teacher_views.staff_update_attendance, name='staff_update_attendance'),
    path("teacher/get_students/", teacher_views.get_students, name='get_students'),
    path("teacher/attendance/fetch/", teacher_views.get_student_attendance, name='get_student_attendance'),
    path("teacher/attendance/save/", teacher_views.save_attendance, name='save_attendance'),
    path("teacher/attendance/update/", teacher_views.update_attendance, name='update_attendance'),
    path("teacher/fcmtoken/", teacher_views.staff_fcmtoken, name='staff_fcmtoken'),
    path("teacher/view/notification/", teacher_views.staff_view_notification, name="staff_view_notification"),
    path("teacher/result/add/", teacher_views.staff_add_result, name='staff_add_result'),
    path("teacher/result/edit/", EditResultView.as_view(),name='edit_student_result'),
    path('teacher/result/fetch/', teacher_views.fetch_student_result, name='fetch_student_result'),



    # Student
    path("home/student/", student_views.student_home, name='student_home'),
    path("student/view/attendance/", student_views.student_view_attendance,name='student_view_attendance'),
    path("student/apply/leave/", student_views.student_apply_leave,name='student_apply_leave'),
    path("student/feedback/", student_views.student_feedback,name='student_feedback'),
    path("student/view/profile/", student_views.student_view_profile,name='student_view_profile'),
    path("student/fcmtoken/", student_views.student_fcmtoken,name='student_fcmtoken'),
    path("student/view/notification/", student_views.student_view_notification,name="student_view_notification"),
    path('student/view/result/', student_views.student_view_result,name='student_view_result'),

]
