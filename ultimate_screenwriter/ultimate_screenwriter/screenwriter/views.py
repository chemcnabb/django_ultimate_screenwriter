from django.shortcuts import render
from django.views.generic import TemplateView
import time, os
from django.http import HttpResponseRedirect
from ultimate_screenwriter.screenwriter.models import Screenplay,Slug, Action, Dialogue, Character, ScreenplayElements, Parentheses, ScreenplayElementType
from ultimate_screenwriter.screenwriter.forms import ScreenplayUploadForm
#from ultimate_screenwriter.common.script_processor import ScriptProcessor
# Create your views here.
class ScreenwriterView(TemplateView):
    template_name = "screenwriter/screenplay.html"
    screenplay_html = ""
    #screenplay = Screenplay.objects.get(title="Poltergeist")

    def get(self, request, *args, **kwargs):
        context = super(ScreenwriterView, self).get_context_data(**kwargs)
        screenplay = Screenplay.objects.get(slug=context['screenplay_slug'])

        return render(request, self.template_name, {
            'screenplay':screenplay,
        })

    def handle_uploaded_file(self, f):
        now = time.localtime(time.time())

        base_path = '/media/uploaded_screenplays/%s/%s/%s/%s' % (time.strftime("%Y", now), time.strftime("%m", now), time.strftime("%d", now),f)
        file_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..') + base_path)


        with open(file_path, 'wb+') as destination:
            #for chunk in f.chunks():
            destination.write(f)

        return destination

    def post(self, request, *args, **kwargs):
        form = ScreenplayUploadForm(request.POST, request.FILES)
        if form.is_valid():
            #screenplay_file = self.handle_uploaded_file(form.cleaned_data['docfile'])
            screenplay = Screenplay(screenplay_document = form.cleaned_data['docfile'])
            screenplay.save()






            #screenplay_elements = ScreenplayElements.objects.filter(screenplay = screenplay).order_by('sort_order')
            #
            #newdoc.save()

            # Redirect to the document list after POST

            return HttpResponseRedirect('/')
        else:
            print form

    def build_screenplay_html(self):
        for element in self.screenplay_elements:
            print element
            self.screenplay_html += self.get_element_html(element)

    def get_element(self, element):
        if element.element_type.name == "action":
            return Action.objects.get(pk=element.element_id)
        if element.element_type.name == "slug":
            return Slug.objects.get(pk=element.element_id)
        if element.element_type.name == "character":
            return Character.objects.get(pk=element.element_id)
        if element.element_type.name == "dialogue":
            return Dialogue.objects.get(pk=element.element_id)
        if element.element_type.name == "parentheses":
            return Parentheses.objects.get(pk=element.element_id)

    def get_element_content(self, element):
        if element.element_type.name == "action":
            return self.get_element(element).action
        if element.element_type.name == "slug":
            return self.get_element(element).slug
        if element.element_type.name == "character":
            return self.get_element(element).name
        if element.element_type.name == "dialogue":
            return self.get_element(element).dialogue_text
        if element.element_type.name == "parentheses":
            return self.get_element(element).parentheses

    def get_element_html(self, element):
        if element.element_type.name == "action":
            return "<div id='action_"+str(element.element_id)+"'>" + self.get_element_content(element).encode('utf-8', 'ignore') + "</div>"
        if element.element_type.name == "slug":
            #print ScreenplayElements.objects.filter(Q(parent = element) | Q(parent__parent = element))
            return "<h1 id='slug_"+str(element.element_id)+"'>" + self.get_element_content(element).encode('utf-8', 'ignore') + "</h1>"
        if element.element_type.name == "character":
            return "<h2 id='character_"+str(element.element_id)+"'>" + self.get_element_content(element).encode('utf-8', 'ignore') + "</h2>"
        if element.element_type.name == "dialogue":
            return "<h3 id='dialogue_"+str(element.element_id)+"'>" + self.get_element_content(element).encode('utf-8', 'ignore') + "</h3>"
        if element.element_type.name == "parentheses":
            return "<h4 id='parentheses_"+str(element.element_id)+"'>" + self.get_element_content(element).encode('utf-8', 'ignore') + "</h4>"

    def get_context_data(self, **kwargs):
        self.build_screenplay_html()
        return {'data': self.screenplay_html}


