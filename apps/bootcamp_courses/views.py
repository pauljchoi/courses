from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
       'all_courses': Course.objects.all(),

    }
    return render(request, 'bootcamp_courses/index.html', context)

def create(request):
    if request.method == 'POST':
        Course.objects.create(course_name = request.POST['course_name'], description=request.POST['description'])
    return redirect('/')

def remove(request, id):
    context = {
         'course': Course.objects.get(id= id)
    }
    return render(request, 'bootcamp_courses/remove.html', context)

def delete(request, id):
    this = Course.objects.get(id= id)
    this.delete()
    return redirect('/')
