**TUGAS 3 PBP**

**Hana Devi Aqila - 2106751556 - PBP-C**

1. Jelaskan perbedaan antara JSON, XML, dan HTML!
    JSON, XML, dan HTML adalah beberapa contoh dari format data dalam implementasi data delivery. JSON adalah JavaScript Object Notation, XML adalah eXtensible Markup Language, dan HTML adalah Hyper Text markup Language. Berikut adalah beberapa perbedaan di antara ketiganya:
    - Perbedaan yang paling jelas di antara ketiganya adalah ekstensi filenya. Ekstensi file tersebut sesuai dengan namanya masing-masing, yaitu .json pada file dengan fromat JSON, .xml pada file XML, dan .html pada file HTML. 
    - Dokumen XML bersifat self-descriptive sehingga data/informasi yang akan disampaikan sudah dapat dimengerti melalui kodenya. XML hanya memiliki data dan tidak mampu merepresentasikan datanya dengan baik. Kemudian, dokumen JSON bersifat self-describing sehingga mudah dimengerti dan dapat merepresentasikan datanya. Sementara itu, dokumen HTML biasanya berisi data dan representasi data untuk didisplay.
    - Format penulisan pada XML lebih terstruktur, yaitu dengan menulis variabel datanya di dalam tag pada kodenya. Sementara itu, format penulisan pada JSON berbentuk seperti dictionary, datanya disimpan berdasarkan key dan valuenya. Dan pada HTML, juga menggunakan tag di mana data yang ingin ditampilkan ditulis di antara 2 tag (opening tag and closing tag)
    - XML dan HTML menggunakan struktur tree, JSON tidak. 
    - XML dan JSON bersifat case sensitive. Sementara itu, secara umum HTML bersifat case insensitive karena pada proses parsingnya, semua elemen diubah menjadi lowercase terlebih dahulu. 
    - XML kurang support penggunaan array. Sementara JSON dan HTML support array.
    - XML harus memiliki root element, sementara JSON dan HTML tidak. 
    - XML merupakan independent data format yang support beragam encoding. JSON merupakan language-independent data-interchange format dan hanya support encoding UTF-8 saja. 

2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Data delivery adalah proses mengirimkan data dari satu stack ke stack lainnya dalam pengembangan suatu platform. Hal ini dilakukan agar kita dapat menampilkan data sesuai dengan yang direquest oleh client di platform yang kita buat. Format data delivery ini juga akan disesuaikan oleh request dari client, misal jika client request HTML page, maka proses data deliverynya akan me-return HTML file. Dengan data delivery, kita juga dapat menampilkan beberapa tipe file tanpa perlu menyimpannya di server sehingga dapat menghemat storage server. Contohnya adalah saat client hanya me-request data, returnnya akan XML atau JSON. File XML ini akan digenerate oleh program dan tidak disimpan dalam server.

