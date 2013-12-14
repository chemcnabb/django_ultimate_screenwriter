from django.shortcuts import render
from django.views.generic import TemplateView
from models import Screenplay

# Create your views here.
class ScreenwriterView(TemplateView):
    template_name = "screenwriter/screenplay.html"

    def get(self, request, *args, **kwargs):
        context = super(ScreenwriterView, self).get_context_data(**kwargs)
        screenplay = Screenplay.objects.get(slug=context['screenplay_slug'])

        return render(request, self.template_name, {
            'screenplay':screenplay,
        })
