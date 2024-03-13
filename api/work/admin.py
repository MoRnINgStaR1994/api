from django.contrib import admin
from .models import WorkOuts, Muscles, WorkoutPlan, DayllyGoals

# Register your models here.
admin.site.register(WorkOuts)
admin.site.register(Muscles)
admin.site.register(WorkoutPlan)
admin.site.register(DayllyGoals)
