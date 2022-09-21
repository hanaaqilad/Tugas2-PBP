from django.shortcuts import render
from mywatchlist.models import MyWatchList

from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_movie_mywatchlist = MyWatchList.objects.all()
    context = {
        'name': 'Hana Devi Aqila',
        'student_id': '2106751556',
        'list_mywatchlist': data_movie_mywatchlist,
    }

    return render(request, "mywatchlist.html", context)

def show_html(request):
    data_movie_mywatchlist = MyWatchList.objects.all()
    context = {
        'name': 'Hana Devi Aqila',
        'student_id': '2106751556',
        'list_mywatchlist': data_movie_mywatchlist,
    }

    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

