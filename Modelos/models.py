from django.db import models

# Create your models here.
class Meta(models.Model):
    descripcion = models.CharField(max_length = 500)

class Tipo_usuario(models.Model):
    Tipo = models.CharField(max_length = 100)

class User(models.Model): #Herencia de el framework
    cedula = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    correo = models.EmailField(max_length = 100, null = True, blank = True)
    contrasena = models.CharField(max_length = 100)
    meta = models.ForeignKey(Meta, on_delete = models.DO_NOTHING)
    tipo_usuario = models.ForeignKey(Tipo_usuario, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Formulario(models.Model):
    descripcion = models.CharField(max_length = 500)
    tipo = models.CharField(max_length = 100)
    fecha = models.DateTimeField(auto_now = True)

class Permiso(models.Model):
    tipo =  models.CharField(max_length = 100)

class Tip(models.Model):
    descripcion = models.CharField(max_length = 500)

class User_Formulario (models.Model):
    cedula = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    formulario = models.ForeignKey(Formulario, on_delete = models.DO_NOTHING)

class Compra(models.Model):
    info = models.CharField(max_length = 200)

class Plan(models.Model):
    info = models.CharField(max_length = 200)
    valor = models.IntegerField()

class Plan_Compra(models.Model):
    compra = models.ForeignKey(Compra, on_delete = models.DO_NOTHING)
    plan = models.ForeignKey(Plan, on_delete = models.DO_NOTHING)

class Herramienta(models.Model):
    descripcion = models.CharField(max_length = 200)

class Metodo_pago(models.Model):
    descripcion = models.CharField(max_length = 100)

class Compra_MetodoPago(models.Model):
    metodo_pago = models.ForeignKey(Metodo_pago, on_delete = models.DO_NOTHING)
    compra = models.ForeignKey(Compra, on_delete = models.DO_NOTHING)

class Herramienta_User(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    herramienta = models.ForeignKey(Herramienta, on_delete = models.DO_NOTHING)

class User_Plan(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    plan = models.ForeignKey(Plan, on_delete = models.DO_NOTHING)

class Factura(models.Model):
    fecha = models.DateTimeField(auto_now = True)
    info = models.CharField(max_length = 150)
    compra = models.ForeignKey(Compra, on_delete = models.DO_NOTHING)
    metodo_pago = models.ForeignKey(Metodo_pago, on_delete = models.DO_NOTHING)

class Encuesta(models.Model):
    descripcion = models.CharField(max_length=800)

class User_Encuesta(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    encuesta = models.ForeignKey(Encuesta, on_delete = models.DO_NOTHING)

class Tipo_usuario_permiso(models.Model):
    permiso = models.ForeignKey(Permiso, on_delete = models.DO_NOTHING)
    tipo_usuario = models.ForeignKey(Tipo_usuario, on_delete = models.DO_NOTHING)

class Avance(models.Model):
    descripcion = models.CharField(max_length = 250)
    usuario = models.ForeignKey(User, on_delete = models.DO_NOTHING)

class Usuarios_Tip(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    tip = models.ForeignKey(Tip, on_delete = models.DO_NOTHING)








