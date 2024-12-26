from doktertaniapp.models import SaranCabai, Obat
from doktertaniapp.serializers import CabaiSerializer, ObatSerializer
from rest_framework import viewsets

class CabaiViewset(viewsets.ModelViewSet):
    queryset = SaranCabai.objects.all()
    serializer_class = CabaiSerializer

class ObatViewset(viewsets.ModelViewSet):
    queryset = Obat.objects.all()
    serializer_class = ObatSerializer