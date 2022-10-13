# TUGAS 6

### 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Pada asynchronus programming, pengguna bisa tetap berinteraksi dengan pagenya sambil menunggu respons dari server yang masih me-load data. Contohnya adalah website W3Schools. Sebaliknya, synchronus programming menerapkan click-wait-reresh sehingga user harus menunggu proses load data dari server dan baru bisa berinteraksi dengan pagenya lagi setelah server memberikan responsenya. Contohnya adalah server SIAK-NG yang mana user baru bisa war hanya ketika ia berhasil masuk ke servernya. 


### 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Paradigma event-driven programming adalah pemrograman yang alur programnya dieksekusi berdasarkan kejadian suatu event/peristiwa sebagai trigger/pemicunya. Pada tugas kali ini, contoh dari penerapan event-driven programming adalah penggunaan button add-task. Saat button tersebut diklik oleh user, maka program akan menampilkan modal untuk tambah task baru sebagai responsenya. 


### 3. Jelaskan penerapan asynchronous programming pada AJAX.

Asynchronus programming pada AJAX membuat usernya tidak perlu melakukan click-wait-refresh. AJAX adalah teknik untuk membuat web app lebih interaktif lagi dengan meng-update suatu page secara dinamis sehingga usernya tidak perlu reload page secara keseluruhan jika ada suatu perubahan kecil. 


### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

AJAX GET: membuat fungsi baru di `views.py` yaitu `ajax_get` dan membuat pathnya juga di `urls.py`. Kemudian di `base.html` menambahkan link ajax dan di `todolist.html` mengganti bagian for loop task dengan script yang berisi asynchronus function. 

AJAX POST: membuat fungsi baru di `views.py` yaitu `ajax_post` dan membuat pathnya juga di `urls.py`. Kemudian di `base.html` menambahkan link ajax dan di `todolist.html` menambahkan button add-task dan pembuatan modal sebagai response dari event-driven programming dari button add-task. Selain itu juga menerapkan asynchronus function untuk post task tambahan tersebut. 

