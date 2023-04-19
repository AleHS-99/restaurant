from django.shortcuts import render
from django.views.generic import ListView

from .models import *
# Create your views here.
def Home(request):
    return render(request,'index.html')

class MenuPage(ListView):
    model = oferta
    template_name = 'Menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = oferta.objects.all()
        a = []
        for i in modalidad.objects.all():
            a.append((i.codigo,i.modal,i.modal.replace(' ','')))
        context['modal'] = a
        return context