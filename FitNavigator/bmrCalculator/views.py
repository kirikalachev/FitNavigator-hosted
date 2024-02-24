from django.shortcuts import render

def bmr(request):
    if request.method == 'POST':
        weight = request.POST['weight']
        height = request.POST['height']
        age = request.POST['age']
        gender = request.POST['gender']
        
        if gender == 'male':
            result = 66.47 + (13.75 * int(weight)) + (5.003 * int(height)) - (6.755 * int(age))
            return render(request,'calculators/bmr.html',{'result':round(result)})
        if gender == 'female':
            result = 655.1 + (9.563 * int(weight)) + (1.850 * int(height)) - (4.676 * int(age))
            return render(request,'calculators/bmr.html',{'result': round(result)})
        
    return render(request, "calculators/bmr.html")
