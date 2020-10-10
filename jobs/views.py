from django.shortcuts import render
from jobs.models import Job

# Create your views here.
def home(request):
    #Bring in all the objects of the database.
    jobs = Job.objects
    return render(request,'jobs/home.html',{'jobs' : jobs})
