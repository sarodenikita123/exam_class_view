from django import forms
from .models import HallTicket


class HallTicketForm(forms.ModelForm):
    class Meta:
        model = HallTicket
        fields = "__all__"

        widgets = {
            "candidate_name": forms.TextInput(attrs={"class": "form-control"}),
            "mother_name": forms.TextInput(attrs={"class": "form-control"}),
            "father_name": forms.TextInput(attrs={"class": "form-control"}),
            "exam_name": forms.TextInput(attrs={"class": "form-control"}),
            "center": forms.TextInput(attrs={"class": "form-control"}),
            "date_of_exam": forms.TextInput(attrs={"type": "date"}),
            "time": forms.TextInput(attrs={"type": "time"}),
        }
