from django.urls import path, include
from .views import *
from django.contrib import admin


urlpatterns = [
    path('details/', DetailView.as_view()),
    path('attendance/', AttendanceView.as_view()),
    path('marks/', MarksView.as_view()),
    path('timetable/', TimetableView.as_view()),
]
