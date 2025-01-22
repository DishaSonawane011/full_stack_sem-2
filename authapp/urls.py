from django.urls import path
from .views import (
    home, signup, login_view, logout_view, membership, workout,
    full_body_workout, cardio_blast, strength_training, yoga_flex,
    tracker, events_calendar, contact_us_view,
    add_event_view, add_tracker, add_exercise, log_mood,personal_details,save_personal_details
)

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('membership/', membership, name='membership'),
    path('workout/', workout, name='workout'),
    path('workout/full-body/', full_body_workout, name='full_body_workout'),
    path('workout/cardio-blast/', cardio_blast, name='cardio_blast'),
    path('workout/strength-training/', strength_training, name='strength_training'),
    path('workout/yoga-flex/', yoga_flex, name='yoga_flex'),
    path('tracker/', tracker, name='tracker'),
    path('tracker/add/', add_tracker, name='add_tracker'),
    path('tracker/<int:pk>/add_exercise/', add_exercise, name='add_exercise'),
    path('tracker/<int:pk>/log_mood/', log_mood, name='log_mood'),
    path('events_calendar/', events_calendar, name='events_calendar'),  
    #path('class_attendance/', class_attendance, name='class_attendance'),  
    path('contact_us/', contact_us_view, name='contact_us'),
    path('add_event/', add_event_view, name='add_event'),
    # path('attendance/', attendance_list_view, name='attendance_list'), 
    # path('add_attendance/', add_attendance_view, name='add_attendance'), 
    path('personal-details/', personal_details, name='personal_details'),
    path('save-personal-details/',save_personal_details, name='save_personal_details'),
]
