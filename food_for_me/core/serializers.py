from rest_framework import serializers
from .models import Propaganda
import core.models as models

class PropagandaSerializer(serializers.ModelSerializer):
	class Meta:
		model=models.Propaganda
		fields=('id','nombre_producto','pyme','descripcion')

class PymeSerializer(serializers.ModelSerializer):
	class Meta:
		model=models.Pyme
		fields=('id','nombre','sitio_web','telefono','correo')
