from rest_framework import serializers
from .models import WorkoutPlan

class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = WorkoutPlan
        fields = ['id', 'name', 'description', 'workouts', 'duration', 'rep_in_day', 'owner']

    @classmethod
    def is_valid(self, data):
        if not data:
            return False
        
        if not 'name' in data:
            return False
        
        if not 'description' in data:
            return False
        
        if not 'duration' in data:
            return False
        
        if not 'workouts' in data:
            return False
        
        if not 'owner' in data:
            return False
        
        return True