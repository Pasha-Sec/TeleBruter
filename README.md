# TeleBruter
## Created By PashaSec

TeleBruter, verilen bir hedef kullanıcı adına sahip bir Telegram hesabının platforma kayıtlı telefon numarasını bulmak için kaba kuvvet yöntemiyle +90 formatında (Vodafone, Turkcell ve Turktelekom dahilinde) telefon numaraları oluşturan ve bu numaraları kontrol eden Python dili ile oluşturulmuş bir attack aracıdır. Kontrol işlemi, Python betiğinde "check" fonksiyonunda gerçekleşir.

check fonksiyonu, format dahilinde oluşturulmuş telefon numarasını alır ve bu numarayı Telegram hesapları arasında bulmaya çalışır. Eğer belirtilen kullanıcı adıyla eşleşen bir Telegram hesabı bulunursa sonucu veren bir mesaj döndürür. Eğer numarayla eşleşen bir hesap bulunamazsa, bir hata mesajı olan "err" döndürür. Biraz sabırlı olursanız, birçok kullanıcının numaralarını elde etmiş olacaksınız. Başlatın ve arkanıza yaslanıp bekleyin...

list_checker fonksiyonu ise, kullanıcının girdiği hedef kullanıcı adını alır ve Turkcell, Vodafone ve TurkTelekom operatörlerine ait telefon numara formatları üretir. Her bir numarayı check fonksiyonuna gönderir ve eğer doğru kullanıcı adıyla eşleşen bir numara bulunursa işlemi sonlandırır ve sonucu veren bir mesaj döndürür. Böylece, doğru numara, belirtilen kullanıcı adıyla eşleşen bir Telegram hesabının bulunmasıyla bulunmuş olur.

![SSlog](https://github.com/Pasha-Sec/TeleBruter/assets/148802667/fa3c728c-24f5-41c0-a397-b2439e008c5a)

![SSAttack](https://github.com/Pasha-Sec/TeleBruter/assets/148802667/5b8e82d0-930e-479e-82d6-27aac503e9cb)

![Pasted image](https://github.com/Pasha-Sec/TeleBruter/assets/148802667/54a30554-ec18-4e5b-b13f-d3d762d7965e)



## TeleBruter'i İndirin:
`sudo apt update`

`sudo apt-get install python3-pip`

`git clone https://github.com/Pasha-Sec/TeleBruter.git`

`cd TeleBruter`

`pip install -r requirements.txt`

`python3 TeleBruter.py`


## Programı Çalıştırın:
Programı çalıştırmadan önce https://my.telegram.org/auth web sitesine gidin ve Telegram api kimliğinizi yaratın.

Betiği bir metin düzenleyici yardımıyla açın ve 75. Satıra ('Your_Phone' bölümüne ve tırnak içinde olacak şekilde) Telegram hesabınızın numarasını girin. 76. Satıra da belirtilen yerleri API kimliğiniz (Your_Api_İD ve 'Your_Api_Hash' tırnak içinde olacak şekilde) ile doldurun. Böylece program çalışır duruma gelecektir.

![ssmalu](https://github.com/Pasha-Sec/TeleBruter/assets/148802667/ca8d2e70-900b-4022-8ffc-c213b4c863a0)


		
## UYARI:
Ancak, Telegram API'nin kullanım politikalarına ve ağır kullanım veya spam önlemlerine uygun hareket etmek önemlidir. Sürekli olarak çok fazla istek göndermek veya spam benzeri davranışlar sergilemek, Telegram hesabınızın askıya alınmasına veya API erişiminizin engellenmesine neden olabilir. Bu nedenle, programı aşırıya kaçmadan ve Telegram API'nin sınırlarını göz önünde bulundurarak kullanmak önemlidir.

### Sorumluluk Reddi Beyanı
Program eğitim amaçlıdır. Tüm sorumluluk yalnızca kullanıcıya aittir.

### Bana Ulaşın:
Programdaki hataları, tespit ettiğiniz bugları veya isteklerinizi bildirmek için bana ulaşın: pashasectr@gmail.com
