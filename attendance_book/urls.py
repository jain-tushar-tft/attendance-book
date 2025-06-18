from django.urls import include, path

urlpatterns = [
    path("student", include("student.urls")),
]
