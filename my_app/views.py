from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

from . import models

from requests.compat import quote_plus 

BASE_CRAIGSLIST_URL="https://delhi.craigslist.org/search/bbb?query={}"
# Create your views here.
def home(request):
     return render(request,'base.html ')
 
def new_search(request):
    search=request.POST.get('search')
    models.Search.objects.create(search=search)

    #print(quote_plus(search))
    final_url=BASE_CRAIGSLIST_URL.format(quote_plus(search))
    #print(final_url)
    response=requests.get(final_url)
    data=response.text

    soup=BeautifulSoup(data,features='html.parser')
    post_listings=soup.find_all('li',{'class':'result-row'})
    

    final_posting=[]
    for post in post_listings:
         post_title=post.find(class_="result-title").text
         post_url=post.find('a').get('href')

         final_posting.append((post_title,post_url))


    
    stuff_for_frontend={
         'search':search,
         'final_postings':final_posting,

         }
    return render(request,'my_app/new_search.html',stuff_for_frontend )