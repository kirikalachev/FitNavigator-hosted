from django.shortcuts import render

def quiz(request):
    return render(request, "Quiz/quiz.html")

def bmr(request):
    return render(request, "bmrCalculator/bmr.html")