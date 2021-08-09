from django.forms import ModelForm

from .models import Csv, SalesManager


class CsvModelForm(ModelForm):
    class Meta:
        model = Csv
        fields = ("file_name",)


class SalesManagerForm(ModelForm):
    class Meta:
        model = SalesManager
        fields = [
            "first_name",
            "last_name",
            "sales_branch",
            "area",
            "position",
            "supervisor",
            "phone_number",
            "email",
            "is_active",
            "photo",
        ]
        labels = {
            "first_name": "Imię",
            "last_name": "Nazwisko",
            "sales_branch": "Oddział",
            "area": "Rejon",
            "position": "Stanowisko",
            "supervisor": "Numer przełożonego",
            "phone_number": "Numer pracownika",
            "email": "Email pracownika",
            "is_active": "Czy aktywny",
            "photo": "Zdjęcie",
        }
