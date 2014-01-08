from django.template import RequestContext
from ultimate_screenwriter.screenwriter.forms import ScreenplayUploadForm

class ScreenplayMiddleware(object):
    """
    Available in all pages
    """
    def process_view(self, request, view_func, view_args, view_kwargs):
        request.screenplay_upload_form = ScreenplayUploadForm()


