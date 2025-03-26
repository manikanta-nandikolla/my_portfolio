from django.shortcuts import render
from .models import PersonalDetail, Education, Skill, Project, ContactMessage
# Create your views here.

def home(request):
    personal_info = PersonalDetail.objects.first()
    education = Education.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()

    context = {
        'personal_info': personal_info,
        'education': education,
        'skills': skills,
        'projects': projects,
        "education": education,
    }
    return render(request, 'home.html', context)