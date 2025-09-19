from django import forms

from  first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields ="__all__"

        widgets={
        "address":forms.Textarea(attrs={"rows":"1","cols":"1"}),
        }