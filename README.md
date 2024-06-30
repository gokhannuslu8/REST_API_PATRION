# Proje Adı

REST API.

## Başlarken

Bu talimatlar, projenizi geliştirme ve test etme amaçlarıyla yerel makinenizde çalıştırmanıza yardımcı olacaktır.

### Gereksinimler

Yazılımı yüklemek için gereken şeyler ve bunları nasıl yükleyeceğiniz:

- Python (3.x sürümü)
- MongoDB
- Sanal Ortam (isteğe bağlı ancak önerilir)

### Kurulum

Geliştirme ortamınızı çalıştırmak için adım adım örnekler:

1. **Depoyu klonlayın:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Sanal ortam oluşturun (isteğe bağlı ancak önerilir):**
    ```bash
    python -m venv venv
    ```

3. **Sanal ortamı etkinleştirin:**
    - **Windows için:**
      ```bash
      venv\Scripts\activate
      ```
    - **Mac/Linux için:**
      ```bash
      source venv/bin/activate
      ```

4. **Bağımlılıkları yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

5. **MongoDB'yi kurun ve başlatın:**
    - Eğer yüklü değilse MongoDB'yi yükleyin.
    - MongoDB servisini başlatın.

6. **Çevresel değişkenleri yapılandırın:**
    Kök dizininde bir `.env` dosyası oluşturun ve aşağıdaki değişkenleri ekleyin:
    ```env
    MONGO_URI=<mongodb-uri'niz>
    MONGO_DBNAME=mydatabase
    JWT_SECRET_KEY=<jwt-gizli-anahtarınız>
    ```

### Uygulamayı Çalıştırma

1. **Flask uygulamasını başlatın:**
    ```bash
    flask run
    ```

2. **API'ye erişin:**
    - API varsayılan olarak `http://localhost:5000` adresinde erişilebilir.
    - API endpoint'leriyle etkileşim için `curl`, `Postman` veya bir web tarayıcısı kullanabilirsiniz.

## Kullanım

Projenizi nasıl kullanacağınızı açıklayın. Gerekirse örnekler ekleyin.

## API Endpoint'leri

API endpoint'lerinizi burada örnekler ve beklenen yanıtlarla açıklayın.

### Fabrika Oluşturma

- **URL:** `/factories`
- **Metod:** `POST`
- **Başlık:** `Authorization: Bearer <jwt-token>`
- **Gövde:**
  ```json
  {
    "name": "Fabrika Adı",
    "location": "Fabrika Konumu",
    "capacity": 100
  }

 ### Testlerin Çalıştırılması
Sistem için otomatik testleri nasıl çalıştıracağınızı açıklayın.

###  Test bağımlılıklarını yükleyin:

pip install pytest pytest-flask

###  Testleri çalıştırın:

pytest

 ### KATKIDA BULUNMA

1- Depoyu çatallayın (fork).

2- Yeni bir dal oluşturun:

git checkout -b feature/yeni-özellik

3- Değişikliklerinizi yapın ve bunları kaydedin

git add .

git commit -m "Yeni özellik eklendi"


### Değişikliklerinizi gönderin

git push origin feature/yeni-özellik


