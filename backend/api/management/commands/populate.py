from django.core.management.base import BaseCommand, CommandError
from api.models import *
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = "Generates dummy data for testing"

    SEED = 2
    random.seed(SEED)

    def handle(self, *args, **options):
        self.stdout.write("Generating dummy data for testing...")

    def create_users(self, seed=SEED):
        users = []

        user_data = [(f"test_user_{i}", str(i)) for i in range(seed)]

        for username, password in user_data:
            user, created = User.objects.get_or_create(username = username)
            if created:
                user.set_password(password)
                user.save()
            users.append(user)
        return users

    def create_exercises(self, seed=SEED):
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

    def generate_data(self, users: list[User], exercises: list[Exercise], seed=SEED):

        # Define the plans
        plans: list[Plan] = []

        for user in users:  # can be better extended with seed
            planA = Plan.objects.create(
                title=f"{user} Plan A",
                description=f"{user}'s first plan.",
                user=user)
            plans.append(planA)
            planB = Plan.objects.create(
                title=f"{user} Plan B",
                description=f"{user}'s second plan.",
                user=user)
            plans.append(planB)

        # define the routines
        routines = []

        for plan in plans:
            routineA = Routine.objects.create(
                title=f"{plan.title} Routine A",
                description=f"{plan.title} Routine A: to be completed... other instructions...",
                plan=plan)
            routines.append(routineA)
            routineB = Routine.objects.create(
                title=f"{plan.title} Routine B",
                description=f"{plan.title} Routine B: to be completed... other instructions...",
                plan=plan)
            routines.append(routineB)



    

        
