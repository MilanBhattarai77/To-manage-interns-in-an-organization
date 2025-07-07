from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Types(models.TextChoices):
    SUPERVISIOR = "Admin", "Admin"
    INTERN = "Employee", "Employee"

class UserProfile(AbstractUser):
    # NEW FOR THE ROLES
    role = models.CharField(
        max_length=20, choices=Types.choices, default=Types.SUPERVISIOR
    )
    email = models.EmailField(unique=True, max_length=50)
    username = models.CharField(unique=True, max_length=20)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.email
    

    
class Task(models.Model):
   title = models.CharField(max_length=250)
   description=models.CharField(max_length=250)
   created_at =models.DateField(auto_now=True)
   due_date =models.DateField(blank=True, null=True)
   is_completed = models.BooleanField(default=False)
   user=models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name="user_profile_task")

   def __str__(self):
       return self.title
   

class Attendance(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="student_user_profile")
    status = models.CharField(max_length=10, choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Late')])
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.student

    




    