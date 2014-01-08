from django.db.models.base import ObjectDoesNotExist
from django.template import RequestContext
from ultimate_screenwriter.screenwriter.forms import ScreenplayUploadForm

def screenplay_upload_form(request):
    return {
        'screenplay_upload_form': ScreenplayUploadForm()
    }
