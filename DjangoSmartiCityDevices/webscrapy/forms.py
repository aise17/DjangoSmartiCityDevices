from django import forms

class CompanyForm(forms.Form):
    id = forms.UUIDField(show_hidden_initial=True)
    create_datetime = forms.DateTimeField(label='Fecha de creacion')
    url = forms.URLField(label='Url')
    name = forms.CharField(max_length=255, label='Nombre')

class Uploadfile(forms.Form):
    path = forms.FileField(label='file')