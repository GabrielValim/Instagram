from django.shortcuts import render, redirect
from services.instagram_scraper import scrape_instagram_data
from services.browser import browser

def login(request):
    return render(request, 'galeria/login.html')

def inicio(request):
    return render(request, 'galeria/inicio.html')

def seguranca(request):
    return render(request, 'galeria/seguranca.html')




def inicio_view(request):
    if request.method == 'POST':
        # Obter as credenciais do formulário
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Chamar a função de raspagem de dados
        instagram_data = scrape_instagram_data(username, password)

        # Redirecionar o usuário para a dashboard
        return redirect('grafico', instagram_data=instagram_data)
    else:
        return render(request, 'galeria/inicio.html')




    

