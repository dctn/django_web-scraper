from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from .forms import UrlForms
# Create your views here.
def index(request):
    form = UrlForms()
    link_address = []
    if request.method == 'POST':
        form = UrlForms(request.POST)
        if form.is_valid():
            site = form.cleaned_data['url']
            page = requests.get(site)
            soup = BeautifulSoup(page.text,'html.parser')

            link = soup.find_all('a')
            link_address = []
            for i in link:
                link_address.append(i.get('href'))

    else:
        form = UrlForms() 
        link_address = []       
    context = {
        "data":link_address,
        "form":form,
    }
    return render(request,'index.html',context)