# prediction/models.py

from django.db import models

class SaranCabai(models.Model):
    penyakit = models.CharField(max_length=100)
    gejala_umum = models.TextField()
    saran = models.TextField()
    obat = models.TextField()

    def __str__(self):
        return self.penyakit
    
class Obat(models.Model):
    obat = models.CharField(max_length=100)
    diskripsi = models.TextField()
    harga = models.TextField()

    def __str__(self):
        return self.penyakit

