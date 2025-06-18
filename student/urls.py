from django.urls import path

from student.views import StudentListCreateView, StudentRetrieveDestroyView

urlpatterns = [
    path("<str:roll_no>/", StudentRetrieveDestroyView.as_view(), name="student-retrieve"),
    path("", StudentListCreateView.as_view(), name="student-list-create"),
]
