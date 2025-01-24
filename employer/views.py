from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from employer.forms import JobCreationForm
from employer.models import Job
from django.contrib import messages
from job_seeker.forms import JobApplicationForm
from job_seeker.models import Application

# Create your views here.
class JobListView(View):
    def get(self, request):
        jobs = Job.objects.all().order_by('-id')[:5]
        return render(request, 'employer/jobs/index.html', {'jobs': jobs})
    
class JobCreateView(View):
    def get(self, request):
        form = JobCreationForm()
        return render(request, 'employer/jobs/create.html', {'form': form})
    
    def post(self, request):
        form = JobCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job created successfully')
            return redirect('/jobs/create')
        messages.error(request, 'Fail to create job')
        return render(request, 'employer/jobs/create.html', {'form': form})
    
class JobSingleView(View):
    def get(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        is_registered = Application.objects.filter(user=request.user).exists()
        form = JobApplicationForm()
        context = {'single_job': job, 'form': form, 'is_registered': is_registered}
        return render(request, 'employer/jobs/single.html', context)
    
    def post(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        Application.objects.get_or_create(job=job, user=request.user)
        JobApplicationForm(request.POST)
        messages.success(request, 'Job application submitted successfully')
        return render(request, 'employer/jobs/single.html', {'single_job': job})
        
        
