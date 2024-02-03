# TeleBruter
## Created By PashaSec

TeleBruter, verilen bir hedef kullanıcı adına sahip bir Telegram hesabının platforma kayıtlı telefon numarasını bulmak için kaba kuvvet yöntemiyle +90 formatında (Vodafone, Turkcell ve Turktelekom dahilinde) telefon numaraları oluşturan ve bu numaraları kontrol eden Python dili ile oluşturulmuş bir attack aracıdır. Kontrol işlemi, Python betiğinde "check" fonksiyonunda gerçekleşir.

check fonksiyonu, format dahilinde oluşturulmuş telefon numarasını alır ve bu numarayı Telegram hesapları arasında bulmaya çalışır. Eğer belirtilen kullanıcı adıyla eşleşen bir Telegram hesabı bulunursa sonucu veren bir mesaj döndürür. Eğer numarayla eşleşen bir hesap bulunamazsa, bir hata mesajı olan "err" döndürür. Biraz sabırlı olursanız, birçok kullanıcının numaralarını elde etmiş olacaksınız. Başlatın ve arkanıza yaslanıp bekleyin...

list_checker fonksiyonu ise, kullanıcının girdiği hedef kullanıcı adını alır ve Turkcell, Vodafone ve TurkTelekom operatörlerine ait telefon numara formatları üretir. Her bir numarayı check fonksiyonuna gönderir ve eğer doğru kullanıcı adıyla eşleşen bir numara bulunursa işlemi sonlandırır ve sonucu veren bir mesaj döndürür. Böylece, doğru numara, belirtilen kullanıcı adıyla eşleşen bir Telegram hesabının bulunmasıyla bulunmuş olur.

Diğer Telegram attack araçlarından farkı da budur. Herhangi bir listeye gerek duymadan anında yüzlerce numara oluşturuyor olması! Yakın bir zamanda yapılacak bir güncellemeyle diğer ülkelerin formatında da çalışabilir duruma gelecektir.

![SSlog](https://github.com/Pasha-Sec/TeleBruter/assets/148802667/fa3c728c-24f5-41c0-a397-b2439e008c5a)

![SSAttack](https://github.com/Pasha-Sec/TeleBruter/assets/148802667/5b8e82d0-930e-479e-82d6-27aac503e9cb)

![Pasted image](https://github.com/Pasha-Sec/TeleBruter/assets/148802667/54a30554-ec18-4e5b-b13f-d3d762d7965e)



## TeleBruter'i İndirin:
### for Ubuntu & Debian:

`sudo apt update`

`sudo apt-get install python3-pip`

`git clone https://github.com/Pasha-Sec/TeleBruter.git`

`cd TeleBruter`

`pip install -r requirements.txt`



### for Windows:

* [Python 3 edin](https://www.python.org/)

  Terminalden kontrol et: `python -version` veya `python3 --version`

* Pip'i edin: Önce get-pip'i kur: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py` ve Pip'i kur: `python get-pip.py` ayrıca kurulumu doğrulamayı unutma: `python` (veya `python3`) `-m pip help`


* [Git'i indir](https://git-scm.com/download/win)

  `git clone https://github.com/Pasha-Sec/TeleBruter.git`
  
  `cd TeleBruter`

  `pip install -r requirements.txt` (bu komutu girerken "no on Path" hata mesajı alınırsa Pip'i Windows ortam değişkenlerine atayın.)

  `python` (veya `python3`) `TeleBruter.py`


## Programı Çalıştırın:
Programı çalıştırmadan önce https://my.telegram.org/auth web sitesine gidin ve Telegram api kimliğinizi yaratın.

Betiği bir metin düzenleyici yardımıyla açın ve 75. Satıra ('Your_Phone' bölümüne ve tırnak içinde olacak şekilde) Telegram hesabınızın numarasını girin. 76. Satıra da belirtilen yerleri API kimliğiniz (Your_Api_İD ve 'Your_Api_Hash' tırnak içinde olacak şekilde) ile doldurun. Her şey tamamsa `python3 TeleBruter` çalıştırmaya hazırsınız.

![ssmalu](https://github.com/Pasha-Sec/TeleBruter/assets/148802667/ca8d2e70-900b-4022-8ffc-c213b4c863a0)


		
## UYARI:
Ancak, Telegram API'nin kullanım politikalarına ve ağır kullanım veya spam önlemlerine uygun hareket etmek önemlidir. Sürekli olarak çok fazla istek göndermek veya spam benzeri davranışlar sergilemek, Telegram hesabınızın askıya alınmasına veya API erişiminizin engellenmesine neden olabilir. Bu nedenle, programı aşırıya kaçmadan ve Telegram API'nin sınırlarını göz önünde bulundurarak kullanmak önemlidir.

### Sorumluluk Reddi Beyanı
Program eğitim amaçlıdır. Tüm sorumluluk yalnızca kullanıcıya aittir.

### Bana Ulaşın:
Programdaki hataları, tespit ettiğiniz bugları veya isteklerinizi bildirmek için bana ulaşın: pashasectr@gmail.com

## Copyright (c) 2024
# Telif Hakkı Bildirimi

Tüm hakları saklıdır. Bu proje (burada "TeleBruter" olarak anılacaktır), aşağıdaki lisans koşulları altında sunulmaktadır.

### Kullanım Hakkı

Yazılımın tüm kullanım hakkı sahibi PashaSec'dir. Yazılımın izinsiz kopyalanması, dağıtılması veya değiştirilmesi yasaktır.

### Lisans

Bu Yazılım MIT lisansı altında lisanslanmıştır. Aşağıdaki koşullara tabidir:

Yazılımın bir kopyasını edinen herkese, bu yazılımı kullanma, değiştirme, birleştirme izni verilir. 

YAZILIM "TİCARET İÇİN UYGUNLUK, BELİRLİ BİR AMACA UYGUNLUK VE İHLAL OLMAMASI DAHİL ANCAK BUNLARLA SINIRLI OLMAMAK ÜZERE" HİÇBİR GARANTİ İLE SAĞLANMAMAKTADIR. HERHANGİ BİR TALEP, ZARAR VEYA DİĞER SORUMLULUKTAN SORUMLU DEĞİLDİR VEYA İHLALDEN SORUMLU TUTULAMAZ.

### Katkılar

Katkılarınızı büyük bir memnuniyetle karşılıyoruz! Lütfen bu projeye katkıda bulunmaktan çekinmeyin. Katkılarınız için teşekkür ederiz.

### İletişim

Proje sahibi ile iletişim kurmak için lütfen [e-posta adresi](pashasectr@gmail.com)'ni kullanın.
