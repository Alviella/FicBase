from django.views.generic import TemplateView


class BasePageViewer(TemplateView):
    template_name = 'MainPage.html'