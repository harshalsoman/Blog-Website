from django import forms
from .models import  *

class DataForm(forms.ModelForm):
    class Meta:
        model= blogform
        fields = '__all__'


#class ImageForm(forms.ModelForm):
    #class Meta:
   #     model=Image
      #  fields = '__all__'
     #   labels = {'pic': ''}