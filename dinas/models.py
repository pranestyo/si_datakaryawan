from django.db import models
from django.contrib.auth.models import User

from django.utils.encoding import python_2_unicode_compatible
from perusahaan.models import KabupatenKota

# Create your models here.

@python_2_unicode_compatible
class AkunDinas(models.Model):
	akun = models.ForeignKey(User)
	kabupatenkota = models.ForeignKey(KabupatenKota)

	def __str__(self):
		return self.kabupatenkota.nama_kabupaten_kota
