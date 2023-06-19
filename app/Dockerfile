# İlk aşama: Python imajını alın
FROM python:3.9-slim-buster

# Çalışma dizinini belirleyin
WORKDIR /flask

# Gerekli dosyaları kopyalayın
COPY requirements.txt .

# Python paketlerini yükleyin
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyalayın
COPY . .

# Flask uygulamasını çalıştırın
CMD ["python", "app.py"]
