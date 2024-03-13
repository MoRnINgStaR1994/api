from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import WorkoutPlan, DayllyGoals
from .serializers import WorkoutPlanSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_plan(request):
    plan_id = request.data['id']

    if not plan_id:
        return Response({'details': 'Id is not provided'}, status=status.HTTP_404_BAD_REQUEST)

    if not WorkoutPlan.objects.filter(id=plan_id).exists():
        return Response({'details': 'Workout plan does not exists'})

    object = WorkoutPlan.objects.get(id=plan_id)
    plan = WorkoutPlanSerializer(object)

    return Response({'id': plan.data['id'], 'data': plan.data})

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_plan(request):
    ser = WorkoutPlanSerializer(request.data)
    if not ser.is_valid(request.data):
        return Response({'details': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    
    reps = 1

    if 'rep_in_day' in ser.data:
        reps = ser.data.get('rep_in_day')

    plan = WorkoutPlan(name=ser.data.get('name'), description=ser.data.get('description'), workouts=ser.data.get('workouts'), duration=ser.data.get('duration'), rep_in_day=reps, owner=ser.data.get('owner'))
    plan.save()

    return Response({'success': ser.data})

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def set_current_achivment(request):
    
    if not 'owner' in request.data:
        return Response({'details': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
    
    if not 'weight' in request.data:
        return Response({'details': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

    goal = DayllyGoals(owner=request.data['owner'], weight=request.data['weight'])
    goal.save()

    return Response({'success': 'Achivment added'})

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_progress(request):
    
    if not 'owner' in request.data:
        return Response({'details': 'id not provided'}, status=status.HTTP_400_BAD_REQUEST)

    id = request.data['owner']
    goal = DayllyGoals.objects.filter(owner=id).values()

    return Response({'success': goal})