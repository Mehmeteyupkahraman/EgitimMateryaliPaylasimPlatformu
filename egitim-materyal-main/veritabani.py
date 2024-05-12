import sqlite3

class veritabani:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='dersler'")
        tablo_var_mi = self.cursor.fetchone()

        if not tablo_var_mi:  # Tablo yok
            self.cursor.execute('CREATE TABLE IF NOT EXISTS kullanicilar (ID INTEGER PRIMARY KEY AUTOINCREMENT, kullaniciadi TEXT, sifre TEXT, ad TEXT, soyad TEXT, telefon TEXT, tur INTEGER)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS dersler (ID INTEGER PRIMARY KEY AUTOINCREMENT, ders_adi TEXT, ogretmen_adi TEXT, ders_turu TEXT, konu TEXT, fotograf TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS ders_listem (ID INTEGER PRIMARY KEY AUTOINCREMENT, kullanici_id INTEGER, ders_id INTEGER, katilmatarih TIMESTAMP)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS sorular (ID INTEGER PRIMARY KEY AUTOINCREMENT, kullanici_id INTEGER, ders_id INTEGER, soru TEXT, yanit TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS ders_icerik (ID INTEGER PRIMARY KEY AUTOINCREMENT, ders_id INTEGER, sayfa INTEGER, icerik TEXT)')

            # Derslerin eklenmesi
            dersler_tuple = [
                ("Matematik", "Fırat Yılmaz", "Sayısal Ders", "Matematik dersi, sayılar, geometri, cebir, trigonometri, fonksiyonlar, olasılık ve istatistik gibi konuları kapsayan geniş bir alandır. Temel aritmetik işlemlerinden karmaşık diferansiyel denklemlere kadar çeşitli konuları içerir. Matematik, mantıklı düşünme, problem çözme becerilerini geliştirme ve soyut düşünme yeteneklerini artırma gibi faydalar sağlar. Ayrıca bilim, mühendislik, ekonomi, sosyal bilimler ve diğer birçok alanda da temel bir rol oynar.", "matematik.jpg"),
                ("Türkçe", "Ayşe Yılmaz", "Dil ve Anlatım", "Türkçe dersi, dil bilgisi, yazım kuralları, sözcük dağarcığı ve yazılı ve sözlü anlatım becerilerini içeren bir derstir. Doğru ve etkili iletişim kurma yeteneğini geliştirmek, dilin doğru kullanımını sağlamak ve edebi metinleri anlamak için önemlidir. Türkçe dersi aynı zamanda edebiyatı tanıma, şiir, hikaye, roman gibi edebi türleri analiz etme ve yorumlama becerilerini de kapsar.", "turkce.jpg"),
                ("Fizik", "Ahmet Kaya", "Fen Bilimleri", "Fizik dersi, madde, enerji, kuvvet ve hareket gibi temel fiziksel kavramları inceler. Doğa olaylarını açıklamak ve gelecekteki teknolojik gelişmeleri öngörmek için önemli bir temel sağlar. Fizik, deney ve gözlem yapma becerilerini geliştirmek, soyut düşünme yeteneklerini güçlendirmek ve analitik düşünme becerilerini artırmak için de önemlidir.", "fizik.jpg"),
                ("Biyoloji", "Fatma Yıldız", "Fen Bilimleri", "Biyoloji dersi, yaşamın temel prensiplerini, canlı organizmaların yapısını, işleyişini ve çevreleriyle olan etkileşimlerini inceler. İnsan vücudu, hücreler, genetik, evrim ve çevre bilimleri gibi konuları kapsar. Biyoloji, sağlık bilincini artırmak, çevreyi korumak ve doğal dünyayı anlamak için önemlidir.", "biyoloji.jpg"),
                ("Kimya", "Mehmet Demir", "Fen Bilimleri", "Kimya dersi, maddenin yapısını, özelliklerini, bileşimini ve reaksiyonlarını inceler. Kimyanın temel prensiplerini anlamak, günlük hayatta karşılaşılan olayları açıklamak ve endüstriyel süreçleri anlamak için önemlidir. Kimya, analitik düşünme becerilerini geliştirmek ve laboratuvar deneyimi kazandırmak açısından da değerlidir.", "kimya.jpg"),
                ("Geometri", "Ayşe Yılmaz", "Sayısal Ders", "Geometri dersi, temel geometrik kavramları ve şekilleri öğretir. Doğrular, açılar, üçgenler, dörtgenler, daire ve katı cisimler gibi konuları kapsar.", "geometri.jpg"),
                ("Tarih", "Mustafa Yılmaz", "Sosyal Bilimler", "Tarih dersi, geçmişteki olayları, toplumların ve medeniyetlerin gelişimini inceler. Tarih, kültürel mirasın korunması, toplumsal değişimin anlaşılması ve tarihsel olayların bugünkü etkilerinin anlaşılması için önemlidir.", "tarih.jpg"),
                ("Coğrafya", "Zeynep Korkmaz", "Sosyal Bilimler", "Coğrafya dersi, dünya yüzeyinin fiziksel özellikleri, iklim, bitki örtüsü, su kaynakları ve insan etkinliklerini inceler. Coğrafya, dünyanın farklı bölgelerini anlamak, insan etkisinin doğal çevre üzerindeki etkilerini incelemek ve sürdürülebilirlik kavramını anlamak için önemlidir.", "cografya.jpg"),
                ("Din Kültürü ve Ahlak Bilgisi", "Fatma Kaya", "Sosyal Bilimler", "Din Kültürü ve Ahlak Bilgisi dersi, dinlerin kökeni, inançları, ibadetleri, ahlaki değerleri ve insanların yaşamlarına etkilerini inceler. Bu ders, öğrencilere dinler arası anlayışı artırma, farklı din ve inanç sistemlerini anlama ve hoşgörüyü geliştirme fırsatı sunar.", "din.jpg")
            ]

            # Ders içeriğinin eklenmesi
            icerikler_tuple = [
                (1, 1, "Matematik dersine hoş geldiniz! Bu dersimizde temel matematik kavramlarını öğreneceğiz. İlk olarak sayılarla başlayacağız."),
                (1, 2, "Sayılarla ilgili temel kavramları öğrendikten sonra, geometriye geçiş yapacağız. Geometri dersinde temel şekilleri ve ölçü birimlerini öğreneceğiz."),
                (1, 3, "Geometri dersini tamamladıktan sonra, cebir konusuna geçiş yapacağız. Cebirde denklem çözme ve matematiksel ifadeleri anlama becerilerimizi geliştireceğiz."),
                (2, 1, "Türkçe dersine hoş geldiniz! Bu dersimizde dil bilgisi kurallarını, yazım kurallarını ve sözcük dağarcığını öğreneceğiz."),
                (2, 2, "Dil bilgisi kurallarını öğrendikten sonra, yazılı ve sözlü iletişim becerilerini geliştireceğiz. Edebi metinleri analiz etmeye başlayacağız."),
                (3, 1, "Fizik dersine hoş geldiniz! Bu dersimizde temel fiziksel kavramları öğreneceğiz. Madde, enerji ve hareket gibi konuları ele alacağız."),
                (4, 1, "Biyoloji dersine hoş geldiniz! Bu dersimizde canlı organizmaların yapısını ve işleyişini inceleyeceğiz. Hücrelerden başlayarak genetik ve evrim konularını ele alacağız."),
                (5, 1, "Kimya dersine hoş geldiniz! Bu dersimizde maddenin yapısını ve reaksiyonlarını öğreneceğiz. Kimyasal bileşimler ve reaksiyonlar üzerinde çalışacağız."),
                (6, 1, "Geometri dersine hoş geldiniz! Bu dersimizde temel geometrik kavramları ve şekilleri öğreneceğiz. İlk olarak doğrular ve açılar konusunu ele alacağız."),
                (6, 2, "Doğrular ve açılar konusunu öğrendikten sonra, üçgenler ve dörtgenler gibi çokgenler üzerinde çalışacağız. Çokgenlerin özelliklerini öğreneceğiz."),
                (6, 3, "Çokgenlerin özelliklerini öğrendikten sonra, daire ve çember konusunu işleyeceğiz. Dairelerin alan ve çevre hesaplarını yapmayı öğreneceğiz."),
                (7, 1, "Tarih dersine hoş geldiniz! Bu dersimizde tarihi olayları ve dönemleri inceleyeceğiz. İlk olarak insanlık tarihine genel bir bakış yapacağız."),
                (7, 2, "İnsanlık tarihini öğrendikten sonra, önemli medeniyetleri ve uygarlıkları inceleyeceğiz. Medeniyetlerin ve kültürlerin gelişimini anlamaya çalışacağız."),
                (8, 1, "Coğrafya dersine hoş geldiniz! Bu dersimizde dünya yüzeyinin fiziksel özelliklerini ve insan etkinliklerini inceleyeceğiz. İlk olarak coğrafi kavramları ve harita okumayı öğreneceğiz."),
                (8, 2, "Harita okumayı öğrendikten sonra, iklim ve bitki örtüsü konularını işleyeceğiz. Dünya üzerindeki farklı iklim tiplerini ve bitki örtüsü bölgelerini inceleyeceğiz."),
                (9, 1, "Din Kültürü ve Ahlak Bilgisi dersine hoş geldiniz! Bu dersimizde farklı dinlerin inançlarını, ibadetlerini ve ahlaki değerlerini öğreneceğiz. İlk olarak dinin tanımını ve dinler arası diyalog kavramını ele alacağız."),
                (9, 2, "Dinin temel kavramlarını öğrendikten sonra, İslam, Hristiyanlık, Yahudilik ve diğer önemli dinlerin inançlarını ve ibadetlerini inceleyeceğiz.")
            ]

            # Veritabanına derslerin ve ders içeriğinin eklenmesi
            self.cursor.execute("INSERT INTO kullanicilar (kullaniciadi, sifre, ad, soyad, telefon,tur) VALUES ('eyüp', '123', 'eyüp', 'yılmaz', '5321122334', 0)")
            self.cursor.execute("INSERT INTO kullanicilar (kullaniciadi, sifre, ad, soyad, telefon,tur) VALUES ('ogretmen', '123', 'Erdem', 'Yücesan', '5351122326', 1)")
            self.cursor.executemany("INSERT INTO dersler (ders_adi, ogretmen_adi, ders_turu, konu, fotograf) VALUES (?,?,?,?,?)", dersler_tuple)
            self.cursor.executemany("INSERT INTO ders_icerik (ders_id, sayfa, icerik) VALUES (?,?,?)", icerikler_tuple)
            self.connection.commit()

    def query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()
        return self.cursor
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def fetchone(self):
        return self.cursor.fetchone()

# Veritabanı bağlantısının oluşturulması
Veritabani = veritabani('sql.db')
