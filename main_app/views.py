from django.shortcuts import render

# Create your views here.
finches = [
  {'name': 'Loco', 'breed': 'gouldian', 'description': 'small and adventurous', 'age': 3},
  {'name': 'Homi', 'breed': 'house', 'description': 'gentle and loving', 'age': 2},
  {'name': 'Joe', 'breed': 'house', 'common redpoll': 'blends well with others', 'age': .5},
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })