from django.shortcuts import render

def about(request):
    return render(request, "about/about.html")

# def aboutUs(request):
#     return render(request, "about/about.html#aboutUs")

# def about1(request):
#     return render(request, "about/about.html#1")

# def about2(request):
#     return render(request, "about/about.html#2")

# def about3(request):
#     return render(request, "about/about.html#3")

# def aboutContacts(request):
#     return render(request, "about/about.html#contacts")
