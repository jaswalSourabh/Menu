from django.shortcuts import render

# Create your views here.

def welcome_page(request):

    return render(request, "welcome_page.html")


def dashboard(request):

    return render(request, "dashboard.html")


def help(request):

    return render(request,"help.html")

def search_bar(request):

    return render(request,"search.html")


def feedback(request):

    return render(request,"feedback.html")