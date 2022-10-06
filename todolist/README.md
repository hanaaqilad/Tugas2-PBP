## LINK APLIKASI
Link Heroku: https://katalog-hana.herokuapp.com/todolist/

## TUGAS 4 PBP
1. Apa kegunaan {% csrf_token %} pada elemen ``<form>`` ? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen ``<form>`` ?

    csrf adalah singkatan dari Cross Site Request Forgery, merupakan suatu serangan yang umum terjadi pada web-app dan dapat merugikan user serta membahayakan web-app tersebut. Kegunaan dari {% csrf_token %} adalah untuk menghindari serangan tersebut. Cara kerja dari {% csrf_token %} adalah dengan menghasilkan token pada server dan akan selalu mengecek token tersebut setiap ada request yang masuk. Jika token tersebut tidak ditemukan, maka requestnya tidak akan dijalankan. Token tersebut unique, secret, dan unpredictable sehingga berbeda-beda setiap user. Jika {% csrf_token %} tidak digunakan, maka tidak ada token yang perlu dicek dan setiap request yang masuk bisa dijalankan tanpa dicek apakah request tersebut berupa serangan atau tidak. Dengan begitu, attacker akan mudah menyerang web dan user tersebut dengan mengubah dan mengirim request tanpa sepengetahuan dan persetujuan user yang sebenarnya. 

2. Apakah kita dapat membuat elemen ``<form>`` secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat ``<form>`` secara manual.
    
    Kita tetap bisa membuat elemen form tanpa generator seperti {{ form.as_table }}. Karena pada dokumentasi Django terkait forms saja di bagian contohnya tidak menggunakan {{ form.as_table }}, melainkan hanya {{ form }}. Saya juga sempat menggunakan {{ form }} saja saat membuat create_task.html dan formnya tetap berfungsi baik. Namun, tanpa generator, letaknya jadi cukup berantakan. Kemudian saat saya mencoba ikuti form register dengan {{ form.as_table }}, letaknya jadi lebih rapih. Cara membuat form adalah mulai dari membuat file forms.py yang berisi class formnya dan disesuaikan dengan models serta atribut apa saja yang ingin diminta inputannya melalui form. Lalu membuat fungsi untuk mengakses formnya pada file views.py (di sini contohnya adalah create_task()). Kemudian membuat htmlnya dengan menyisipkan code dengan tag ``<form> dan </form>`` di mana di dalamnya menggunakan {{ form }} atau generator lainnya. 

Tidak pakai {{ form.as_table }}

<img src="https://user-images.githubusercontent.com/90792106/192592314-ca7d354a-64e2-48f4-b5d9-875e633f6045.png" width="600" height="440">

Pakai {{ form.as_table }}

<img src="https://user-images.githubusercontent.com/90792106/192592315-62a3a05a-90cc-4477-8121-5ba0aeb857e7.png" width="600" height="440">

3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
    
    Pertama, user akan memberi input pada form yang sudah di-request. Lalu, browser akan meng-generate dan meneruskan HTTP Request, method, dan argumen ke url tujuan berdasarkan page form dan input tersebut ke server. Kemudian, server akan menerima data inputan tersebut lalu divalidasi menggunakan method ``is_valid`` dan apabila datanya valid maka akan dijadikan cleaned_data dan juga disimpan ke database dengan method ``save()``. Selanjutnya, server akan menjalankan fungsi pada views.py yang dipanggil dari fungsi form sebelumnya. Berdasarkan fungsi views.py yang dijalankan tersebut, server akan meng-generate HTML page yang selanjutnya akan ditampilkan oleh browser. Data input yang sudah tersimpan tadi akan dipanggil di dalam fungsi tersebut dan ditampilkan pada HTML page. 

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    1. Menjalankan ``python manage.py startapp todolist`` pada virtual environment tugas pbp
    2. Menambahkan todolist sebagai aplikasi pada settings.py dan path todolist pada list urlpatterns di urls.py project django. 
    3. Membuat class Task pada file models.py dengan atribut sesuai ketentuan soal dan paramater User didapat dari import, sebagai berikut:
    ``` shell
    from django.db import models
    from django.contrib.auth.models import User

    class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    ```
    4. Membuat fungsi register, login_user, dan logout_user pada views.py. Untuk class form pada register, sudah ada dari import UserCreationForm.
    ```shell
    # REGISTER
    def register(request):
        form = UserCreationForm()
        
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Akun telah berhasil dibuat!')
                return redirect('todolist:login')
        
        context = {'form':form}
        return render(request, 'register.html', context)

    # LOGIN
    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todolist:show_todolist')
            else:
                messages.info(request, 'Username atau Password salah!')
        context = {}
        return render(request, 'login.html', context)

    # LOGOUT
    def logout_user(request):
        logout(request)
        return redirect('todolist:login')
    ```
    5. Membuat file todolist.html yang menampilkan:
    username pengguna dengan `<h3>Username Pengguna :  {{username}} </h3>`;
    tombol tambah task dan logout dengan  `<button><a href="{% url 'todolist:create_task' %}">Tambah Task</a></button>` dan `<button><a href="{% url 'todolist:logout' %}">Logout</a></button>`;
    tabel berisi tanggal pembuatan, judul, dan deskripsi task dengan cara yang sama seperti html pada beberapa lab dan tugas sebelumnya. Versi lebih lengkapnya bisa dilihat langsung pada filenya. 
    6. Membuat file html baru yaitu create_task.html yang berisi code html untuk menampilkan formnya. Menggunakan tag `<form>`, generator {{ form.as_table }}, dan tag `<table>` serta menambahkan button input tambah task. File html ini juga dipanggil oleh fungsi create_task sebagai handle views.py untuk request formnya. Detail codenya bisa dilihat di file create_task.html
    7. Menambahkan seluruh path yang terkait ke urlpatterns pada urls.py todolist, sebagai berikut:
    ```shell
    urlpatterns = [
        path('', show_todolist, name='show_todolist'),
        path('register/', register, name='register'), 
        path('login/', login_user, name='login'), 
        path('logout/', logout_user, name='logout'), 
        path('create-task/', create_task, name='create_task'), 
    ]
    ```
    8. Git add, commit, push lalu re-run di githubnya agar berhasil terdeploy
    9. Membuat 2 akun melalui register dan menambahkan masing-masing user sebanyak 3 task melalui page tambah task

