from django import forms

class taskInputForm(forms.Form):
    status_task = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'your ToDo list'}))

