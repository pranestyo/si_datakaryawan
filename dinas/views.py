from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime

from perusahaan.fusioncharts import FusionCharts

from dinas.models import AkunDinas
from perusahaan.models import *

# Create your views here.
@login_required(login_url=settings.LOGIN_DINAS_URL)
def dashboard_dinas(request):
    pilih = KabupatenKota.objects.filter(id=request.session['kabupaten_id'])
    jumlah_karyawan = Karyawan.objects.filter(kabupatenkota__id=request.session['kabupaten_id']).count()
    jumlah_aktif = Aktif.objects.filter().count()
    jumlah_resign = Resign.objects.filter().count()
    jumlah_sma = Karyawan.objects.filter(kabupatenkota__id=request.session['kabupaten_id'], pendidikan_terakhir='sma_smk').count()
    jumlah_d1 = Karyawan.objects.filter(kabupatenkota__id=request.session['kabupaten_id'], pendidikan_terakhir='d1').count()
    jumlah_d2 = Karyawan.objects.filter(kabupatenkota__id=request.session['kabupaten_id'], pendidikan_terakhir='d2').count()
    jumlah_d3 = Karyawan.objects.filter(kabupatenkota__id=request.session['kabupaten_id'], pendidikan_terakhir='d3').count()
    jumlah_s1 = Karyawan.objects.filter(kabupatenkota__id=request.session['kabupaten_id'], pendidikan_terakhir='s1').count()
    jumlah_s2 = Karyawan.objects.filter(kabupatenkota__id=request.session['kabupaten_id'], pendidikan_terakhir='s2').count()
    jumlah_s3 = Karyawan.objects.filter(kabupatenkota__id=request.session['kabupaten_id'], pendidikan_terakhir='s3').count()


    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    dataSource = {}
    dataSource['chart'] = { 
        "caption": "Keadaan Karyawan",
            "subCaption": "Berdasarkan Tingkat Gaji",
            "xAxisName": "Tingkat Pendidikan",
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
    for key in Karyawan.objects.filter(kabupatenkota__id=request.session['kabupaten_id']):
      data = {}
      data['label'] = key.pendidikan_terakhir
      data['value'] = key.gaji
      dataSource['data'].append(data)

    # Create an object for the Column 2D chart using the FusionCharts class constructor                 
    column2D = FusionCharts("column2D", "ex1" , "600", "350", "chart-1", "json", dataSource)
    contex1 = {'jumlah_karyawan':jumlah_karyawan, 'jumlah_aktif':jumlah_aktif, 'jumlah_resign':jumlah_resign,'jumlah_sma':jumlah_sma,'jumlah_d1':jumlah_d1,'jumlah_d2':jumlah_d2,'jumlah_d3':jumlah_d3,'jumlah_s1':jumlah_s1,'jumlah_s2':jumlah_s2,'jumlah_s3':jumlah_s3, 'output': column2D.render()}
    return render(request, 'dashboard_dinas.html', contex1)