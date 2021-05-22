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

from . import hod_views, staff_views, student_views, views

urlpatterns = [
    path("", views.login_page, name='login_page'),
    path("get_attendance", views.get_attendance, name='get_attendance'),
    path("firebase-messaging-sw.js", views.showFirebaseJS, name='showFirebaseJS'),
    path("doLogin/", views.doLogin, name='user_login'),
    path("logout_user/", views.logout_user, name='user_logout'),
    path("home/admin/", hod_views.admin_home, name='admin_home'),
    path("add/teacher", hod_views.add_staff, name='add_staff'),
    path("add/course", hod_views.add_course, name='add_course'),
    path("send_student_notification/", hod_views.send_student_notification,name='send_student_notification'),
    path("send_staff_notification/", hod_views.send_staff_notification,name='send_staff_notification'),
    path("add_session/", hod_views.add_session, name='add_session'),
    path("admin_notify_student", hod_views.admin_notify_student,name='admin_notify_student'),
    path("admin_notify_teacher", hod_views.admin_notify_staff,name='admin_notify_staff'),
    path("admin_view_profile", hod_views.admin_view_profile,name='admin_view_profile'),
    path("check_email_availability", hod_views.check_email_availability,name="check_email_availability"),
    path("manage/session/", hod_views.manage_session, name='manage_session'),
    path("edit/session/<int:session_id>",hod_views.edit_session, name='edit_session'),
    path("student/view/feedback/", hod_views.student_feedback_message,name="student_feedback_message",),
    path("teacher/view/feedback/", hod_views.staff_feedback_message,name="staff_feedback_message",),
    path("student/view/leave/", hod_views.view_student_leave,name="view_student_leave",),
    path("teacher/view/leave/", hod_views.view_staff_leave, name="view_staff_leave",),
    path("attendance/view/", hod_views.admin_view_attendance,name="admin_view_attendance",),
    path("attendance/fetch/", hod_views.get_admin_attendance,name='get_admin_attendance'),
    path("student/add/", hod_views.add_student, name='add_student'),
    path("subject/add/", hod_views.add_subject, name='add_subject'),
    path("manage/teacher/", hod_views.manage_staff, name='manage_staff'),
    path("manage/student/", hod_views.manage_student, name='manage_student'),
    path("manage/course/", hod_views.manage_course, name='manage_course'),
    path("manage/subject/", hod_views.manage_subject, name='manage_subject'),
    path("edit/teacher/<int:staff_id>", hod_views.edit_staff, name='edit_staff'),
    path("edit/student/<int:student_id>",hod_views.edit_student, name='edit_student'),
    path("edit/course/<int:course_id>",hod_views.edit_course, name='edit_course'),
    path("edit/subject/<int:subject_id>",hod_views.edit_subject, name='edit_subject'),
    
    
    # Staff
    path("home/teacher/", staff_views.staff_home, name='staff_home'),
    path("teacher/apply/leave/", staff_views.staff_apply_leave,name='staff_apply_leave'),
    path("teacher/feedback/", staff_views.staff_feedback, name='staff_feedback'),
    path("teacher/view/profile/", staff_views.staff_view_profile,name='staff_view_profile'),
    path("teacher/attendance/take/", staff_views.staff_take_attendance,name='staff_take_attendance'),
    path("teacher/attendance/update/", staff_views.staff_update_attendance,name='staff_update_attendance'),
    path("teacher/get_students/", staff_views.get_students, name='get_students'),
    path("teacher/attendance/fetch/", staff_views.get_student_attendance,name='get_student_attendance'),
    path("teacher/attendance/save/", staff_views.save_attendance, name='save_attendance'),
    path("teacher/attendance/update/", staff_views.update_attendance,name='update_attendance'),
    path("teacher/fcmtoken/", staff_views.staff_fcmtoken, name='staff_fcmtoken'),
    path("teacher/view/notification/", staff_views.staff_view_notification,name="staff_view_notification"),
    path("teacher/result/add/", staff_views.staff_add_result, name='staff_add_result'),
    path("teacher/result/edit/", EditResultView.as_view(),name='edit_student_result'),
    path('teacher/result/fetch/', staff_views.fetch_student_result,name='fetch_student_result'),



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
