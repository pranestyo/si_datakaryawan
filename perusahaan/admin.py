from django.contrib import admin

from perusahaan.models import *

# Register your models here.
class ProvinsiAdmin(admin.ModelAdmin):
	list_display = ['nama_provinsi']
	list_filter = ()
	search_fields = ['nama_provinsi']
	list_per_page = 25

admin.site.register(Provinsi, ProvinsiAdmin)

class KabupatenKotaAdmin(admin.ModelAdmin):
	list_display = ['nama_kabupaten_kota','provinsi']
	list_filter = ('provinsi',)
	search_fields = ['nama_kabupaten_kota']
	list_per_page = 25

admin.site.register(KabupatenKota, KabupatenKotaAdmin)

class KecamatanAdmin(admin.ModelAdmin):
	list_display = ['nama_kecamatan','kabupatenkota']
	list_filter = ('kabupatenkota',)
	search_fields = ['nama_kecamatan']
	list_per_page = 25

admin.site.register(Kecamatan, KecamatanAdmin)

class PerusahaanAdmin(admin.ModelAdmin):
	list_display = ['nama_perusahaan','email','provinsi','kabupatenkota','kecamatan','alamat','telepon','produk_utama','tenaga_kerja','diterima']
	list_filter = ('provinsi','kabupatenkota','kecamatan',)
	search_fields = ['nama_perusahaan']
	list_per_page = 25

	actions = ['terima_daftar','tolak_daftar']

	def terima_daftar(self,request,queryset):
		queryset.update(diterima=True)

	terima_daftar.short_description = "Terima Pendaftaran Perusahaan"

	def tolak_daftar(self,request,queryset):
		queryset.update(diterima=False)

	tolak_daftar.short_description = "Tolak Pendaftaran Perusahaan"

admin.site.register(Perusahaan, PerusahaanAdmin)

class AkunPerusahaanAdmin(admin.ModelAdmin):
	list_display = ['akun','perusahaan']
	list_filter = ('perusahaan',)
	search_fields = ['perusahaan']
	list_per_page = 15

admin.site.register(AkunPerusahaan, AkunPerusahaanAdmin)

class KaryawanAdmin(admin.ModelAdmin):
	list_display = ['perusahaan','nama_karyawan','no_identitas','pendidikan_terakhir','jurusan','provinsi','kabupatenkota','kecamatan','alamat','jenis_kelamin','email','telepon','gaji','jabatan','divisi','status_karyawan']
	list_filter = ('perusahaan','provinsi','kabupatenkota')
	search_fields = ['perusahaan']
	list_per_page = 25

admin.site.register(Karyawan, KaryawanAdmin)

class AktifAdmin(admin.ModelAdmin):
	list_display = ['perusahaan','karyawan','mulai_bekerja','foto']
	list_filter = ('karyawan',)
	search_fields = ['karyawan']
	list_per_page = 25

admin.site.register(Aktif, AktifAdmin)


admin.site.register(Revenue)