from django.shortcuts import render
from django.views.generic import TemplateView
from ultimate_screenwriter.screenwriter.models import Screenplay



# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)


        return render(request, self.template_name, {})


# Create your views here.
class ProfileView(TemplateView):
    template_name = "accounts/profile.html"


    def get(self, request, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        screenplays = Screenplay.objects.filter(user=request.user)

        return render(request, self.template_name, {
            'screenplays':screenplays,
        })

