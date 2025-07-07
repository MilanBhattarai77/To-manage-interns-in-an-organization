from rest_framework import serializers # type: ignore
from .models import UserProfile, Task, Attendance



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields='__all__'



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'




class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'



    