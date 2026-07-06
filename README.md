# 🌦️ Weather API with Redis Caching

Un microserviciu web dezvoltat în **Flask** care oferă prognoza meteo prin interogarea unui API extern (Visual Crossing), optimizat cu **Redis** pentru performanță ridicată.

## 🚀 Despre Proiect
Acest proiect demonstrează utilizarea corectă a:
- **Flask** pentru crearea unui API RESTful.
- **Redis** pentru implementarea unei strategii de *Cache-Aside* (reducerea cererilor externe și creșterea vitezei).
- **Variabilelor de mediu** (`.env`) pentru securitatea cheilor API.

## 🛠️ Tehnologii Folosite
* Python 3.14
* Flask (Web Framework)
* Redis (In-memory Data Store)
* Requests (HTTP Library)
* Visual Crossing Weather API

## 📋 Configurare și Instalare

### 1. Clonarea repository-ului
```bash
git clone <URL-ul-proiectului-tau>
cd Weather-API
```

### 2. Crearea mediului virtual
```bash
python3 -m venv api_env
source api_env/bin/activate
```

### 3. Instalarea dependentelor
```bash
pip install -r requirements.txt
```

### 4. Configurare variabile de mediu
```bash
WEATHER_API_KEY=cheia_ta_aici
```

### 5. Pornire server
```bash
python3 main.py
```

### Accesează următoarea rută în browser sau folosind un client de API (ex: Postman/cURL):
```bash
http://127.0.0.1:5000/weather?city=Iasi
```

