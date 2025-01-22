from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone

from datetime import time

class Event(models.Model): 
    name = models.CharField(max_length=100) 
    date = models.DateField() 
    time = models.TimeField(default=time(0, 0))  
    location = models.CharField(max_length=200, default="Default Location") 
    description = models.TextField() 
    def __str__(self): 
        return self.name

class TrackerEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)  # User who logs the tracker entry
    date = models.DateTimeField(default=timezone.now)  # Date of the workout
    workout_type = models.CharField(max_length=100)  # Type of workout
    duration = models.PositiveIntegerField(help_text="Duration in minutes")  # Store duration in minutes  # Duration of the workout
    notes = models.TextField(blank=True, null=True)  # Optional notes for the workout

    def __str__(self):
        return f"{self.workout_type} ({self.date.strftime('%Y-%m-%d')}) by {self.user.username}"

class Exercise(models.Model): 
        tracker_entry = models.ForeignKey(TrackerEntry, on_delete=models.CASCADE, related_name='exercises') 
        exercise_name = models.CharField(max_length=100) 
        sets_reps = models.CharField(max_length=100) 
        weight = models.FloatField() 
        def __str__(self): return self.exercise_name 
class MoodLog(models.Model): 
            date = models.DateTimeField(default=timezone.now) 
            mood = models.CharField(max_length=50) 
            energy_level = models.CharField(max_length=50) 
            tracker_entry = models.ForeignKey(TrackerEntry, on_delete=models.CASCADE, related_name='mood_logs') 
            def __str__(self): 
                return f"Mood: {self.mood}, Energy Level: {self.energy_level}"
    
class ContactUs(models.Model): 
    name = models.CharField(max_length=100) 
    email = models.EmailField() 
    phone_number = models.CharField(max_length=15, blank=True, null=True) 
    preferred_workout_time = models.CharField(max_length=50, blank=True, null=True) 
    message = models.TextField() 
    def __str__(self): 
        return f"Message from {self.name} ({self.email})"

class GymClass(models.Model): 
    name = models.CharField(max_length=100) 
    description = models.TextField() 
    def __str__(self): 
        return self.name

class Attendance(models.Model): 
    class_name = models.ForeignKey(GymClass, on_delete=models.CASCADE) 
    member = models.ForeignKey(User, on_delete=models.CASCADE) 
    attendance_date = models.DateField() 
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')]) 
    def __str__(self): 
        return f"{self.member.username} - {self.class_name.name} on {self.attendance_date}"
    
class PersonalDetail(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    bio = models.TextField()

    def __str__(self):
        return self.name

