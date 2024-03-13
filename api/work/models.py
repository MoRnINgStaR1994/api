from django.db import models

class Muscles(models.Model):
    name = models.CharField(max_length=50)

class WorkOuts(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    instructions = models.CharField(max_length=500, default='')
    target_muscles = models.ForeignKey(Muscles, models.DO_NOTHING, default=0)
    recomended_sets = models.IntegerField(default=1)
    recomended_rep = models.IntegerField(default=10)

class WorkoutPlan(models.Model):
    owner = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    workouts = models.CharField(max_length=500, default='') #space seperated string of ids of workouts
    duration = models.DateField()
    rep_in_day = models.IntegerField(default=1)

class DayllyGoals(models.Model):
    owner = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)