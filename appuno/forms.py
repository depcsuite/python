from django import forms

from appuno.models import Producto
class CrearProducto(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.FloatField()
    #CHOICES = (('s', 'Sí'), ('n','No'))
    #dispo = forms.ChoiceField(CHOICES)
class CrearProductoPro(forms.ModelForm):


    class Meta:
        model = Producto
        fields = ('__all__')
