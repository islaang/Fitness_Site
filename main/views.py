from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def nutrition(request):
    return render(request, 'pages/nutrition.html')

def clothing(request):
    return render(request, 'pages/clothing.html')

def workouts(request):
    return render(request, 'pages/workouts.html')

def chatbot(request):
    return render(request, 'pages/chatbot.html')

def cart(request):
    return render(request, 'pages/cart.html')
