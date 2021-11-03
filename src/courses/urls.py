from django.urls import path
from .views import CourseListView, CourseDetailView

urlpatterns = [
   path('', CourseListView.as_view(), name='list'),
   path('', CourseDetailView.as_view(), name='detail'),
]
