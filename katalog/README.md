## TUGAS 2 PBP - C 

Hana Devi Aqila - 2106751556

Link Heroku: 
https://katalog-hana.herokuapp.com (Hello world)
https://katalog-hana.herokuapp.com/katalog (Tampilan katalog)

**-- Jawaban --**

_**1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;**_

<img src="https://user-images.githubusercontent.com/90792106/189834848-463802bd-42a9-4f0d-a91a-301f8b0f9d0b.png" width="600" height="440">

Saat request client masuk, ia akan diproses oleh urls.py terlebih dahulu. Hal ini dikarenakan url routingnya ada di urls.py. Kemudian, urls.py akan mengecek path yang diminta pada request lalu akan diforward request tersebut ke views.py yang sesuai. Jika fungsi pada views.py membutuhkan read/write data dari database, maka views.py akan menghubungi atau mengambil data dari models.py sebagai perantara ke database. Kemudian, untuk menampilkan data tersebut, views.py akan mengakses template tampilan yang sesuai pada berkas html. Output akhirnya berupa halaman html yang utuh sebagai response untuk client. Kaitan antara urls.py, views.py, models.py, dan berkas html adalah semuanya berperan dan saling terhubung dalam memproses response dari suatu request client. 



_**2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**_
    
Virtual environment adalah sebuah environment yang terisolasi dari dependencies utama. Dengan begitu, setiap environment dapat memiliki dependecies yang sesuai dengan kriterianya masing-masing tanpa harus tercampur dengan dependecies dari environment yang lain. Penggunaan virtual environment bersifat unlimited sehingga kita dapat membuat membuat banyak venv untuk banyak project yang berbeda-beda. Tools ini juga banyak digunakan di Python yaitu di Django, untuk mengeksekusi suatu aplikasi yang dibuat. 

Saat kita menginstall suatu library tanpa menggunakan virtual env, maka secara default library tersebut akan terinstall secara global pada python dan semua aplikasi bisa mengaksesnya. Namun, biasanya antar aplikasi membutuhkan dan cocok dengan library atau versi library yang berbeda-beda. Jika diinstall secara global, ketika library tersebut diupgrade ke versi terbaru, lalu terdapat aplikasi A yang kita buat tidak kompatibel dengan versi terbaru library tersebut. Tentunya aplikasi A menjadi tidak bisa berjalan dengan baik. Sementara itu, terdapat aplikasi B yang membutuhkan library versi terbaru tersebut untuk berjalan. Oleh karena itu, penggunaan virtual env penting untuk mencegah hal-hal semacam itu terjadi sehingga setiap aplikasi tetap dapat berjalan dengan librarynya masing-masing yang sudah terisolasi. Kita tetap dapat membuat aplikasi web tanpa menggunakan virtual environment, tetapi sebaiknya tetap memakai virtual environment agar dependenciesnya bisa terklasifikasi dengan baik.  


_**3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.**_


Cara implementasi poin 1 adalah mengimport class CatalogItem dari file models.py agar dapat mengambil data dari model. Kemudian juga mengimport fungsi render dari django.shortcut yang berfungsi untuk memproses data dari model menjadi httpresponse (berupa html) sesuai dengan template html yang dimasukkan pada parameternya. Selanjutnya mengisi views.py dengan fungsi show_katalog berparamater request (Any) dan me-return dengan pemanggilan fungsi render(request, "katalog.html", context). "katalog.html" sebagai template httpresponsenya sehingga nanti tampilannya akan sesuai dengan codingan di katalog.html. Sementara itu, context adalah bahan konten yang akan ditampilkan oleh html, context berisi keterangan yang diimpor dari model (CatalogItem) dan keterangan lain yang diperlukan.  

Cara implementasi poin 2 adalah membuat berkas bernama urls.py yang akan me-routing fungsi views ke html agar dapat ditampilkan di browser. Berdasarkan template codingan dari urls.py, caranya adalah menambahkan "path('katalog/', include('katalog.urls'))," pada list url_patterns. Dengan begitu, kita akan memasukkan url configuration lain ke list urlpatternsnya. Namun, sebelumnya kita juga harus mengimport function path dan include dari django.urls karena akan dipanggil di dalam list urlpatterns untuk mengakses data yang terkait. 

Cara implementasi poin 3 adalah dengan meng-load data dari file json pada folder fixtures ke dalam database Django lokal. Syntaxnya berupa python manage.py loaddata initial_catalog_data.json. Data tersebut akan tersimpan dalam CatalogItem kemudian terdata di context pada fungsi di views.py yang nantinya akan diproses ke html menggunakan pemanggilan fungsi render pada returnnya.

Cara implementasi poin 4 adalah dengan add, commit, dan push perubahan yang telah dibuat ke repo di github. Sebelumnya perlu membuat file Procfile, dpl.yml, .gitignore, dan perubahan lain yang dibutuhkan. Lalu, menambahkan variabel repository secret untuk deployment. Variabel tersebut berupa API key dari akun heroku dan nama aplikasi yang dibuat di heroku. Kemudian re-run workflow yang failed hingga berhasil. Setelah itu, link aplikasi heroku appnya sudah bisa diakses. 

**Referensi:**
https://www.petanikode.com/python-virtualenv/ 
https://www.petanikode.com/django-untuk-pemula/ 
