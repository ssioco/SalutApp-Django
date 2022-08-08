from django.contrib import admin
from .models import Meta, Tipo_usuario, User, Formulario, Permiso, Tip, User_Formulario, Compra, Plan, Plan_Compra, Herramienta, Metodo_pago, Compra_MetodoPago, Herramienta_User, User_Plan, Factura, Encuesta, User_Encuesta, Tipo_usuario_permiso, Avance, Usuarios_Tip
# Register your models here.

@admin.register(Meta)
class MetaAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion', 'nombre', )
    search_fields = ['nombre','id',]

@admin.register(Tipo_usuario)
class Tipo_usuarioAdmin(admin.ModelAdmin):
    list_display = ('tipo', )
    search_fields = ['tipo']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'correo', 'contrasena', 'meta', 'tipo_usuario', 'fecha_nacimiento', 'calculateAge' )
    search_fields = ['cedula', 'correo',]

@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'tipo', 'fecha', )
    search_fields = ['fecha',]

@admin.register(Permiso)
class PermisoAdmin(admin.ModelAdmin):
    list_display = ('tipo', )
    search_fields = ['tipo',]

@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    list_display = ('descripcion', )

@admin.register(User_Formulario)
class User_FormularioAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'formulario', )
    search_fields = [str]

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('info',)

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('info', 'valor', 'nombre', )
    search_fields = ['nombre',]

@admin.register(Plan_Compra)
class Plan_CompraAdmin(admin.ModelAdmin):
    list_display = ('compra', 'plan', )
    search_fields = ['compra', 'plan']

@admin.register(Herramienta)
class HerramientAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'nombre', )
    search_fields = ['nombre',]

@admin.register(Metodo_pago)
class Metodo_pagoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)
    
@admin.register(Compra_MetodoPago)
class Compra_MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('metodo_pago', 'compra', )
    search_fields = ['metodo_pago', 'compra', ]

@admin.register(Herramienta_User)
class Herramienta_UserAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'herramienta', )
    search_fields = ['usuario', 'herramienta',]

@admin.register(User_Plan)
class User_PlanAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'plan', )
    search_fields = ['usuario', 'plan', ]

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'info', 'compra', 'metodo_pago', )
    search_fields = ['fecha', 'compra',]

@admin.register(Encuesta)
class EncuestaAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

@admin.register(User_Encuesta)
class User_EncuestaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'encuesta', )
    search_fields = ['usuario',]

@admin.register(Tipo_usuario_permiso)
class Tipo_usuario_permisoAdmin(admin.ModelAdmin):
    list_display = ('permiso', 'tipo_usuario', )
    search_fields = ['permiso', 'tipo_usuario',]

@admin.register(Avance)
class AvanceAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'usuario', )
    search_fields = ['usuario',]

@admin.register(Usuarios_Tip)
class Usuarios_TipAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tip', )
    search_fields = ['usuario']
















