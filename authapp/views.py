from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Event, TrackerEntry,ContactUs
from .models import TrackerEntry, Exercise, MoodLog,PersonalDetail
#from .models import Attendance, GymClass
from django.db import IntegrityError
from django.http import HttpResponse
# Home view
def home(request):
    return render(request, 'home.html')

# Signup view


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        # Create the user
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login_view')  # Redirect to login after successful signup

    return render(request, 'signup.html')
# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

# Logout view

def logout_view(request):
    """Logs out the user and redirects to the home page."""
    logout(request)
    return redirect('/')

# Membership view
def membership(request):
    return render(request, 'membership.html')

# Workout view
def workout(request):
    return render(request, 'workouts.html')

# Workout detail views
def full_body_workout(request):
    return render(request, 'full_body_workout.html')

def cardio_blast(request):
    return render(request, 'cardio_blast.html')

def strength_training(request):
    return render(request, 'strength_training.html')

def yoga_flex(request):
    return render(request, 'yoga_flex.html')

# Tracker view
def tracker(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        workout_type = request.POST.get('workout_type')
        duration = request.POST.get('duration')
        notes = request.POST.get('notes')

        # Validate the required fields
        if date and workout_type and duration:
            tracker_entry = TrackerEntry(
                user=request.user,
                date=date,
                workout_type=workout_type,
                duration=duration,
                notes=notes
            )
            tracker_entry.save()
            return redirect('tracker')
        else:
            return render(request, 'tracker.html', {
                'error': 'Please fill out all required fields.',
                'entries': TrackerEntry.objects.filter(user=request.user),
            })

    entries = TrackerEntry.objects.filter(user=request.user)
    return render(request, 'tracker.html', {'entries': entries})
def tracker_list(request): 
    tracker_entries = TrackerEntry.objects.all() 
    return render(request, 'tracker/tracker_list.html', {'tracker_entries': tracker_entries}) 

def add_tracker(request): 
    if request.method == 'POST': 
        form = TrackerEntryForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('tracker_list') 
        else: form = TrackerEntryForm() 
        return render(request, 'tracker/add_tracker.html', {'form': form}) 


def add_exercise(request, pk): 
    tracker_entry = get_object_or_404(TrackerEntry, pk=pk)
    if request.method == 'POST': 
        # Get data from the POST request
        exercise_name = request.POST.get('exercise_name')
        sets = request.POST.get('sets')
        reps = request.POST.get('reps')
        weight = request.POST.get('weight')

        # Validate required fields
        if exercise_name and sets and reps:
            # Create a new Exercise entry
            exercise = Exercise(
                tracker_entry=tracker_entry,
                exercise_name=exercise_name,
                sets=sets,
                reps=reps,
                weight=weight
            )
            exercise.save()
            return redirect('tracker_list')  # Redirect to the tracker list
        else:
            # Handle missing data error
            return render(request, 'tracker/add_exercise.html', {
                'error': 'Please fill out all required fields.'
            })

    return render(request, 'tracker/add_exercise.html')

def log_mood(request, pk): 
    tracker_entry = get_object_or_404(TrackerEntry, pk=pk)
    if request.method == 'POST': 
        # Get data from the POST request
        mood = request.POST.get('mood')
        energy_level = request.POST.get('energy_level')
        comments = request.POST.get('comments')

        # Validate required fields
        if mood and energy_level:
            # Create a new MoodLog entry
            mood_log = MoodLog(
                tracker_entry=tracker_entry,
                mood=mood,
                energy_level=energy_level,
                comments=comments
            )
            mood_log.save()
            return redirect('tracker_list')  # Redirect to the tracker list
        else:
            # Handle missing data error
            return render(request, 'tracker/log_mood.html', {
                'error': 'Please fill out all required fields.'
            })

    return render(request, 'tracker/log_mood.html')

# Events Calendar view
def events_calendar(request):
    events = Event.objects.all()
    return render(request, 'events_calendar.html', {'events': events})

# Event creation view
def add_event_view(request): 
    if request.method == 'POST': 
        name = request.POST['name'] 
        date = request.POST['date'] 
        time = request.POST['time'] 
        location = request.POST['location'] 
        description = request.POST['description']
        event = Event( 
            name=name, 
            date=date, 
            time=time, 
            location=location, 
            description=description
            ) 
        event.save() 
        return redirect('events_calendar') 
    return render(request, 'add_event.html')

# Class Attendance view
#def class_attendance(request):
    #attendances = class_attendance.objects.all()
    #return render(request, 'class_attendance.html', {'attendances': "attendances"})

# List Attendance Records
#def attendance_list_view(request): 
    #attendances = Attendance.objects.all() 
    #return render(request, 'attendance_list.html', {'attendances': attendances})

# def add_attendance_view(request): 
    #if request.method == 'POST': 
        #class_name_id = request.POST['class_name'] 
        #member_id = request.POST['member'] 
        #attendance_date = request.POST['attendance_date'] 
        #status = request.POST['status'] 
        #class_name = get_object_or_404(GymClass, pk=class_name_id) 
        #member = get_object_or_404(User, pk=member_id) 
        #attendance = Attendance( 
            #class_name=class_name, 
            #member=member, 
            #attendance_date=attendance_date, 
            #status=status
         
        #attendance.save() 
        #return redirect('attendance_list') 
    #classes = GymClass.objects.all() 
    #members = User.objects.all() 
    #return render(request, 'add_attendance.html', {'classes': classes, 'members': members})



# Contact Us view
def contact_us_view(request):
    if request.method == 'POST':
        print("POST data:", request.POST)  # Debug statement
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone_number = request.POST.get('phone_number', '')
        preferred_workout_time = request.POST.get('preferred_workout_time', '')
        message = request.POST.get('message', '')
        
        if name and email and message:  # Ensure required fields are not empty
            contact_us = ContactUs(
                name=name,
                email=email,
                phone_number=phone_number,
                preferred_workout_time=preferred_workout_time,
                message=message
            )
            contact_us.save()
            print("Saved ContactUs object:", contact_us)  # Debug statement
            return redirect('homepage')
        else:
            print("Validation failed")  # Debug statement
            return render(request, 'contact_us.html', {'error': 'Please fill out all required fields.'})
    
    return render(request, 'contact_us.html')
def Home(request): 
    return render(request, 'home.html')

def personal_details(request):
    # Fetch the most recent personal detail entry
    details = PersonalDetail.objects.last()
    return render(request, 'save_personal_details.html', {'details': details})


def save_personal_details(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        bio = request.POST.get('bio')

        # Check if an entry with the same email already exists
        if PersonalDetail.objects.filter(email=email).exists():
            return HttpResponse("An entry with this email already exists.")

        try:
            personal_detail = PersonalDetail(
                name=name,
                age=age,
                address=address,
                email=email,
                phone_number=phone_number,
                bio=bio
            )
            personal_detail.save()
            return redirect('personal_details')  # Redirect to the view page
        except IntegrityError:
            return HttpResponse("Failed to save due to database constraints.")
    
    return render(request, 'personal_details_form.html')

def saved_details(request):
    # Fetch the most recent saved details
    details = PersonalDetail.objects.last()
    return render(request, 'save_personal_details.html', {'details': details})

