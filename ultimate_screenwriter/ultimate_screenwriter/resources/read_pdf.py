from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
#from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage

from pprint import pprint
import sys
import re

password = ""


class SreenplayPdfProcessor:
    screenplay_object_list = []
    char_margin = False

    def __init__(self, pdf):
        self.document = pdf
        #initialize parsing parameters
        self.file_pointer = open(self.document.name, 'rb')
        self.parser = PDFParser(self.file_pointer)
        self.pdf_document = PDFDocument(self.parser)
        self.pdf_document.initialize()
        # set resaource management
        self.resource_manager = PDFResourceManager()
        self.pdf_device = PDFPageAggregator(self.resource_manager, laparams=LAParams())
        #set interpreter
        self.interpreter = PDFPageInterpreter(self.resource_manager, self.pdf_device)
        #self.file_pointer.close()

    def get_pages(self, *args):
        screenplay_object_list = [] # a list of strings, each representing text collected from each page of the doc
        counter = 0
        for page in PDFPage.create_pages(self.pdf_document):
            self.interpreter.process_page(page)
            # receive the LTPage object for this page
            processed_pdf_page = self.pdf_device.get_result()
            # processed_pdf_page is an LTPage object which may contain child objects like LTTextBox, LTFigure, LTImage, etc.
            screenplay_object_list.append(self.get_screenplay_element_objects(processed_pdf_page, (counter+1), '/tmp/'))
            counter+=1

        return screenplay_object_list

    def is_left_justified(self, page_object):
        return page_object.x0 == 108 or page_object.x0 == 90

    def is_character_margin(self, pdf_page_object):
        #print pdf_page_object
        margin_list = [252,]
        if pdf_page_object.x0 in margin_list:
            self.char_margin = True
            return True
        else:
            self.char_margin = False

    def is_dialogue_margin(self, pdf_page_object):

        margin_list = [180,]
        if pdf_page_object.x0 in margin_list:
            return True
        return False

    def remove_block_from_holder(self, item):
        if type(item) == tuple:
            item = " ".join(item)
        self.text_block_holder = self.text_block_holder.replace(item, "")

    def add_item_to_screenplay_object_list(self, item_type, func):
        item = func()
        if item:
            self.remove_block_from_holder(item)
            self.screenplay_object_list.append(dict(name=item_type, content=item))

    def get_screenplay_element_objects (self, pdf_page_objects, page_number, images_folder):
        """Iterate through the list of LT* objects and capture the text or image data contained in each"""
        text_content = []

        for pdf_page_object in pdf_page_objects:

            if isinstance(pdf_page_object, LTTextBox):

                self.text_block_holder = pdf_page_object.get_text()

                if self.text_block_holder.strip() != "":

                    if self.is_left_justified(pdf_page_object):
                        #ACTION and HEADINGS
                        self.add_item_to_screenplay_object_list("slug", self.get_heading)
                        self.add_item_to_screenplay_object_list("action", self.get_action)

                    elif self.is_character_margin(pdf_page_object):
                        #CHARACTER and DIALOGUE

                        self.add_item_to_screenplay_object_list("character", self.get_character_name)
                        self.add_item_to_screenplay_object_list("parentheses", self.get_parentheses)

                    elif self.is_dialogue_margin(pdf_page_object):
                        self.add_item_to_screenplay_object_list("dialogue", self.get_dialogue)

                    elif pdf_page_object.x0 > 400:
                        # TRANSITONS
                        continue

        return self.screenplay_object_list

    def get_element(self, search_string):
        element = re.findall(search_string, self.text_block_holder)
        try:
            element = element[0]
        except IndexError:
            pass
        if element:
            return element

        return None

    def get_character_name(self):
        character_name = self.get_element("([^<>a-z\s][^...][^a-z:\!\?]*?[^a-z\(\!\?:,][\s]??)\n{1}")
        if character_name:

        #character_name = self.get_element("([A-Z]{2,})")
        #character_name = self.get_element("([^<>a-z\s].[A-Z:\!\?][^...]([A-Z:\!\?]| ){4,})")
            if self.char_margin:
                #character_name = self.get_element("([^<>a-z\s].[A-Z:\!\?][^...]([A-Z:\!\?]| ){4,})")

                #print character_name
                return character_name
        else:
            return None

    def get_parentheses(self):
        return self.get_element("(\([^<>]*?\)[\s]??)")

    def get_dialog(self):
        return self.get_element(".*|.*\n{0,1}(.+?)\n")

    def get_heading(self):
        heading = self.get_element("((INT|EXT|[^a-zA-Z0-9]EST)([\.\-\s]+?).+)")
        try:
            heading = heading[0]
        except TypeError:
            pass

        return heading

    def get_action(self):
        return self.text_block_holder

    def get_dialogue(self):
        return self.text_block_holder

