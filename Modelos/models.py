from django.db import models
from datetime import date

# Create your models here.
class Meta(models.Model):
    descripcion = models.CharField(max_length = 500)
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nombre} {self.descripcion}"

class Tipo_usuario(models.Model):
    tipo = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return f"{self.tipo}"

class User(models.Model): #Herencia de el framework
    cedula = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    correo = models.EmailField(max_length = 100, null = True, blank = True)
    contrasena = models.CharField(max_length = 100)
    meta = models.ForeignKey(Meta, on_delete = models.DO_NOTHING)
    tipo_usuario = models.ForeignKey(Tipo_usuario, on_delete = models.DO_NOTHING)
    fecha_nacimiento = models.DateField()

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} {self.correo}"

    def calculateAge(self): 
        today = date.today() 
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

class Formulario(models.Model):
    descripcion = models.CharField(max_length = 500)
    tipo = models.CharField(max_length = 100)
    fecha = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return f"{self.tipo} {self.descripcion}"

class Permiso(models.Model):
    tipo =  models.CharField(max_length = 100)

    def __str__(self) -> str:
        return f"{self.tipo}"

class Tip(models.Model):
    descripcion = models.CharField(max_length = 500)

    def __str__(self) -> str:
        return f"{self.descripcion}"

class User_Formulario (models.Model):
    cedula = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    formulario = models.ForeignKey(Formulario, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.cedula} {self.formulario}"

class Compra(models.Model):
    info = models.CharField(max_length = 200)

    def __str__(self) -> str:
        return f"{self.info}"

class Plan(models.Model):
    info = models.CharField(max_length = 200)
    valor = models.IntegerField()
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.nombre} {self.valor}"

class Plan_Compra(models.Model):
    compra = models.ForeignKey(Compra, on_delete = models.DO_NOTHING)
    plan = models.ForeignKey(Plan, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.plan} {self.compra}"

class Herramienta(models.Model):
    descripcion = models.CharField(max_length = 200)
    nombre = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.nombre}"

class Metodo_pago(models.Model):
    descripcion = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return f"{self.descripcion}"

class Compra_MetodoPago(models.Model):
    metodo_pago = models.ForeignKey(Metodo_pago, on_delete = models.DO_NOTHING)
    compra = models.ForeignKey(Compra, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.metodo_pago} {self.compra}"

class Herramienta_User(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    herramienta = models.ForeignKey(Herramienta, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.usuario} {self.herramienta}"

class User_Plan(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    plan = models.ForeignKey(Plan, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.usuario} {self.plan}"

class Factura(models.Model):
    fecha = models.DateTimeField(auto_now = True)
    info = models.CharField(max_length = 150)
    compra = models.ForeignKey(Compra, on_delete = models.DO_NOTHING)
    metodo_pago = models.ForeignKey(Metodo_pago, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.fecha} {self.compra} {self.info}"

class Encuesta(models.Model):
    descripcion = models.CharField(max_length=800)

    def __str__(self) -> str:
        return f"{self.descripcion}"

class User_Encuesta(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    encuesta = models.ForeignKey(Encuesta, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.usuario} {self.encuesta}"

class Tipo_usuario_permiso(models.Model):
    permiso = models.ForeignKey(Permiso, on_delete = models.DO_NOTHING)
    tipo_usuario = models.ForeignKey(Tipo_usuario, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.permiso} {self.tipo_usuario}"

class Avance(models.Model):
    descripcion = models.CharField(max_length = 250)
    usuario = models.ForeignKey(User, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.usuario} {self.descripcion}"

class Usuarios_Tip(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    tip = models.ForeignKey(Tip, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.tip} {self.usuario}"








