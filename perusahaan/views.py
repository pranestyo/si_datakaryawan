from __future__ import (absolute_import, division,
						print_function, unicode_literals)
from builtins import *

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.forms import ModelForm

from django.views.generic.edit import UpdateView

from io import BytesIO
from reportlab.pdfgen import canvas

from django.core.files.storage import FileSystemStorage


from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle 
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle 
from reportlab.lib.units import inch 
from reportlab.lib.pagesizes import A4, landscape, letter
from reportlab.lib import colors

from perusahaan.fusioncharts import FusionCharts

from perusahaan.models import *
from perusahaan.forms import PerusahaanForm, KaryawanForm, AktifForm, ResignForm, UploadFileForm
from perusahaan.handle_uploaded_file import handle_uploaded_file


# Create your views here.

@login_required(login_url=settings.LOGIN_PERUSAHAAN_URL)
def write_pdf_view(request):
	 # pengaturan respon berformat pdf 
	filename = "detail_karyawan"
	response = HttpResponse(content_type='application/pdf') 
	response['Content-Disposition'] = 'attachment; filename="' + filename + datetime.now().strftime("%Y%m%d%H%M%S") + '.pdf"'

	data = Karyawan.objects.filter(perusahaan__id=request.session['perusahaan_id'])
	table_data = []
	table_data.append(["Nama","No Identitas","Pendidikan Terakhir","Jurusan","Alamat","Jenis Kelamin","Email","Telepon","Gaji","Jabatan"])

	for x in data:
		table_data.append([x.nama_karyawan, x.no_identitas, x.pendidikan_terakhir, x.jurusan, x.alamat, x.jenis_kelamin, x.email, x.telepon, x.gaji, x.jabatan])

	 # membuat dokumen baru 
	doc = SimpleDocTemplate(response, pagesize=landscape(letter), rightMargin=300, leftMargin=300, topMargin=72, bottomMargin=18) 
	styles = getSampleStyleSheet()

	 # pengaturan tabel di pdf 
	table_style = TableStyle([ 
							   ('ALIGN',(0,0),(0,0),'RIGHT'), 
							   ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'), 
							   ('VALIGN',(0,0),(0,-1),'TOP'), 
							   ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black), 
							   ('BOX', (0,0), (-1,-1), 0.25, colors.black), 
						   ]) 
	detail_table = Table(table_data, colWidths=None) 
	detail_table.setStyle(table_style)

	 # mengisi pdf 
	content = [] 
	content.append(Paragraph('Detail Karyawan', styles['Title'])) 
	content.append(Spacer(1,12)) 
	content.append(Paragraph('Berikut ini adalah detail karyawan Anda:', styles['Normal'])) 
	content.append(Spacer(1,12)) 
	content.append(detail_table) 
	content.append(Spacer(1,36)) 
	content.append(Paragraph('Mengetahui, ', styles['Normal'])) 
	content.append(Spacer(1,48)) 
	content.append(Paragraph('Johan Pranestyo', styles['Normal'])) 

	 # menghasilkan pdf untk di download 
	doc.build(content) 
	return response


def mendaftar(request):
	if request.method == 'POST':
		form = PerusahaanForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/daftar_info/')

	else:
		form = PerusahaanForm()

	return render(request, 'index.html', {'form': form})

@login_required(login_url=settings.LOGIN_PERUSAHAAN_URL)
def tambah_aktif(request):
	if request.method == 'POST':
		form = AktifForm(request.POST, request.FILES)
		karyawan = request.POST['karyawan']
		k = Karyawan.objects.get(id=karyawan)

		if form.is_valid():
			handle_uploaded_file(request.FILES['file'])
			aktif = Aktif(
					perusahaan = Perusahaan.objects.get(id=request.session['perusahaan_id']),
					karyawan = get_object_or_404(Karyawan, id=k.id),
					mulai_bekerja = request.POST['mulai_bekerja'],
					foto = form.cleaned_data['foto'],
				)
			aktif.save()

			return HttpResponseRedirect('/aktif_info/')

	else:
		form = AktifForm()

	return render(request, 'tambah_karyawan_aktif.html', {'form':form})

