from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date
from django.forms import widgets

from perusahaan.models import *

class PerusahaanForm(ModelForm):
	class Meta:
		model = Perusahaan
		fields = ['nama_perusahaan', 'email', 'provinsi', 'kabupatenkota','kecamatan','telepon','produk_utama','tenaga_kerja','alamat']
		labels = {
			'perusahaan':"Nama Perusahaan",
			'email':"Email",
			'provinsi':"Provinsi",
			'kabupatenkota':"Kabupaten/Kota",
			'kecamatan':"Kecamatan",
			'telepon':"Telepon",
			'produk_utama':"Produk Utama",
			'tenaga_kerja':"Jumlah Tenaga Kerja",
			'alamat':"Alamat Perusahaan",
		}

		error_messages = {
			'perusahaan': {
				'required':"Nama Perusahaan Harus Diisi"
			},
			'email': {
				'required':"Email Harus Diisi"
			},
			'provinsi': {
				'required':"Provinsi Harus Diisi"
			},
			'kabupatenkota': {
				'required':"Kabupaten atau Kota Harus Diisi"
			},
			'kecamatan': {
				'required':"Kecamatan Harus Diisi"
			},
			'telepon': {
				'required':"Telepon Harus Diisi"
			},
			'produk_utama': {
				'required':"Produk Utama Harus Diisi"
			},
			'tenaga_kerja': {
				'required':"Tenaga Kerja Harus Diisi"
			},
			'alamat': {
				'required':"Alamat Harus Diisi"
			}
		}

		widgets = {
			'alamat': forms.Textarea(attrs={'cols':50,'rows':10})
		}


class KaryawanForm(ModelForm):
	class Meta:
		model = Karyawan
		fields = ['nama_karyawan','no_identitas','pendidikan_terakhir',
				'jurusan','provinsi','kabupatenkota','kecamatan','alamat',
				'jenis_kelamin','email','telepon','gaji','jabatan','divisi','status_karyawan']
		labels = {
				'nama_karyawan':"Nama Karyawan",
				'no_identitas':"No. KTP",
				'pendidikan_terakhir':"Pendidikan Terakhir",
				'jurusan':"Jurusan",
				'provinsi':"Nama Provinsi",
				'kabupatenkota':"Nama Kabupaten/Kota",
				'kecamatan':"Nama Kecamatan",
				'alamat':"Alamat",
				'jenis_kelamin':"Jenis Kelamin",
				'email':"Email",
				'telepon':"Telepon",
				'gaji':"Gaji",
				'jabatan':"Jabatan",
				'divisi':"Divisi",
				'status_karyawan':"Status Karyawan",
		}
		error_messages = {
			'nama_karyawan': {
				'required':"Nama karyawan harus Anda isi !"
			},
			'no_identitas': {
				'required':"Nomor identitas harus Anda isi !"
			},
			'pendidikan_terakhir':{
				'required':"Pendidikan terakhir harus Anda isi !"
			},
			'jurusan':{
				'required':"Jurusan harus Anda isi"
			},
			'provinsi': {
				'required':"Provinsi Harus Anda isi"
			},
			'kabupatenkota': {
				'required':"Kabupaten atau Kota Harus Anda isi"
			},
			'kecamatan': {
				'required':"Kecamatan Harus Anda isi"
			},
			'alamat':{
				'required':"Alamat harus Anda isi"
			},
			'jenis_kelamin':{
				'required':"Jenis kelamin harus Anda isi"
			},
			'email':{
				'required':"Email harus Anda isi"
			},
			'telepon':{
				'required':"Telepon harus Anda isi"
			},
			'gaji':{
				'required':"Gaji harus Anda isi"
			},
			'jabatan':{
				'required':"Jabatan harus Anda isi"
			},
			'divisi':{
				'required':"Divisi harus Anda isi"
			},
			'status_karyawan':{
				'required':"Status karyawan harus Anda isi"
			}
		}

		widgets = {
			'alamat': forms.Textarea(attrs={'cols':50,'rows':10})
		}

class DateInput(forms.DateInput):
	input_type = 'date'

class AktifForm(ModelForm):
	class Meta:
		model = Aktif
		fields = ['karyawan','mulai_bekerja','foto']
		labels = {
				'karyawan':"Nama Karyawan",
				'mulai_bekerja':"Mulai Bekerja",
				'foto':"Foto",
		}
		error_messages = {
			'karyawan':{
				'required':"Nama karyawan harus diisi"
			},
			'mulai_bekerja':{
				'required':"Harap isi tanggal mulai bekerja"
			}
		}
		widgets = {
			'mulai_bekerja': DateInput()
		}

class ResignForm(ModelForm):
	class Meta:
		model = Resign
		fields = ['karyawan','mulai_bekerja','akhir_bekerja','surat_keterangan']
		labels = {
				'karyawan':"Nama Karyawan",
				'mulai_bekerja':"Mulai Bekerja",
				'akhir_bekerja':"Akhir Bekerja",
				'surat_keterangan':"Surat Keterangan",
		}
		error_messages = {
			'karyawan':{
				'required':"Nama karyawan harus diisi"
			},
			'mulai_bekerja':{
				'required':"Harap isi mulai bekerja"
			},
			'akhir_bekerja':{
				'required':"Harap isi akhir bekerja"
			}
		}
		widgets = {
			'akhir_bekerja': DateInput(),
			'mulai_bekerja': DateInput()
		}


class CreateUserForm(forms.Form):        
    required_css_class = 'required'        
    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                label="Username",
                                error_messages={'invalid': "This value may contain only letters, numbers and @/./+/-/_ characters."})
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(widget=forms.PasswordInput,
                                label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label="Repassword")

    def clean_username(self):            
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError("A user with that username already exists.")
        else:
            return self.cleaned_data['username']

    def clean_email(self):
        #if you want unique email address. else delete this function
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError("This email address is already in use. Please supply a different email address.")
        return self.cleaned_data['email']

    def clean(self):            
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("The two password fields didn't match.")
        return self.cleaned_data

class UploadFileForm(forms.Form): 
	title = forms.CharField(max_length=50) 
	file = forms.FileField()
