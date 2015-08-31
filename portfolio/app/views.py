from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import View
from .models import Contact, AboutMe, Skill, Project


class IndexView(View):
    def get(self, request):
        contact = get_object_or_404(Contact)
        about_me = get_object_or_404(AboutMe)
        skills = get_list_or_404(Skill)
        not_owned_projects = get_list_or_404(Project.objects.filter(is_owner=False))
        owned_projects = get_list_or_404(Project.objects.filter(is_owner=True))

        template_data = {
            'contact': contact,
            'about_me': about_me,
            'skills': skills,
            'owned_projects': owned_projects,
            'not_owned_projects': not_owned_projects
        }

        return render(request, 'app/index.html', template_data)