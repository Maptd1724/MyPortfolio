from django.shortcuts import render
from django.http import HttpResponse

from .models import Skill
from skills.models import Skill
from works.models import Work


def skills(request):
    skills = Skill.objects.order_by('title')

    context = {
        'skills': skills
    }
    return render(request, 'skills/skills.html', context)

def works(request):
    works = Work.objects.order_by('title')
    
    context = {
        'works': works
    }
    return render(request, 'works/works.html', context)


