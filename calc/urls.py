from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('add_course',views.AddCourse,name='add_course'),
    path('add_teachers',views.AddTeachers,name='add_teachers'),
    path('class_room',views.AddClassroom,name='class_room'),
    path('fetchdata',views.fetchData,name='fetchdata'),
    path('createtimetable',views.createtimetable, name='createtimetable'),   
      
]

#path('createtimetable',views.createtimetable,name='createtimetable'),
