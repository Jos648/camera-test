# camera-test
andord L
burada elini yumruk yaptiginda telefon kendini yeniden baslatir yani bu kendini yeniden baslatyorsa hersey duzgun ireliyor koda bir az daha duzenleme yapip elerin uzaktan kontrol etmeye basliyacaksin 


bunu kopyala terminale yaz "python camera.py" 





1. Termux’u Aç ve Güncelle
İlk olarak Termux’u aç ve sistem paketlerini güncelle:

bash
Kopyala
Düzenle
pkg update && pkg upgrade -y
2. Python ve Git’i Yükle
Python ve Git yüklü değilse hemen yükle:

bash
Kopyala
Düzenle
pkg install python git -y
3. Projeyi GitHub’dan İndir
Projeyi GitHub’dan bilgisayarına indirmek için aşağıdaki komutu yaz (GitHub linkini kendi repo adresinle değiştir):

bash
Kopyala
Düzenle
git clone https://github.com/KULLANICI_ADIN/hand_control_system.git
4. Proje Klasörüne Gir
İndirilen klasöre geç:

bash
Kopyala
Düzenle
cd hand_control_system
5. Python Paketlerini Kur
Projede kullanılan paketleri yükle:

bash
Kopyala
Düzenle
pip install --upgrade pip
pip install -r requirements.txt
Bu dosyada şu paketler var:

opencv-python (kamera ve görüntü işleme için)

mediapipe (el takibi için Google kütüphanesi)

6. Termux’a Kamera İzni Ver
Termux’un kameraya erişebilmesi için izin vermen gerekiyor. Şu komutla kameranın çalıştığını test et:

bash
Kopyala
Düzenle
termux-camera-photo -c 0 test.jpg
Eğer hata verirse, telefonunun ayarlarından Termux uygulamasına kamera izni vermelisin.

7. Programı Çalıştır
Şimdi programı başlat:

bash
Kopyala
Düzenle
python main.py
8. Program Nasıl Çalışır?
Kamera açılır ve görüntü ekranında elini görürsün.

Elinle hareket edebilirsin, MediaPipe elini takip eder.

Yumruk yaptığında (başparmak ile işaret parmağı uçları birbirine çok yaklaşınca) program kendini yeniden başlatır.

Programdan çıkmak için ESC tuşuna bas.