@login_required(login_url=settings.LOGIN_PERUSAHAAN_URL)
def tambah_resign(request):
	if request.method == 'POST':
		form = ResignForm(request.POST, request.FILES)

		karyawan = request.POST['karyawan']
		s = Karyawan.objects.get(id=karyawan)

		if form.is_valid():
			resign = Resign(
					perusahaan = Perusahaan.objects.get(id=request.session['perusahaan_id']),
					karyawan = get_object_or_404(Karyawan, id=s.id),
					mulai_bekerja = request.POST['mulai_bekerja'],
					akhir_bekerja =request.POST['akhir_bekerja'],
					surat_keterangan = form.cleaned_data['surat_keterangan'],
				)
			resign.save()

			return HttpResponseRedirect('/resign_info/')

	else:
		form = ResignForm()

	return render(request, 'tambah_karyawan_resign.html', {'form':form})

@login_required(login_url=settings.LOGIN_PERUSAHAAN_URL)
def input_data_karyawan(request):
	if request.method == 'POST':
		form_data = request.POST
		form = KaryawanForm(form_data)

		provinsi = request.POST['provinsi']
		n = Provinsi.objects.get(id=provinsi)

		kabupatenkota = request.POST['kabupatenkota']
		k = KabupatenKota.objects.get(id=kabupatenkota)

		kecamatan = request.POST['kecamatan']
		c = Kecamatan.objects.get(id=kecamatan)

		if form.is_valid():
			tambah = Karyawan(
						perusahaan = Perusahaan.objects.get(id=request.session['perusahaan_id']),
						nama_karyawan = request.POST['nama_karyawan'],
						no_identitas = request.POST['no_identitas'],
						pendidikan_terakhir = request.POST['pendidikan_terakhir'],
						jurusan = request.POST['jurusan'],
						provinsi = get_object_or_404(Provinsi, id=n.id),
						kabupatenkota = get_object_or_404(KabupatenKota, id=k.id),
						kecamatan = get_object_or_404(Kecamatan, id=c.id),
						alamat = request.POST['alamat'],
						jenis_kelamin = request.POST['jenis_kelamin'],
						email = request.POST['email'],
						telepon = request.POST['telepon'],
						gaji = request.POST['gaji'],
						jabatan = request.POST['jabatan'],
						divisi = request.POST['divisi'],
						status_karyawan = request.POST['status_karyawan'],
				)
			tambah.save()

			return HttpResponseRedirect('/input_info/')
	else:
		form = KaryawanForm()

	return render(request, 'tambah_data_karyawan.html', {'form':form})

