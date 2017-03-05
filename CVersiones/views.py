from django.views.generic.base import TemplateView  

# Create your views here.
class InicioView(TemplateView):
    template_name="CVersiones/index.html"