# MongoDB Değişiklik Algılama ile Kafka

Bu proje, bir üretici ve bir tüketici uygulaması geliştirir. Üretici uygulama, her 10 saniyede bir belirli bir MongoDB koleksiyonunu yeni belgeler için sorgular ve her yeni belge için bir JSON mesajını bir Kafka konusuna yayınlar. Tüketici uygulaması, Kafka konusundan mesajları tüketir ve onları konsola yazdırır.

## Kullanılan Teknolojiler

-   Python
-   Docker
-   Apache Kafka
-   ZooKeeper
-   Kafdrop
-   MongoDB

## Build Adımları

1. Bu repoyu klonlayın: `git clone https://github.com/Emir/dsadsa`
2. Proje dizinine gidin: `cd Proje adi`
3. Docker imajlarını oluşturun: `docker-compose build`
4. Docker hizmetlerini başlatın: `docker-compose up -d`

## Uygulamaların Çalıştırılması

Docker hizmetlerini başlattıktan sonra, üretici ve tüketici uygulamaları otomatik olarak çalışmaya başlar. Üretici, her 10 saniyede bir MongoDB koleksiyonunu yeni belgeler için kontrol eder ve yeni belgeleri Kafka konusuna yayınlar. Tüketici, Kafka konusundan mesajları tüketir ve onları konsola yazdırır.

## Lisans

Bu proje [MIT Lisansı](LICENSE.md) altında lisanslanmıştır.
