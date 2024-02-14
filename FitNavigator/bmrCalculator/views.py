from django.shortcuts import render

def bmr(request):
    return render(request, "bmrCalculator/bmr.html")
