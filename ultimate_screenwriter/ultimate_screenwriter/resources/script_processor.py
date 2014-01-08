# coding=utf-8
from django.conf import settings
import os

from read_pdf import SreenplayPdfProcessor




settings.configure(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".."), 'db.screenwriter'),
    }
}, MEDIA_ROOT="../media/")
from ultimate_screenwriter.screenwriter.models import Slug, Action, Dialogue, Character, Screenplay, ScreenplayElements, Parentheses, ScreenplayElementType
directory = os.path.dirname(__file__)
from pprint import pprint

class ScriptProcessor:



    def __init__(self, file_name):
        self.file_name = file_name
        self.set_screenplay_title(self.file_name)
        self.screenplay = Screenplay.objects.get_or_create(name=self.title)[0]
        self.screenplay.screenplay_document = os.path.abspath(os.path.join('../media',self.screenplay.screenplay_document.name))

        self.is_file_or_error()

        self.pdf_processor = SreenplayPdfProcessor(self.screenplay.screenplay_document)

        self.set_screenplay_json()

    def is_file_or_error(self):
        if not os.path.isfile(self.screenplay.screenplay_document.name):
            raise Exception, "file " + self.screenplay.screenplay_document.name + " not found."

    def set_screenplay_json(self):
        self.screenplay_element_dict = self.pdf_processor.get_pages(self.screenplay.screenplay_document)



    def remove_non_alpha(self, title):
        tmp_title = []
        for e in title:
            if not e.isalnum():
                title = title.replace(e, " ")
        return title, tmp_title

    def filter_and_capitalize(self, title, tmp_title):
        for word in title.split(" "):
            if word in ["screenplay"]:
                continue
            tmp_title.append(word.capitalize())


    def set_screenplay_title(self, title):
        title, tmp_title = self.remove_non_alpha(title)
        self.filter_and_capitalize(title, tmp_title)
        self.title = " ".join(tmp_title)




    def insertNewLine(self, text, lineLength, spaces=12):
        if len(text) < lineLength:
            return text
        else:
            newtext = text[text[lineLength - 1:].find(' ') + lineLength:]
            if text.find(' ') == -1:
                return text
            else:
                return text[:text[lineLength - 1:].find(' ') + lineLength] + '\n' + str(
                    " " * spaces) + self.insertNewLine(newtext, lineLength, spaces)


    def add_formatting_spaces(self, element_name, number=False):
        margin_num = 15
        margin = str(" " * margin_num)

        if element_name == "slug":
            if number:
                return margin_num
            return margin

        elif element_name == "character":
            if number:
                return margin_num + 20
            return margin + str(" " * 20)

        elif element_name == "transition":
            if number:
                return margin_num + 16
            return margin + str(" " * 16)

        elif element_name == "action":
            if number:
                return margin_num
            return margin

        elif element_name == "dialogue":
            if number:
                return margin_num + 10
            return margin + str(" " * 10)

        elif element_name == "parentheses":
            if number:
                return margin_num + 14
            return margin + str(" " * 14)


    def output_txt(self):
        returnVal = ""
        for element in self.screenplay_element_dict[0]:
            if element["name"] == "slug":
                returnVal += self.add_formatting_spaces(element["name"]) + element["content"]

            elif element["name"] == "character":
                returnVal += "" + self.add_formatting_spaces(element["name"]) + element["content"]

            elif element["name"] == "transition":
                returnVal += self.add_formatting_spaces(element["name"]) + element["content"]

            elif element["name"] == "action":
                returnVal += self.add_formatting_spaces(element["name"]) + self.insertNewLine(
                    element["content"].replace("\n", ""), 60, self.add_formatting_spaces(element["name"], True)) + "\n\n"

            elif element["name"] == "dialogue":

                dialog = element["content"]
                returnVal += "\n" + self.add_formatting_spaces(element["name"]) + self.insertNewLine(
                    dialog.replace("\n", ""), 30, self.add_formatting_spaces(element["name"], True)) + "\n\n"

            elif element["name"] == "parentheses":
                returnVal += "\n" + self.add_formatting_spaces(element["name"]) + self.insertNewLine(
                    element["content"].replace("\n", ""), 20, self.add_formatting_spaces(element["name"], True))

        print returnVal
        #out_script = open(directory + '/tmp/' + self.file_name + '.txt', 'w+')
        #out_script.write(returnVal.encode('utf-8', 'ignore')) #processor.screenplay_cleaned.encode('utf-8','ignore')


    def write_to_db(self):
        sort_order = 0

        for line in self.screenplay_element_dict:


            if line["name"] == "slug":
                heading = Slug.objects.get_or_create(slugfield=line["content"])
                try:
                    heading.save()
                except AttributeError:
                    heading = heading[0]
                    heading.save()
                script_elements = ScreenplayElements.objects.get_or_create(element_id=heading.id,
                                                     element_type=ScreenplayElementType.objects.get_or_create(name=line["name"])[0],
                                                     parent=None, screenplay=self.screenplay, sort_order=sort_order)[0]
                script_elements.save()

            elif line["name"] == "character":
                character = Character.objects.get_or_create(name=line["content"])
                try:
                    character.save()
                except AttributeError:
                    character = character[0]
                    character.save()


                try:
                    parent = script_elements
                except NameError:
                    parent = None

                script_elements = ScreenplayElements(element_id=character.id,
                                                     element_type=ScreenplayElementType.objects.get_or_create(name=line["name"])[0],
                                                     parent=parent, screenplay=self.screenplay, sort_order=sort_order)
                script_elements.save()

            # elif line["name"] == "TRANSITION":
            #     transition = Transition(line["content"])
            #     transition.save()

            elif line["name"] == "action":
                action = Action(action=line["content"])
                action.save()

                try:
                    parent = script_elements
                except NameError:
                    parent = None

                script_elements = ScreenplayElements(element_id=action.id,
                                                     element_type=ScreenplayElementType.objects.get_or_create(name=line["name"])[0],
                                                     parent=parent,
                                                     screenplay=self.screenplay,
                                                     sort_order=sort_order)
                #script_elements.save()


            elif line["name"] == "dialogue":

                dialog = Dialogue(dialogue_text=line["content"])
                dialog.save()

                try:
                    parent = script_elements
                except NameError:
                    parent = None

                script_elements = ScreenplayElements(element_id=dialog.id,
                                                     element_type=ScreenplayElementType.objects.get_or_create(name=line["name"])[0],
                                                     parent=parent, screenplay=self.screenplay, sort_order=sort_order)
                script_elements.save()

            elif line["name"] == "parentheses":
                parentheses = Parentheses(parentheses=line["content"])
                parentheses.save()

                try:
                    parent = script_elements
                except NameError:
                    parent = None

                script_elements = ScreenplayElements(element_id=parentheses.id,
                                                     element_type=ScreenplayElementType.objects.get_or_create(
                                                         name=line["name"])[0], parent=parent,
                                                     screenplay=self.screenplay, sort_order=sort_order)
                script_elements.save()

        sort_order += 1


    def special(self):
        pass


if __name__ == "__main__":
    pdf_name = "Poltergeist"

    processor = ScriptProcessor(pdf_name)
    processor.output_txt()
    #processor.write_to_db()


