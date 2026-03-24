from django.core.management.base import BaseCommand, CommandError
from api.models import *
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Generates dummy data for testing"
    print("Generating dummy data for testing...")

    def clear_data():
        User.objects.all().delete()

    def create_users():
        users = []

        user_data = [
            ("test_user_1", "1"),
            ("test_user_2", "2"),
            ("test_user_3", "3")
        ]

        for username, password in user_data:
            user, created = User.objects.get_or_create(username = username)
            if created:
                user.set_password(password)
                user.save()
            users.append(user)
        return users

    def create_exercises():
        exercises = []

        exercise_data = [
            ("Bench Press", "Chest compound movement targeting pectorals, triceps, and anterior deltoids"),
            ("Squat", "Lower body compound movement targeting quads, glutes, and hamstrings"),
            ("Deadlift", "Full-body compound movement emphasizing posterior chain including glutes, hamstrings, and lower back"),
            ("Pull Up", "Upper body pulling movement targeting lats, biceps, and upper back"),
            ("Shoulder Press", "Overhead pressing movement targeting deltoids and triceps"),
            ("Lateral Raise", "Isolation exercise targeting the medial deltoids for shoulder width"),
            ("Bicep Curl", "Isolation exercise targeting the biceps brachii"),
            ("Tricep Pushdown", "Isolation exercise targeting the triceps, especially the lateral head"),
        ]

        for exercise_name, exercise_desc in exercise_data:
            exercise, created = Exercise.objects.get_or_create(
                name = exercise_name,
                defaults={"description": exercise_desc})
            exercises.append(exercise)

        return exercises


    

        
