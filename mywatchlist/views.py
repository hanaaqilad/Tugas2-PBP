from django.shortcuts import render
from mywatchlist.models import MyWatchList

from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_movie_mywatchlist = MyWatchList.objects.all()

    # referensi code : https://linuxtut.com/en/367599a00bcd709de512/ 
    movie_list = list(data_movie_mywatchlist.values())

    count_belum = 0
    count_sudah = 0
    res_watched = ""

    for movie in movie_list:
        if movie['watched'] == 'Sudah':
            count_sudah += 1
        elif movie['watched'] == "Belum":
            count_belum += 1

    if count_sudah >= count_belum:
        res_watched = "Selamat, kamu sudah banyak menonton!"
    else:
        res_watched = "Wah, kamu masih sedikit menonton!"

    context = {
        'name': 'Hana Devi Aqila',
        'student_id': '2106751556',
        'list_mywatchlist': data_movie_mywatchlist,
        'bonus_watched': res_watched,
    }
    
    return render(request, "mywatchlist.html", context)

def show_html(request):
    data_movie_mywatchlist = MyWatchList.objects.all()

    # referensi code : https://linuxtut.com/en/367599a00bcd709de512/ 
    movie_list = list(data_movie_mywatchlist.values())

    count_belum = 0
    count_sudah = 0
    res_watched = ""

    for movie in movie_list:
        if movie['watched'] == 'Sudah':
            count_sudah += 1
        elif movie['watched'] == "Belum":
            count_belum += 1

    if count_sudah >= count_belum:
        res_watched = "Selamat, kamu sudah banyak menonton!"
    else:
        res_watched = "Wah, kamu masih sedikit menonton!"

    context = {
        'name': 'Hana Devi Aqila',
        'student_id': '2106751556',
        'list_mywatchlist': data_movie_mywatchlist,
        'bonus_watched': res_watched,
    }
    
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