<img src="https://user-images.githubusercontent.com/90792106/192592172-31c71bc6-5d6e-430d-8722-3494ef732c18.png" width="600" height="440">
<img src="https://user-images.githubusercontent.com/90792106/192592187-8a1db7d1-a67f-42a6-9023-37977a274f72.png" width="600" height="440">

## TUGAS 5 PBP
1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
    - Inline CSS adalah cara penulisan CSS dengan cara menuliskan CSS propertiesnya secara langsung di body section elemennya. Style attributenya ditulis di dalam tag HTMLnya. 
    Kelebihan:
        - Prioritasnya paling utama. Dimana prioritas jika terdapat lebih dari satu styling, maka urutan prioritasnya adalah inline, external dan internal, lalu browser default. 
        - Sangat efektif untuk menguji style pada satu elemen.
        - Dapat digunakan untuk memperbaiki kode dengan cepat serta load websitenya juga akan lebih cepat.
    Kekurangan:
        - Kurang efisien karena hanya bisa merubah style pada satu elemen saja. 

    - Internal CSS adalah cara penulisan CSS dengan cara menuliskannya pada file HTML yang terkait. Cara penulisan ini bisa digunakan ketika hanya ingin styling suatu HTML secara terpisah atau unik. Caranya dengan menuliskan stylingnya di antara tag `<style>` dan `</style>` di bagian atas file HTML yang ingin di-styling.
    Kelebihan:
        - Efektif digunakan jika hanya ingin merubah style pada satu halaman saja. 
        - Tidak perlu mengupload file apapun karena CSS dan HTMLnya berada dalam satu file yang sama.
        - Class dan ID dapat digunakan oleh internal stylesheet.
    Kekurangan:
        - Kurang efisien jika ingin melakukan styling sekaligus terhadap beberapa halaman atau bahkan seluruh halaman. 
        - Memperlambat performa website. 

    - External CSS adalah cara penulisan CSS dengan cara menuliskannya pada file terpisah dari HTMLnya. Misalnya membuat static files berupa `style.css`. Lalu, styling pada file tersebut dapat dihubungkan dengan menyisipkan nama file tersebut di dalam tag `<link>`. 
    Kelebihan:
        - Memperkecil size file html dan penulisan htmlnya juga jadi lebih rapih.  
        - Loading website lebih cepat.
        - Dapat digunakan untuk styling beberapa halaman sekaligus.
    Kekurangan:
        - Jika file CSS nya gagal dipanggil karena koneksi yang buruk maka halaman HTMLnya bisa berantakan.

2. Jelaskan tag HTML5 yang kamu ketahui.
    - `<!DOCTYPE>` : untuk menentukan tipe dokumen
    - `<html>`   : untuk membuat sebuah dokumen HTML
    - `<title>`	: untuk membuat judul dari sebuah halaman
    - `<body>`	: untuk membuat tubuh dari sebuah halaman
    - `<h1> to <h6>`	: untuk membuat heading
    - `<p>`	: untuk membuat paragraf
    - `<br>`	: untuk memasukkan satu baris putus
    - `<!--...-->` : untuk membuat komentar
    - `<html>` : Tag untuk membuat dokumen HTML
    - `<a>`	: untuk membuat hyperlink
    - `<link>`	: untuk menghubungkan suatu dokumen dengan htmlnya
    - `<table>`	: untuk membuat tabel
    - `<th>`	: untuk membuat sebuah sel header tabel
    - `<tr>`	: untuk membuat baris dalam sebuah tabel
    - `<td>`	: untuk membuat sel dalam sebuah tabel
    - `<style>` : untuk membuat informasi style untuk dokumen
    - `<div>`	 : untuk membuat sebuah bagian dalam dokumen
    - `<form>` : untuk membuat form untuk meminta input dari user
    - `<input>` : untuk menunjukkan sebuah inputan berdasarkan tipe
 
3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
    - Element selector : cara menggunakan element selector adalah dengan memanfaatkan tag html sebagai selector untuk mengubah properti yang ada pada tag itu sendiri. Misalnya h1, p, h2, h3, dst. Contohnya `h1 {...}`
    - ID selector : cara menggunakan ID selector adalah dengan menambahkan beberapa ID pada tag html dan juga menambahkan ID selector pada file CSS maupun internal CSS dengan penulisan `#namaID {...}`
    - Class selector : cara menggunakan class selector adalah dengan menambahkan beberapa class pada tag html dan juga menambahkan class selector pada file CSS maupun internal CSS dengan penulisan `.namaClass {...}`
    
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    Menjalankan virtual environment pada direktori tugas pbp, kemudian membuka foldernya dan melakukan kustomisasi tampilan html dengan mencari referensi dari website bootstrap. Mengganti penggunaan tabel dengan card untuk halaman utama todolist serta menambahkan efek shadow pada cardnya jika sedang dihover. Lalu membuat 4 page tersebut responsive dengan menggunakan bootstrap. 
