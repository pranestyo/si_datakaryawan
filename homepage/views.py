from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django import forms

from perusahaan.models import *
from dinas.models import AkunDinas
from perusahaan.forms import CreateUserForm
from django.contrib.auth.models import User

# Create your views here.


def create_inactive_user(request):
    if request.method=='POST':
        frm=CreateUserForm(request.POST)
        if frm.is_valid():
            username, email, password = frm.cleaned_data['username'], frm.cleaned_data['email'], frm.cleaned_data['password1']
            new_user = User.objects.create_user(username, email, password)
            new_user.is_active = True # if you want to set active
            new_user.save()

            return HttpResponseRedirect('/akun_info/')

        else:
        	messages.add_message(request, messages.INFO,'Semua kolom harus diisi dengan benar.')

    else:
        frm=CreateUserForm()

    return render(request,'akun_perusahaan.html',{'form':frm})

def akun_info(request):
	return render(request, 'akun_info.html')

def login_dinas(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                try:
                    akun = AkunDinas.objects.get(akun=user.id)
                    login(request, user)

                    request.session['kabupaten_id'] = akun.kabupatenkota.id
                    request.session['username'] = request.POST['username']

                except:
                    messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data Kabupaten/Kota.')
                return redirect('/dashboard_dinas/')
            else:
                messages.add_message(request, messages.INFO, 'User belum terverifikasi.')
        else:
            messages.add_message(request, messages.INFO, 'Username atau password Anda salah.')

    return render(request,'login_dinas.html')

def logout_dinas(request):
    logout(request)

    return redirect('/login_dinas/')