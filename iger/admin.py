from django.contrib import admin
from .models import Student
from .models import ListaDepartamento
from .models import Circle
from .forms import ListaDepartamentoForm
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportMixin
from import_export.formats import base_formats
import adminactions.actions as actions

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        import_id_fields = ['carnet']

class StudentAdmin(ImportExportModelAdmin, ExportMixin, admin.ModelAdmin):
    list_display = ('carnet', 'nombre_completo', 'grado', 'semestre', 'circulo')
    list_filter = ('grado', 'semestre', 'circulo')
    def get_import_formats(self):
            """
            Returns available export formats.
            """
            formats = (
                  base_formats.CSV,
                  base_formats.XLS,
                  base_formats.XLSX,
                  base_formats.JSON,
            )
            return [f for f in formats if f().can_export()]
    def get_export_formats(self):
            """
            Returns available export formats.
            """
            formats = (
                  base_formats.CSV,
                  base_formats.XLSX,
            )
            return [f for f in formats if f().can_export()]

    resource_class = StudentResource

class CyD(admin.ModelAdmin):
    list_display = ('departamento', 'coordinacion')
    form = ListaDepartamentoForm

class Prueba(admin.ModelAdmin):
    list_display = ('codigo_circulo', 'coordinacion')

admin.site.register(Student, StudentAdmin)
admin.site.register(ListaDepartamento, CyD)
admin.site.register(Circle, Prueba)
admin.site.add_action(actions.graph_queryset)
