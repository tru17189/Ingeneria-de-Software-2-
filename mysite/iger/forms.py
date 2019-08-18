from django import forms
from .models import ListaDepartamento

class ListaDepartamentoForm(forms.ModelForm):
    class Meta:
        model = ListaDepartamento
        fields = ['coordinacion', 'departamento']




    def clean_departamento(self):

        departamento = self.cleaned_data.get('departamento')

        print (departamento)

        lista = [
            "ALTA VERAPAZ",
            "BAJA VERAPAZ",
            "CHIMALTENANGO",
            "CHIQUIMULA",
            "EL PROGRESO",
            "ESCUINTLA",
            "GUATEMALA 1",
            "GUATEMALA 2",
            "HUEHUETENANGO",
            "IZABAL",
            "JALAPA",
            "JUTIAPA",
            "PETÉN",
            "QUETZALTENANGO",
            "QUICHÉ",
            "RETALHULEU",
            "SACATEPÉQUEZ",
            "SAN MARCOS",
            "SANTA ROSA",
            "SOLOLÁ",
            "SUCHITEPÉQUEZ",
            "TOTONICAPÁN",
            "ZACAPA"
        ]
        
        if departamento not in lista:
            raise forms.ValidationError("NO PUEDE INGRESARSE", departamento, ", no es un departamento")

        return departamento