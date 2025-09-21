# Guía de Integraciones - Business Content Agent

Esta guía detalla cómo integrar el Agente de Contenido Empresarial con servicios externos como Google Drive, Google Custom Search y otras APIs necesarias para su funcionamiento completo.

## 🔗 Integración con Google Drive

### Configuración de Google Cloud Platform

#### Paso 1: Crear Proyecto

1. Accede a [Google Cloud Console](https://console.cloud.google.com/)
2. Haz clic en "Seleccionar un proyecto" → "Nuevo proyecto"
3. Asigna un nombre descriptivo: `Business Content Agent`
4. Selecciona la organización y ubicación (si aplica)
5. Haz clic en "Crear"

#### Paso 2: Habilitar APIs Necesarias

1. En el menú lateral, ve a "APIs y servicios" → "Biblioteca"
2. Busca y habilita las siguientes APIs:
   - ✅ **Google Drive API**
   - ✅ **Custom Search JSON API** (para búsqueda web)

#### Paso 3: Crear Credenciales OAuth 2.0

1. Ve a "APIs y servicios" → "Credenciales"
2. Haz clic en "Crear credenciales" → "ID de cliente OAuth"
3. Selecciona "Aplicación web" como tipo de aplicación
4. Configura la pantalla de consentimiento:
   - **Tipo de usuario**: Externo
   - **Nombre de la app**: Business Content Agent
   - **Correo electrónico de soporte**: tu-email@dominio.com
   - **Dominios autorizados**: agrega tu dominio si aplica
5. En "Alcances (scopes)", agrega:
   ```
   https://www.googleapis.com/auth/drive.readonly
   ```
6. Crea el cliente OAuth y descarga el archivo JSON
7. Renombra el archivo a `credentials.json` y colócalo en la raíz del proyecto

#### Paso 4: Configurar Carpeta de Google Drive

1. Abre [Google Drive](https://drive.google.com/)
2. Crea una nueva carpeta o selecciona una existente
3. Comparte la carpeta con la cuenta de servicio (opcional)
4. Copia el ID de la carpeta desde la URL:
   ```
   https://drive.google.com/drive/folders/1A2B3C4D5E6F7G8H9I0J
   ```
   El ID es: `1A2B3C4D5E6F7G8H9I0J`

#### Paso 5: Actualizar Configuración

Edita `config/config.json`:

```json
{
  "google_drive": {
    "credentials_path": "credentials.json",
    "token_path": "token.json",
    "folder_id": "1A2B3C4D5E6F7G8H9I0J"
  }
}
```

### Verificación de Integración con Google Drive

```bash
# Activar entorno virtual
source venv/bin/activate

# Probar conexión
python -c "
from src.drive_access import GoogleDriveAccess
import json

with open('config/config.json') as f:
    config = json.load(f)

try:
    drive = GoogleDriveAccess(config['google_drive'])
    docs = drive.get_documents()
    print(f'✓ Conexión exitosa. {len(docs)} documentos encontrados.')
except Exception as e:
    print(f'✗ Error de conexión: {e}')
"
```

## 🔍 Integración con Google Custom Search

### Configuración de Custom Search Engine

#### Paso 1: Crear Motor de Búsqueda

1. Ve a [Custom Search Engine](https://cse.google.com/)
2. Haz clic en "Crear un motor de búsqueda personalizado"
3. Configura:
   - **Nombre**: Business Content Research
   - **Descripción**: Motor para investigación de contenido empresarial
   - **Sitios web a buscar**: deja vacío para búsqueda global
4. Activa "Buscar en toda la web"
5. Crea el motor de búsqueda

#### Paso 2: Obtener Search Engine ID

1. En la página de control del motor, copia el "Search Engine ID"
   ```
   Ejemplo: 012345678901234567890:abcdefghijk
   ```

#### Paso 3: Crear API Key

1. Regresa a [Google Cloud Console](https://console.cloud.google.com/)
2. Ve a "APIs y servicios" → "Credenciales"
3. Haz clic en "Crear credenciales" → "Clave API"
4. Copia la clave generada (formato: `AIzaSyD...`)

#### Paso 4: Actualizar Configuración

```json
{
  "web_search": {
    "api_key": "AIzaSyD1234567890abcdef",
    "search_engine_id": "012345678901234567890:abcdefghijk"
  }
}
```

### Verificación de Integración de Búsqueda

```bash
# Probar búsqueda web
python -c "
from src.web_search import WebSearch
import json

with open('config/config.json') as f:
    config = json.load(f)

try:
    search = WebSearch(config['web_search'])
    results = search.search_related_info(['marketing digital'])
    print(f'✓ Búsqueda exitosa. {len(results)} resultados encontrados.')
except Exception as e:
    print(f'✗ Error de búsqueda: {e}')
"
```

## 🧠 Integración con Modelos de Lenguaje (spaCy)

### Instalación y Configuración

```bash
# Instalar spaCy
pip install spacy

# Descargar modelo en inglés
python -m spacy download en_core_web_sm

# Verificar instalación
python -c "import spacy; nlp = spacy.load('en_core_web_sm'); print('✓ spaCy OK')"
```

### Modelos de Lenguaje Alternativos

Para diferentes idiomas o funcionalidades avanzadas:

```bash
# Español
python -m spacy download es_core_news_sm

# Inglés grande (más preciso, más lento)
python -m spacy download en_core_web_lg

# Modelo transformer (muy preciso, requiere GPU)
python -m spacy download en_core_web_trf
```

### Configuración en el Proyecto

```json
{
  "nlp": {
    "model": "en_core_web_sm",
    "language": "en",
    "pipeline": ["tok2vec", "tagger", "parser", "ner"]
  }
}
```

## 🌐 Integración con Otras APIs de Búsqueda

### Bing Web Search API (Alternativa)

Si prefieres usar Bing en lugar de Google:

1. Regístrate en [Azure Cognitive Services](https://azure.microsoft.com/)
2. Crea un recurso de "Bing Search"
3. Obtén la clave API
4. Modifica `src/web_search.py` para usar Bing API

### SerpApi (Alternativa Premium)

Para búsquedas más avanzadas:

1. Regístrate en [SerpApi](https://serpapi.com/)
2. Obtén tu API key
3. Actualiza la configuración:
```json
{
  "web_search": {
    "provider": "serpapi",
    "api_key": "tu_serpapi_key"
  }
}
```

## 📊 Integración con Bases de Datos

### SQLite (Incluido por defecto)

El agente usa SQLite para almacenamiento local:

```python
import sqlite3

# Conectar a base de datos local
conn = sqlite3.connect('business_agent.db')

# Crear tabla para resultados
conn.execute('''
    CREATE TABLE IF NOT EXISTS analysis_results (
        id INTEGER PRIMARY KEY,
        document_name TEXT,
        key_ideas TEXT,
        analysis_date TIMESTAMP
    )
''')
```

### PostgreSQL (Para producción)

Para entornos de producción:

```bash
# Instalar dependencias
pip install psycopg2-binary

# Configuración
DATABASE_URL = "postgresql://user:password@localhost/business_agent"
```

## 🔒 Integración con Servicios de Almacenamiento

### AWS S3 (Para backups)

```bash
pip install boto3
```

```python
import boto3

# Configurar cliente S3
s3 = boto3.client(
    's3',
    aws_access_key_id='tu_access_key',
    aws_secret_access_key='tu_secret_key'
)

# Subir resultados
s3.upload_file('results.json', 'tu-bucket', 'analysis_results.json')
```

### Google Cloud Storage

```bash
pip install google-cloud-storage
```

```python
from google.cloud import storage

# Configurar cliente
client = storage.Client()
bucket = client.bucket('tu-bucket')

# Subir archivo
blob = bucket.blob('results/analysis.json')
blob.upload_from_filename('results.json')
```

## 📧 Integración con Servicios de Email

### SMTP para Notificaciones

```python
import smtplib
from email.mime.text import MIMEText

def send_notification(email, subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = 'agent@tu-dominio.com'
    msg['To'] = email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('tu-email@gmail.com', 'tu-app-password')
        server.sendmail(msg['From'], msg['To'], msg.as_string())
```

### SendGrid (Servicio profesional)

```bash
pip install sendgrid
```

```python
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

sg = sendgrid.SendGridAPIClient(api_key='tu_sendgrid_key')
# Configurar y enviar email
```

## 🔧 Integración con Herramientas de Desarrollo

### Logging y Monitoreo

```python
import logging
from logging.handlers import RotatingFileHandler

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler('agent.log', maxBytes=10485760, backupCount=5),
        logging.StreamHandler()
    ]
)
```

### Métricas con Prometheus

```bash
pip install prometheus-client
```

```python
from prometheus_client import Counter, Histogram, start_http_server

# Definir métricas
ANALYSIS_TIME = Histogram('analysis_duration_seconds', 'Time spent analyzing')
DOCUMENTS_PROCESSED = Counter('documents_processed_total', 'Documents processed')

# Usar métricas
@ANALYSIS_TIME.time()
def analyze_business():
    # lógica de análisis
    DOCUMENTS_PROCESSED.inc()
```

## 🚀 Integración con Servicios en la Nube

### Docker para Despliegue

Crear `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Descargar modelo spaCy
RUN python -m spacy download en_core_web_sm

EXPOSE 5000

CMD ["python", "main.py"]
```

### Heroku para Hosting

Crear `Procfile`:

```
web: python main.py
```

Configurar variables de entorno en Heroku:

```bash
heroku config:set GOOGLE_DRIVE_FOLDER_ID=tu_folder_id
heroku config:set GOOGLE_SEARCH_API_KEY=tu_api_key
```

### AWS Lambda para Serverless

```python
import json
from src.main import main

def lambda_handler(event, context):
    # Procesar evento
    result = main()
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
```

## 🔄 Integración con APIs Personalizadas

### Crear API REST con Flask

```python
from flask import Flask, request, jsonify
from src.business_analyzer import BusinessAnalyzer

app = Flask(__name__)
analyzer = BusinessAnalyzer()

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    result = analyzer.analyze_business(data['documents'], data['additional_info'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
```

### Webhooks para Notificaciones

```python
import requests

def send_webhook(url, payload):
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        print("✓ Webhook enviado exitosamente")
    except requests.RequestException as e:
        print(f"✗ Error en webhook: {e}")
```

## 📋 Checklist de Integraciones

- [ ] Google Drive API configurada
- [ ] Credenciales OAuth válidas
- [ ] Carpeta de Drive accesible
- [ ] Custom Search API habilitada
- [ ] API Key de búsqueda válida
- [ ] Modelo spaCy descargado
- [ ] Configuración JSON actualizada
- [ ] Pruebas de conexión exitosas
- [ ] Entorno virtual funcionando
- [ ] Backups configurados (opcional)

## 🆘 Solución de Problemas de Integración

### Problema: "Access denied" en Google Drive

**Posibles causas**:
- Credenciales expiradas
- Permisos insuficientes en la carpeta
- API no habilitada

**Soluciones**:
```bash
# Regenerar token
rm token.json
python main.py  # Se volverá a autenticar
```

### Problema: "Quota exceeded" en búsquedas

**Soluciones**:
- Esperar renovación de cuota (diaria)
- Cambiar API key
- Implementar rate limiting
- Usar caché para resultados

### Problema: "Model not found" en spaCy

**Solución**:
```bash
# Forzar descarga
python -m spacy download en_core_web_sm --force

# Verificar instalación
python -c "import spacy; print(spacy.info())"
```

---

**Nota**: Mantén tus claves API seguras y nunca las subas a repositorios públicos. Usa variables de entorno para producción.