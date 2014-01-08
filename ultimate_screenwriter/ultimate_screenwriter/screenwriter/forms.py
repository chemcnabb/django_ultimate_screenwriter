# -*- coding: utf-8 -*-
from django import forms

class ScreenplayUploadForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )
