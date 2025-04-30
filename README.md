# Unisex Bathroom Problem - Python Implementation

Bu proje, klasik "Unisex Bathroom Problem" için Python kullanılarak geliştirilmiş bir çözüm modelidir.  
Problem, bir tuvaletin aynı anda sadece erkekler ya da sadece kadınlar tarafından kullanılabilmesini, ancak her iki grubun da adil (fair) bir şekilde erişebilmesini sağlamayı amaçlar.


## 🧩 Problem Tanımı

- Erkekler ve kadınlar tuvaleti kullanmak istiyor.
- Aynı anda hem kadın hem erkek tuvalette olamaz.
- Aynı türden en fazla 3 kişi aynı anda tuvaleti kullanabilir.
- Tuvalet boşaldığında diğer cinsiyete fırsat tanınır.
- Gereksiz beklemeler ve starvation (aç kalma) önlenmelidir.


## 🛠 Kullanılan Yapılar

- `threading.Semaphore`: Aynı anda sınırlı sayıda kişinin erişimini kontrol eder.
- `threading.Lock`: Birden fazla thread arasında kritik bölgeleri güvenli hale getirir.
- `Lightswitch` Sınıfı: 
  - Bir grup kişi için giriş-çıkışları organize eder.
  - İlk gelen, ortak kaynağı (tuvaleti) kilitler; son çıkan serbest bırakır.


## 📜 Kod Akışı

1. Erkekler ve kadınlar için ayrı ayrı fonksiyonlar (`male_use_bathroom`, `female_use_bathroom`) tanımlandı.
2. `Lightswitch` mekanizması ile ilk gelen semaforu kapatır, son çıkan açar.
3. `Multiplex` semaforu ile aynı anda en fazla 3 kişinin tuvalette bulunması sağlandı.
4. `Turnstile` semaforu ile giriş sırası adil hale getirildi.
5. Thread'ler oluşturulup rastgele karıştırılarak eş zamanlı çalıştırıldı.



