from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de la tarea", max_length=200)
    description = forms.CharField(
        label="Descripción de la tarea", widget=forms.Textarea)


class CreateProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200)
