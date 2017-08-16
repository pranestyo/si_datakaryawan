"""si_dk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

#from django.conf.urls.defaults import *
from wkhtmltopdf.views import PDFTemplateView

from homepage import views as homepage_views
from perusahaan import views as perusahaan_views
from dinas import views as dinas_views
from perusahaan import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', perusahaan_views.grafik),
    url(r'^login_dinas/', homepage_views.login_dinas),
    url(r'^logout_dinas/', homepage_views.logout_dinas),
    url(r'^login_perusahaan/', perusahaan_views.login_perusahaan),
    url(r'^logout_perusahaan/', perusahaan_views.logout_perusahaan_view),
    url(r'^mendaftar/', perusahaan_views.mendaftar),
    url(r'^input/', perusahaan_views.input_data_karyawan),
    url(r'^aktif/', perusahaan_views.tambah_aktif),
    url(r'^resign/', perusahaan_views.tambah_resign),
    url(r'^daftar/', homepage_views.create_inactive_user),
    url(r'^daftar_info/', perusahaan_views.daftar_info),
    url(r'^akun_info/', homepage_views.akun_info),
    url(r'^login_home/', perusahaan_views.login_home),
    url(r'^dashboard_perusahaan/', perusahaan_views.grafik),
    url(r'^input_info/', perusahaan_views.input_info),
    url(r'^aktif_info/', perusahaan_views.aktif_info),
    url(r'^resign_info/', perusahaan_views.resign_info),
    url(r'^detail_info/', perusahaan_views.detail_views),
    url(r'^karyawan_aktif/', perusahaan_views.aktif_views),
    url(r'^karyawan_resign/', perusahaan_views.resign_views),
    url(r'^cari_karyawan/', perusahaan_views.cari),
    url(r'^pdf/$', perusahaan_views.write_pdf_view),
    url(r'^contoh/', perusahaan_views.contoh),
    url(r'^dashboard_dinas/', dinas_views.dashboard_dinas),
    url(r'^update/', perusahaan_views.karyawan_update),
    url(r'^list/', views.server_list, name='server_list'),
    url(r'^new$', views.server_create, name='server_new'),
    url(r'^edit/(?P<pk>\d+)$', views.server_update, name='server_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.server_delete, name='server_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
