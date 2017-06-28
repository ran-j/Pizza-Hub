#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User,Permission
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

def criaruser(request):
	if request.method == 'POST':
			username = request.POST.get('usuario')
			email = request.POST.get('email')
			password = request.POST.get('senha')
			
			
			user = User.objects.create_user(username, email, password)

			user.save()
			
			return render(request, 'cadastrarusu.html', {'reto': 'Usuário cadastrado'})
	
	return render(request, 'cadastrarusu.html')
		
def logina(request):
	if request.method == 'POST':
		username = request.POST.get('usuario')
		password = request.POST.get('senha')
		
		user = authenticate(username=username, password=password)
		
		if user is not None:
			
			if user.is_active:
				login(request,user)
				if  user.is_staff:
					return redirect('/funcionario')
				else:
					return redirect('/cliente')
	
			else:
				return render(request, 'login.html', {'reto': 'Usuário bloqueado'})
				
		else:
			return render(request, 'login.html', {'reto': 'Usuário não registrado'})
				
	return render(request, 'login.html')
		


def sair(request):
	logout(request)
	return redirect(reverse('home'))


   
   
 