3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    1. Membuat aplikasi baru bernama mywatchlist dengan cara mengeksekusi startapp di direktori Tugas2 di dalam virtual environment untuk membuat app baru pada Django. Syntaxnya berupa `python manage.py startapp mywatchlist`. Setelah itu, maka secara otomatis langsung terbuat folder baru bernama mywatchlist dengan isiannya berupa admin.py, apps.py, views.py, dll. 
    2. Membuat file urls.py di dalam folder mywatchlist, dengan isian sebagai berikut:
    ```shell
    from django.urls import path
    from mywatchlist.views import show_mywatchlist                  // agar dapat melakukan routing terhadap fungsi-fungsi yang ada pada views

    app_name = 'mywatchlist'        // nama aplikasinya

    urlpatterns = [
        path('', show_mywatchlist, name='show_mywatchlist'),        // menambahkan path agar bisa melakukan routing
    ]
    ```
    Untuk sementara, views.py nya berisi:
    ```shell
    from django.shortcuts import render
    from mywatchlist.models import MyWatchList

    def show_mywatchlist(request):
        data_movie_mywatchlist = MyWatchList.objects.all()
        context = {
            'name': 'Hana Devi Aqila',
            'student_id': '2106751556',
            'list_mywatchlist': data_movie_mywatchlist,
        }

        return render(request, "mywatchlist.html", context)
    ```
    Selain itu juga menambahkan:
    `path('mywatchlist/', include('mywatchlist.urls')),`
    sebagai elemen pada list urlpatterns di urls.py yang ada di folder project_django

    3. Membuat class MyWatchList dengan 5 atribut yang sesuai pada file models.py yang ada di folder mywatchlist. Setiap field dari atribut tersebut juga disesuaikan dengan tipe field yang sesuai. Misal, release_date menggunakan DateField(). Classnya adalah sebagai berikut:
    ```shell
    from django.db import models
    class MyWatchList(models.Model):
        watched = models.CharField(max_length=5)
        title = models.CharField(max_length=200)
        rating = models.IntegerField()
        release_date = models.DateField()
        review = models.TextField()
    ```
    
    4. Pada folder mywatchlist, membuat folder baru bernama fixtures dengan file initial_mywatchlist_data.json di dalamnya. Kemudian membuat sebuah list dengan 10 elemen yang berisi data-data yang diinginkan. Setiap elemen tersebut didefinisikan terlebih dahulu model dan pk nya. Selanjutnya membuat dictionary fields dengan key berupa atribut yang telah ditentukan pada models.py tadi dan valuenya berupa data yang ingin dipakai. Contoh dari elemennya adalah sebagai berikut:
    ```shell
     {
        "model": "mywatchlist.MyWatchList",
        "pk": 2,
        "fields": {
            "watched": "Sudah",
            "title": "Nanti Kita Cerita Tentang Hari Ini",
            "rating": 5,
            "release_date": "2022-09-21",
            "review": "Filmnya sedih, Auroranya kasian"
        }
     }
     ```

    5. Pada file views.py, menambahkan import agar dapat menampilkan response, yaitu: 
    ```shell
    from django.http import HttpResponse
    from django.core import serializers
    ```
    Membuat 3 fungsi yaitu:
    ```shell
    def show_xml(request):
        data = MyWatchList.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = MyWatchList.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    dan `show_html()` yang isinya sama dengan fungsi `show_mywatchlist()` (karena show_mywatchlist tampilannya berupa html).

    6. Kemudian pada urls.py di folder mywatchlist, menambahkan import berupa:
    `from mywatchlist.views import show_json, show_xml, show_html`

    dan elemen pada urlpatterns berupa:
    ```shell
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/', show_html, name='show_html')
    ```

    7. Deployment ke Heroku dilakukan dengan cara melakukan gti add, commit, push ke repository di github. Lalu membuat aplikasi baru di heroku dan membuat variabel secrets pada repository github. Kemudian di re-run agar aplikasinya berhasil terdeploy. 

**SS POSTMAN**

HTML 
<img width="1440" alt="Screen Shot 2022-09-21 at 23 30 18" src="https://user-images.githubusercontent.com/90792106/191560527-d70a6407-9396-4525-8bec-0f2feac39e54.png">

<img src="https://user-images.githubusercontent.com/90792106/191560527-d70a6407-9396-4525-8bec-0f2feac39e54.png" width="600" height="440">

XML 
<img width="1440" alt="Screen Shot 2022-09-21 at 23 30 48" src="https://user-images.githubusercontent.com/90792106/191560548-179be2f7-0af7-4937-9715-c31afd508697.png">
<img src="https://user-images.githubusercontent.com/90792106/191560548-179be2f7-0af7-4937-9715-c31afd508697.png" width="600" height="440">

JSON 
<img width="1440" alt="Screen Shot 2022-09-21 at 23 31 04" src="https://user-images.githubusercontent.com/90792106/191560569-46dc496f-e9db-41dd-ab29-5faad885184d.png">
<img src="https://user-images.githubusercontent.com/90792106/191560569-46dc496f-e9db-41dd-ab29-5faad885184d.png" width="600" height="440">
