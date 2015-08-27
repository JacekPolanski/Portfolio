from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Contact, AboutMe


class IndexView(View):
    def get(self, request):
        contact = get_object_or_404(Contact)
        about_me = get_object_or_404(AboutMe)

        template_data = {
            'contact': contact,
            'about_me': about_me,
        }

        return render(request, 'app/index.html', template_data)