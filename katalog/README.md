## TUGAS 2 PBP - C 

Hana Devi Aqila - 2106751556

Link Heroku: https://katalog-hana.herokuapp.com 

**-- Jawaban --**

**1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;**
<img src="https://user-images.githubusercontent.com/90792106/189834848-463802bd-42a9-4f0d-a91a-301f8b0f9d0b.png" width="600" height="440">




**2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
    
Virtual environment adalah sebuah environment yang terisolasi dari dependencies utama. Dengan begitu, setiap environment dapat memiliki dependecies yang sesuai dengan kriterianya masing-masing tanpa harus tercampur dengan dependecies dari environment yang lain. Penggunaan virtual environment bersifat unlimited sehingga kita dapat membuat membuat banyak venv untuk banyak project yang berbeda-beda. Tools ini juga banyak digunakan di Python yaitu di Django, untuk mengeksekusi suatu aplikasi yang dibuat. 

Saat kita menginstall suatu library tanpa menggunakan virtual env, maka secara default library tersebut akan terinstall secara global pada python dan semua aplikasi bisa mengaksesnya. Namun, biasanya antar aplikasi membutuhkan dan cocok dengan library atau versi library yang berbeda-beda. Jika diinstall secara global, ketika library tersebut diupgrade ke versi terbaru, lalu terdapat aplikasi A yang kita buat tidak kompatibel dengan versi terbaru library tersebut. Tentunya aplikasi A menjadi tidak bisa berjalan dengan baik. Sementara itu, terdapat aplikasi B yang membutuhkan library versi terbaru tersebut untuk berjalan. Oleh karena itu, penggunaan virtual env penting untuk mencegah hal-hal semacam itu terjadi sehingga setiap aplikasi tetap dapat berjalan dengan librarynya masing-masing yang sudah terisolasi. Kita tetap dapat membuat aplikasi web tanpa menggunakan virtual environment, tetapi sebaiknya tetap memakai virtual environment agar dependenciesnya bisa terklasifikasi dengan baik.  




**3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.**

    

**Referensi:**
https://www.petanikode.com/python-virtualenv/ 

