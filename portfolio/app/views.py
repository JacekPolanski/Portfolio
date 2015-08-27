from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Contact


class IndexView(View):
    def get(self, request):
        contact = get_object_or_404(Contact)

        template_data = {
            'contact': contact
        }

        return render(request, 'app/index.html', template_data)