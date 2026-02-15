from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='plans'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.user.username}"

class Routine(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    plan = models.ForeignKey(
        Plan, 
        on_delete=models.CASCADE,
        related_name='routines'
    )
    order = models.PositiveIntegerField(default=0) 

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    routine = models.ForeignKey(
        Routine, 
        on_delete=models.CASCADE,
        related_name='exercises'
    )
    sets = models.PositiveIntegerField(null=True, blank=True)
    reps = models.PositiveIntegerField(null=True, blank=True)
    duration_seconds = models.PositiveIntegerField(null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.name

class Log(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='logs'
    )
    routine = models.ForeignKey(  
        Routine, 
        on_delete=models.CASCADE,
        related_name='logs'
    )
    date_time = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)  
    completed = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_time']

    def __str__(self):
        return f"{self.user.username} - {self.routine.title} - {self.date_time.date()}"