from django import forms


class StudentNumberForm(forms.Form):
    number = forms.IntegerField(label="Number of students", min_value=1, max_value=100)
