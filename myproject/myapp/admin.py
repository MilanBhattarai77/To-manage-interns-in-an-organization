from django.contrib import admin
from .models import Attendance
from .models import UserProfile
from .models import Task

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Task)
admin.site.register(Attendance)

