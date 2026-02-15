from django.db import models

class User(models.Model):
    usernname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Plan(models.Model):
    title = models.CharField(max_length=100)

class Log(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)

class Routine(models.Model):
    title = models.CharField(max_length=100)

class Exercise(models.Model):
    exercises = {"Pendulum swings", "Passive shoulder flexion (stick or towel assist)", "Wall slides", "Isometric external rotation", "Isometric internal rotation", "Resistance band rows", "Resistance band external rotation", "Resistance band internal rotation", "Scapular retractions", "Shoulder flexion with light dumbbell"}
