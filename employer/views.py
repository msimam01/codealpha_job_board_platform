from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
class JobListView(View):
    def get(self, request):
        return render(request, 'employer/jobs/index.html', {})
