from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def gettask(request):
    if request.method == "GET":
        tasks = list(Task.objects.values())
        return JsonResponse(tasks,safe=False)

@csrf_exempt
def add(request):
    if request.method=='POST':
        data = json.loads(request.body)
        Task.objects.create(title=data.get('title'),disc=data.get('disc',""))
        return JsonResponse({"message":"task completed"})
    
@csrf_exempt
def update(request, id):
    if request.method == 'PUT':
        try:
            utask = Task.objects.get(id=id)

            # ✅ ONLY toggle
            utask.completed = not utask.completed

            utask.save()
            return JsonResponse({"message": 'task updated'})

        except Task.DoesNotExist:
            return JsonResponse({'ERROR': "Task not found"}, status=404)
        
@csrf_exempt
def delete(request,id):
    if request.method == 'DELETE':
        try:
            dtask = Task.objects.get(id=id)
            dtask.delete()
            return JsonResponse({'message':'task is deleted'})
        
        except Task.DoesNotExist:
            return JsonResponse({'ERROR':"Task not found"},status=404)
        
            

        



