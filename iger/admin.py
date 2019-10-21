# import json
# from django.contrib import admin
# from django.core.serializers.json import DjangoJSONEncoder
# from django.db.models import Count
# from django.db.models.functions import TruncDay
# from django.http import JsonResponse
# from django.urls import path
import json
from django.contrib import admin
from .models import Student
from .models import ListaDepartamento
from .models import Circle, CircleSummary
from .forms import ListaDepartamentoForm
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportMixin
from import_export.formats import base_formats
import adminactions.actions as actions
from django.db.models import Count, Sum, Min, Max, DateTimeField

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        import_id_fields = ['carnet']

class CircleResource(resources.ModelResource):
    class Meta:
        model = Circle
        import_id_fields = ['codigo_circulo']

class DptResource(resources.ModelResource):
    class Meta:
        model = ListaDepartamento
        import_id_fields = ['coordinacion']

class StudentAdmin(ImportExportModelAdmin, ExportMixin, admin.ModelAdmin):
    list_display = ('carnet', 'nombre_completo', 'grado', 'semestre', 'circulo', 'ingreso')
    list_filter = ('grado', 'semestre', 'circulo')
    def get_import_formats(self):
          
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

class CyD(ImportExportModelAdmin, ExportMixin,admin.ModelAdmin):
    list_display = ( 'coordinacion' , 'departamento', 'ingreso')
    form = ListaDepartamentoForm
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

    resource_class = DptResource

@admin.register(Circle)
class CircleCountAdmin(ImportExportModelAdmin, ExportMixin, admin.ModelAdmin):
    
    list_display = ('codigo_circulo', 'coordinacion', 'ingreso')

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

    resource_class = DptResource

#     def changelist_view(self, request, extra_context=None):
#         char_data = (
#             Circle.objects.values_list('codigo_circulo', 'ingreso')
#         )
#         as_json = json.dumps(list(char_data), cls=DjangoJSONEncoder)
#         extra_context = extra_context or {"char_data": as_json}
#         return super().changelist_view(request, extra_context = extra_context)

@admin.register(CircleSummary)
class CircleSummaryAdmin(admin.ModelAdmin):
        change_list_template = 'admin/iger/circlesummary/cs_change_list.html'
        def changelist_view(self, request, extra_context=None):
                response = super().changelist_view(
                request,
                extra_context=extra_context,
                )

                try:
                        qs = response.context_data['cl'].queryset
                except (AttributeError, KeyError):
                        return response

                metrics = {
                'total': Sum('ingreso'),
                'total_sales': Sum('ingreso'),
                }

                response.context_data['summary'] = list(
                qs
                .values('codigo_circulo')
                .annotate(**metrics)
                .order_by('-total')
                )

               
                

                
                return response
   

admin.site.register(Student, StudentAdmin)
admin.site.register(ListaDepartamento, CyD)
admin.site.add_action(actions.graph_queryset)