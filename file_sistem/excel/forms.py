from django import forms


class PathForm(forms.Form):
    path = forms.CharField(label='Путь к файлам', widget=forms.TextInput(attrs={'size': 60}))
