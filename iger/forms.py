from django import forms
from .models import ListaDepartamento
#Clase que tiene la funcion de validar el ingreso de departamentos nuevos
#verificando que el departamento ingresado si exista, buscandolo dentro de una lista
#de los Departamentos que existen en Guatemala
class ListaDepartamentoForm(forms.ModelForm):
    class Meta:
        model = ListaDepartamento
        fields = ['coordinacion', 'departamento']




    def clean_departamento(self):

        departamento = self.cleaned_data.get('departamento')


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
            raise forms.ValidationError("NO PUEDE INGRESARSE")

        return departamento