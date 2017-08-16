from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

import os
from datetime import date


# Create your models here.

@python_2_unicode_compatible
class Provinsi(models.Model):
	nama_provinsi = models.CharField(max_length=50)

	def __str__(self):
		return self.nama_provinsi

@python_2_unicode_compatible
class KabupatenKota(models.Model):
	nama_kabupaten_kota = models.CharField(max_length=50)
	provinsi = models.ForeignKey(Provinsi)

	def __str__(self):
		return self.nama_kabupaten_kota

@python_2_unicode_compatible
class Kecamatan(models.Model):
	nama_kecamatan = models.CharField(max_length=50)
	kabupatenkota = models.ForeignKey(KabupatenKota)

	def __str__(self):
		return self.nama_kecamatan

@python_2_unicode_compatible
class Perusahaan(models.Model):
	nama_perusahaan = models.CharField(max_length=50)
	email = models.CharField(max_length=40)
	provinsi = models.ForeignKey(Provinsi)
	kabupatenkota = models.ForeignKey(KabupatenKota)
	kecamatan = models.ForeignKey(Kecamatan)
	alamat = models.TextField(max_length=200, blank=False)
	telepon = models.CharField(max_length=15)
	produk_utama = models.CharField(max_length=50)
	tenaga_kerja = models.IntegerField()
	diterima = models.BooleanField(default=False)

	def __str__(self):
		return self.nama_perusahaan

@python_2_unicode_compatible
class Karyawan(models.Model):
	PENDIDIKAN_TERAKHIR_CHOICES = (
		('sma_smk','SMA/SMK'),
		('d1','D1'),
		('d2','D2'),
		('d3','D3'),
		('s1','S1'),
		('s2','S2'),
		('s3','S3'),
		)
	JENIS_KELAMIN_CHOICES = (
		('pria','Pria'),
		('wanita', 'Wanita'),
		)

	perusahaan = models.ForeignKey(Perusahaan)
	nama_karyawan = models.CharField(max_length=50)
	no_identitas = models.IntegerField()
	pendidikan_terakhir = models.CharField(max_length=50, choices=PENDIDIKAN_TERAKHIR_CHOICES)
	jurusan = models.CharField(max_length=50)
	provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE)
	kabupatenkota = models.ForeignKey(KabupatenKota, on_delete=models.CASCADE)
	kecamatan = models.ForeignKey(Kecamatan, on_delete=models.CASCADE)
	alamat = models.TextField(max_length=200, blank=False)
	jenis_kelamin = models.CharField(max_length=20, choices=JENIS_KELAMIN_CHOICES)
	email = models.CharField(max_length=40)
	telepon = models.CharField(max_length=15)
	gaji = models.IntegerField()
	jabatan = models.CharField(max_length=50)
	divisi = models.CharField(max_length=50)
	status_karyawan = models.CharField(max_length=20)

	def __str__(self):
		return self.nama_karyawan

	def get_absolut_url(self):
		return reverse('karyawan_edit', kwargs={'pk': self.pk})

@python_2_unicode_compatible
class Aktif(models.Model):
	perusahaan = models.ForeignKey(Perusahaan)
	karyawan = models.ForeignKey(Karyawan)
	mulai_bekerja = models.DateField()
	foto = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT,"image_upload"), blank=True)


class Resign(models.Model):
	perusahaan = models.ForeignKey(Perusahaan)
	karyawan = models.ForeignKey(Karyawan)
	mulai_bekerja = models.DateField()
	akhir_bekerja = models.DateField()
	surat_keterangan = models.FileField(upload_to=os.path.join(settings.MEDIA_ROOT,"file_upload"), blank=True)

@python_2_unicode_compatible
class AkunPerusahaan(models.Model):
	akun = models.ForeignKey(User)
	perusahaan = models.ForeignKey(Perusahaan)

	def __str__(self):
		return self.perusahaan.nama_perusahaan

class Revenue(models.Model):
	MonthlyRevenue = models.CharField(max_length=50)
	Month = models.CharField(max_length=50)

	def __str__(self):
		return u'%s %s' % (self.MonthlyRevenue, self.Month)