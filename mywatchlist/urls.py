from django.urls import path
from mywatchlist.views import show_mywatchlist
from mywatchlist.views import show_json, show_xml, show_html

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/', show_html, name='show_html')
]