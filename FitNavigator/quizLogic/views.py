import random
from django.shortcuts import render, redirect
from .models import Home_Workout
from .models import Busy_Workout
from .models import Free_Workout
from .models import Diet_Tips

def quiz(request):

    if request.method == "POST":
        env = request.POST.get('env')
        gender = request.POST.get('gender')
        goals = request.POST.get('goals')
        time = request.POST.get('time')
        bodytype = request.POST.get('bodytype')
        current_index = int(request.POST.get('current_index', 0))

        all_workouts = []
        diet_tips = []

        if env == "home":
            all_workouts = list(Home_Workout.objects.filter(gender=gender))
        elif env == "gym":
            if time == "busy":
                all_workouts = list(Busy_Workout.objects.filter(gender=gender))
            else:
                all_workouts = list(Free_Workout.objects.filter(gender=gender))

        random.shuffle(all_workouts)

        if 'next_button' in request.POST:
            current_index = (current_index + 1) % len(all_workouts)

        diet_tips = list(Diet_Tips.objects.filter(goals = goals, bodytype = bodytype))

        return render(request, 'Quiz/results.html', {'all': all_workouts, 'tips': diet_tips})
    
    return render(request, "Quiz/quiz.html",)

def bmi(request):
    if request.method == 'POST':
        weight = request.POST['weight']
        height = request.POST['height']
        
        result = int(weight)/(int(height)/100)**2
        return render(request,'calculators/bmi.html',{'result':round(result)})
 
    return render(request,"calculators/bmi.html")

def results(request):

    # if 'next_button' in request.POST:
    #             current_index = (current_index + 1) % len(all_workouts)

    return render(request,"Quiz/results.html")