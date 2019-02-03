from django.db import models


class Obat(models.Model):
    kode_obat = models.CharField(max_length=5)
    nama_obat = models.CharField(max_length=30)
    jenis_obat = models.CharField(max_length=15)
    kategori = models.CharField(max_length=50)
    harga_obat = models.IntegerField()
    jumlah_obat = models.IntegerField()

class Pembayaran(models.Model):
    nomor_bayar = models.CharField(max_length=6)
    kode_pasien = models.CharField(max_length=6, primary_key='true')
    tanggal_bayar = models.DateField(auto_now_add=True)
    jumlah_bayar = models.IntegerField

class Pasien(models.Model):
    kode_pasien = models.CharField(max_length=6, primary_key='true')
    nama_pasien = models.CharField(max_length=30)
    alamat_pasien = models.CharField(max_length=100)
    gender = models.BooleanField(max_length=2)
    umur = models.CharField(max_length=2)
    telepon = models.CharField(max_length=12)

class Polklinik(models.Model):
    kode_plk = models.CharField(max_length=2)
    nama_plk = models.CharField(max_length=30)

class Dokter(models.Model):
    kode_dokter = models.CharField(max_length=1, primary_key='true')
    nama_dokter = models.CharField(max_length=30)
    spesialis = models.CharField(max_length=30)
    alamat = models.CharField(max_length=100)
    nomer = models.CharField(max_length=15)
    tarif = models.IntegerField

class Pendfataran(models.Model):
    no_pendaftaran = models.CharField(max_length=1)
    tanggal_pendaftaran = models.CharField(max_length=30)
    kode_dokter = models.CharField(max_length=1, primary_key='true')
    kode_pasien = models.CharField(max_length=100)
    kode_polklinik = models.CharField(max_length=15)
    biaya = models.IntegerField
    ket = models.TextField


class Detail(models.Model):
    no_resep = models.CharField(max_length=2)
    kode_obat = models.CharField(max_length=3)
    harga = models.IntegerField
    dosis = models.CharField(max_length=30)
    total = models.IntegerField

class Resep(models.Model):
    nomer_resep = models.CharField(max_length=4)
    tanggal_resep = models.DateField
    kode_dokter = models.CharField(max_length=1)
    kode_pasien = models.CharField(max_length=5)
    kode_plk = models.CharField(max_length=2)
    total_harga = models.IntegerField
    bayar = models.IntegerField
    kembali = models.IntegerField


