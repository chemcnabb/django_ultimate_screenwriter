from django.views.generic import TemplateView
from screenwriter.models import Slug, Action, Dialogue, Character, Screenplay, ScreenplayElements, Parentheses, ScreenplayElementType
from django.db.models.query import Q

class HomePage(TemplateView):
    template_name = "home.html"
    screenplay_html = ""
    screenplay = Screenplay.objects.get(title="Poltergeist")
    screenplay_elements = ScreenplayElements.objects.filter(screenplay = screenplay).order_by('sort_order')

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

