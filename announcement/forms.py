from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class AnnouncementForm(forms.ModelForm):
    title = forms.CharField()
    number_vacancies = forms.CharField()
    city = forms.ModelChoiceField(queryset=City.objects.all())
    prerequisites = forms.CharField()
    note = forms.CharField()
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Announcement
        exclude = ['created', 'updated', 'user', 'email']
        
    def __init__(self, *args, **kwargs):
        super(AnnouncementForm, self).__init__(*args, **kwargs)

    # Header Image Field
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['number_vacancies'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['prerequisites'].widget.attrs['class'] = 'form-control'
        self.fields['note'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['money'].widget.attrs['class'] = 'form-control'
        self.fields['type_vacancy'].widget.attrs['class'] = 'form-control'
