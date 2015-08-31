from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Contact, AboutMe, Skill, Project, Community

import json


class IndexView(View):
    def get(self, request):
        contact = get_object_or_404(Contact)
        about_me = get_object_or_404(AboutMe)
        skills = get_list_or_404(Skill)
        not_owned_projects = get_list_or_404(Project.objects.filter(is_owner=False))
        owned_projects = get_list_or_404(Project.objects.filter(is_owner=True))
        communities = get_list_or_404(Community)

        template_data = {
            'contact': contact,
            'about_me': about_me,
            'skills': skills,
            'owned_projects': owned_projects,
            'not_owned_projects': not_owned_projects,
            'communities': communities,
        }

        return render(request, 'app/index.html', template_data)


def email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email_address = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            'Nowa wiadomość od '+name,
            message,
            email_address,
            ['jacek.polanski.91@gmail.com'],
            fail_silently=False
        )

        return HttpResponse(
            json.dumps({
                'result': 'Success',
                'name': name,
                'email': email_address,
                'message': message,
            }),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({'result': 'error'}),
            content_type="application/json"
        )