def login_perusahaan(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			if user.is_active:
				try:
					akun = AkunPerusahaan.objects.get(akun=user.id)
					login(request, user)

					request.session['perusahaan_id'] = akun.perusahaan.id
					request.session['perusahaan_email'] = akun.perusahaan.email
					request.session['username'] = request.POST['username']
				except:
					messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data Perusahaan.')
				return redirect('/')
			else:
				messages.add_message(request, messages.INFO, 'User belum terverifikasi.')
		else:
			messages.add_message(request, messages.INFO, 'Username atau password Anda salah.')

	return render(request,'login_perusahaan.html')

def logout_perusahaan_view(request):
	logout(request)

	return redirect('/login_perusahaan/')

def daftar_info(request):
	return render(request, 'daftar_info.html')

def login_home(request):
	return render(request, 'login_perusahaan.html')

@login_required(login_url=settings.LOGIN_PERUSAHAAN_URL)
def input_info(request):
	return render(request, 'input_info.html')

@login_required(login_url=settings.LOGIN_PERUSAHAAN_URL)
def aktif_info(request):
	return render(request, 'aktif_info.html')

@login_required(login_url=settings.LOGIN_PERUSAHAAN_URL)
def resign_info(request):
	return render(request, 'resign_info.html')

@login_required(login_url=settings.LOGIN_PERUSAHAAN_URL)
def detail_views(request):
	detail_karyawan = Karyawan.objects.filter(perusahaan__id=request.session['perusahaan_id'])

	paginator = Paginator(detail_karyawan, 3)
	page = request.GET.get('page')
	try:
		detail_karyawan = paginator.page(page)
	except PageNotAnInteger:
		detail_karyawan = paginator.page(1)
	except EmptyPage:
		detail_karyawan = paginator.page(paginator.num_pages)

	return render(request, 'detail_karyawan.html', {'detail_karyawan':detail_karyawan})

@login_required(login_url=settings.LOGIN_PERUSAHAAN_URL)
def aktif_views(request):
	karyawan_aktif = Aktif.objects.filter(perusahaan__id=request.session['perusahaan_id'])

	paginator = Paginator(karyawan_aktif, 3)
	page = request.GET.get('page')
	try:
		karyawan_aktif = paginator.page(page)
	except PageNotAnInteger:
		karyawan_aktif = paginator.page(1)
	except EmptyPage:
		karyawan_aktif = paginator.page(paginator.num_pages)

	return render(request, 'karyawan_aktif.html', {'karyawan_aktif':karyawan_aktif})

@login_required(login_url=settings.LOGIN_PERUSAHAAN_URL)
def resign_views(request):
	karyawan_resign = Resign.objects.filter(perusahaan__id=request.session['perusahaan_id'])

	paginator = Paginator(karyawan_resign, 3)
	page = request.GET.get('page')
	try:
		karyawan_resign = paginator.page(page)
	except PageNotAnInteger:
		karyawan_resign = paginator.page(1)
	except EmptyPage:
		karyawan_resign = paginator.page(paginator.num_pages)

	return render(request, 'karyawan_resign.html', {'karyawan_resign':karyawan_resign})

@login_required(login_url=settings.LOGIN_PERUSAHAAN_URL)
def cari(request):
	no_ktp = request.POST['ktp']
	cari_karyawan = Karyawan.objects.filter(no_identitas=no_ktp)

	paginator = Paginator(cari_karyawan, 3)
	page = request.GET.get('page')
	try:
		cari_karyawan = paginator.page(page)
	except PageNotAnInteger:
		cari_karyawan = paginator.page(1)
	except EmptyPage:
		cari_karyawan = paginator.page(paginator.num_pages)

	return render(request, 'hasil_cari.html', {'cari_karyawan':cari_karyawan})


def contoh(request):
	# Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
	dataSource = {}
	dataSource['chart'] = { 
		"caption": "Monthly revenue for last year",
			"subCaption": "Harry's SuperMart",
			"xAxisName": "Month",
			"yAxisName": "Revenues (In USD)",
			"numberPrefix": "$",
			"paletteColors": "#0075c2",
			"bgColor": "#ffffff",
			"borderAlpha": "0",
			"canvasBorderAlpha": "0",
			"usePlotGradientColor": "0",
			"plotBorderAlpha": "10",
			"placevaluesInside": "1",
			"rotatevalues": "1",
			"valueFontColor": "#ffffff",
			"showXAxisLine": "1",
			"xAxisLineColor": "#999999",
			"divlineColor": "#999999",
			"divLineIsDashed": "1",
			"showAlternateHGridColor": "0",
			"subcaptionFontBold": "0",
			"subcaptionFontSize": "14"
		}
   
	# The data for the chart should be in an array where each element of the array is a JSON object
	# having the `label` and `value` as key value pair.

	dataSource['data'] = []
	# Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
	for key in Karyawan.objects.all():
	  data = {}
	  data['label'] = key.pendidikan_terakhir
	  data['value'] = key.gaji
	  dataSource['data'].append(data)

	# Create an object for the Column 2D chart using the FusionCharts class constructor        	  		
	column2D = FusionCharts("column2D", "ex1" , "600", "350", "chart-1", "json", dataSource)
	return render(request, 'contoh.html', {'output': column2D.render()})

@login_required(login_url=settings.LOGIN_PERUSAHAAN_URL)
def grafik(request):
	jumlah_karyawan = Karyawan.objects.filter(perusahaan__id=request.session['perusahaan_id']).count()
	jumlah_aktif = Aktif.objects.filter(perusahaan__id=request.session['perusahaan_id']).count()
	jumlah_resign = Resign.objects.filter(perusahaan__id=request.session['perusahaan_id']).count()
	jumlah_sma = Karyawan.objects.filter(perusahaan__id=request.session['perusahaan_id'], pendidikan_terakhir='sma_smk').count()
	jumlah_d1 = Karyawan.objects.filter(perusahaan__id=request.session['perusahaan_id'], pendidikan_terakhir='d1').count()
	jumlah_d2 = Karyawan.objects.filter(perusahaan__id=request.session['perusahaan_id'], pendidikan_terakhir='d2').count()
	jumlah_d3 = Karyawan.objects.filter(perusahaan__id=request.session['perusahaan_id'], pendidikan_terakhir='d3').count()
	jumlah_s1 = Karyawan.objects.filter(perusahaan__id=request.session['perusahaan_id'], pendidikan_terakhir='s1').count()
	jumlah_s2 = Karyawan.objects.filter(perusahaan__id=request.session['perusahaan_id'], pendidikan_terakhir='s2').count()
	jumlah_s3 = Karyawan.objects.filter(perusahaan__id=request.session['perusahaan_id'], pendidikan_terakhir='s3').count()

	# Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
	dataSource = {}
	dataSource['chart'] = { 
		"caption": "Keadaan Karyawan",
			"subCaption": "Berdasarkan Tingkat Gaji",
			"xAxisName": "Nama Karyawan",
			"yAxisName": "Gaji (In IDR)",
			"numberPrefix": "Rp",
			"paletteColors": "#0075c2",
			"bgColor": "#ffffff",
			"borderAlpha": "0",
			"canvasBorderAlpha": "0",
			"usePlotGradientColor": "0",
			"plotBorderAlpha": "10",
			"placevaluesInside": "1",
			"rotatevalues": "1",
			"valueFontColor": "#ffffff",
			"showXAxisLine": "1",
			"xAxisLineColor": "#999999",
			"divlineColor": "#999999",
			"divLineIsDashed": "1",
			"showAlternateHGridColor": "0",
			"subcaptionFontBold": "0",
			"subcaptionFontSize": "14"
		}
   
	# The data for the chart should be in an array where each element of the array is a JSON object
	# having the `label` and `value` as key value pair.

	dataSource['data'] = []
	# Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
	for key in Karyawan.objects.filter(perusahaan__id=request.session['perusahaan_id']):
	  data = {}
	  data['label'] = key.nama_karyawan
	  data['value'] = key.gaji
	  dataSource['data'].append(data)

	# Create an object for the Column 2D chart using the FusionCharts class constructor        	  		
	column2D = FusionCharts("column2D", "ex1" , "600", "350", "chart-1", "json", dataSource)
	contex1 = {'jumlah_karyawan':jumlah_karyawan, 'jumlah_aktif':jumlah_aktif, 'jumlah_resign':jumlah_resign,'jumlah_sma':jumlah_sma,'jumlah_d1':jumlah_d1,'jumlah_d2':jumlah_d2,'jumlah_d3':jumlah_d3,'jumlah_s1':jumlah_s1,'jumlah_s2':jumlah_s2,'jumlah_s3':jumlah_s3, 'output': column2D.render()}
	return render(request, 'dashboard_perusahaan.html', contex1)

@login_required(login_url=settings.LOGIN_PERUSAHAAN_URL)
def karyawan_update(request, id):
    karyawan = get_object_or_404(Karyawan, pk=id)
    form = KaryawanForm(request.POST or None, instance=karyawan)
    if form.is_valid():
        form.save()
        return redirect('/dashboard_perusahaan/')
    return render(request, 'karyawan_update_form.html', {'form':form})

class ServerForm(ModelForm):
    class Meta:
        model = Karyawan
        fields = ['nama_karyawan', 'no_identitas', 'pendidikan_terakhir', 'jurusan','provinsi','kabupatenkota','kecamatan','alamat','jenis_kelamin','email','telepon','gaji','jabatan','status_karyawan']

@login_required(login_url=settings.LOGIN_PERUSAHAAN_URL)
def server_list(request, template_name='karyawan_list.html'):
    servers = Karyawan.objects.filter(perusahaan__id=request.session['perusahaan_id'])
    data = {}
    data['object_list'] = servers
    return render(request, template_name, data)

@login_required(login_url=settings.LOGIN_PERUSAHAAN_URL)
def server_create(request, template_name='karyawan_form.html'):
    form = ServerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('server_list')
    return render(request, template_name, {'form':form})

@login_required(login_url=settings.LOGIN_PERUSAHAAN_URL)
def server_update(request, pk, template_name='karyawan_form.html'):
    server = get_object_or_404(Karyawan, pk=pk)
    form = ServerForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('server_list')
    return render(request, template_name, {'form':form})

@login_required(login_url=settings.LOGIN_PERUSAHAAN_URL)
def server_delete(request, pk, template_name='karyawan_confirm_delete.html'):
    server = get_object_or_404(Karyawan, pk=pk)    
    if request.method=='POST':
        server.delete()
        return redirect('server_list')
    return render(request, template_name, {'object':server})