from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("polls/", include("polls.urls")),   # localhost:8000/polls/
    path('admin/', admin.site.urls),        # localhost:8000/admin/
    path('student/', include("student.urls")),
    path('school/', include("school.urls")),
]
