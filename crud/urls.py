from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    #add data
    path ('add-student/',postStudent),
    path ('add-teacher/',postTeacher),

    #fetch data
    path ('get-student/',getStudent),
    path ('get-teacher/',getTeacher),

    #edit data
    path('edit-student/<id>',editStudentData),
    path('edit-teacher/<id>',editTeacherData),

#delete items
    path('delete-student/<id>',deleteStudentData),
    path('delete-teacher/<id>',deleteTeacherData),

    #update
    #  path('update-teacher/<id>',updateStudentData),

]