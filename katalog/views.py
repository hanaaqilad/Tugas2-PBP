from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
        'name': 'Hana Devi Aqila',
        'student_id': '2106751556',
        'list_item': data_catalog_item,
    }

    return render(request, "katalog.html", context)