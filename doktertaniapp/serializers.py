from doktertaniapp.models import SaranCabai, Obat
from rest_framework import serializers

class CabaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaranCabai
        fields = ['id','penyakit', 'gejala_umum', 'saran', 'obat']

class ObatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obat
        fields = ['id', 'obat', 'diskripsi', 'harga']