# Solución de Problemas - Business Content Agent

Esta guía proporciona soluciones a problemas comunes que pueden surgir durante la instalación, configuración y uso del Agente de Contenido Empresarial.

## 🔍 Diagnóstico General

### Verificar Estado del Sistema

Ejecuta el script de diagnóstico incluido:

```bash
# Diagnóstico completo
python -c "
import sys
print('=== DIAGNÓSTICO DEL SISTEMA ===')
print(f'Python: {sys.version}')
print(f'Plataforma: {sys.platform}')

# Verificar dependencias críticas
deps = ['spacy', 'flask', 'googleapiclient', 'requests']
for dep in deps:
    try:
        __import__(dep)
        print(f'✓ {dep}')
    except ImportError:
        print(f'✗ {dep} - NO INSTALADO')

# Verificar modelo spaCy
try:
    import spacy
    nlp = spacy.load('en_core_web_sm')
    print('✓ Modelo spaCy en_core_web_sm')
except:
    print('✗ Modelo spaCy NO CARGADO')
"
```

### Logs de Depuración

Habilita logs detallados para diagnóstico:

```bash
# Ejecutar con logs
PYTHONPATH=src python -c "
import logging
logging.basicConfig(level=logging.DEBUG)
from main import main
main()
" 2>&1 | tee debug.log
```

## 🚫 Errores de Instalación

### Error: "ModuleNotFoundError: No module named 'spacy'"

**Síntomas**: Fallo al importar spaCy después de instalación

**Soluciones**:

1. **Verificar entorno virtual**:
```bash
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

2. **Reinstalar spaCy**:
```bash
pip uninstall spacy
pip install spacy
```

3. **Instalar con dependencias del sistema** (Linux):
```bash
sudo apt install build-essential python3-dev
pip install spacy
```

4. **Verificar instalación**:
```bash
python -c "import spacy; print(spacy.__version__)"
```

### Error: "Microsoft Visual C++ 14.0 is required" (Windows)

**Causa**: Falta compilador C++ en Windows

**Soluciones**:

1. **Instalar Build Tools**:
   - Descargar [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
   - Seleccionar "C++ build tools" durante instalación

2. **Usar wheels precompilados**:
```bash
pip install spacy --only-binary=all
```

3. **Usar conda** (alternativa):
```bash
conda install -c conda-forge spacy
```

### Error: "No module named 'googleapiclient'"

**Soluciones**:

```bash
# Instalar Google API client
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

# Verificar instalación
python -c "from googleapiclient.discovery import build; print('✓ Google API OK')"
```

## 🔐 Errores de Autenticación

### Error: "Access denied" con Google Drive

**Códigos de error comunes**:
- `access_denied`
- `invalid_client`
- `redirect_uri_mismatch`

**Soluciones paso a paso**:

1. **Verificar credenciales**:
```bash
# Comprobar que credentials.json existe
ls -la credentials.json

# Validar formato JSON
python -c "import json; json.load(open('credentials.json')); print('✓ JSON válido')"
```

2. **Regenerar token de acceso**:
```bash
# Eliminar token antiguo
rm token.json

# Forzar re-autenticación
python main.py
```

3. **Verificar configuración de OAuth**:
   - Ir a [Google Cloud Console](https://console.cloud.google.com/)
   - APIs y servicios → Credenciales
   - Verificar URIs de redireccionamiento
   - Confirmar alcances (scopes) correctos

4. **Comprobar permisos de carpeta**:
   - Abrir Google Drive
   - Verificar que la carpeta está compartida (si es necesario)
   - Confirmar que la cuenta tiene acceso de lectura

### Error: "invalid_grant" en autenticación

**Causa**: Token expirado o revocado

**Solución**:
```bash
# Eliminar tokens antiguos
rm -f token.json *.pickle

# Re-autenticar
python main.py
```

### Error: "Daily quota exceeded" en Custom Search

**Soluciones**:

1. **Verificar uso de cuota**:
   - Ir a [Google Cloud Console](https://console.cloud.google.com/)
   - APIs y servicios → Cuotas
   - Revisar uso de "Custom Search API"

2. **Implementar rate limiting**:
```python
import time

def search_with_rate_limit(query):
    # Limitar a 1 búsqueda por segundo
    time.sleep(1)
    return search_api.search(query)
```

3. **Usar caché para resultados**:
```python
from functools import lru_cache

@lru_cache(maxsize=100)
def cached_search(query):
    return search_api.search(query)
```

## 📄 Errores de Procesamiento de Documentos

### Error: "Unsupported file type" en Google Drive

**Causa**: El agente solo procesa archivos de texto

**Archivos soportados**:
- `.txt`, `.md`, `.docx`, `.pdf` (texto extraíble)

**Solución**:
```python
# Ver archivos en carpeta
from src.drive_access import GoogleDriveAccess

drive = GoogleDriveAccess(config)
docs = drive.get_documents()
for doc in docs:
    print(f"{doc['name']}: {doc['type']}")
```

### Error: "Empty document" o "No content extracted"

**Posibles causas**:
- Archivo corrupto
- Codificación incorrecta
- Contenido no textual (imágenes, etc.)

**Diagnóstico**:
```python
# Verificar contenido de documentos
from src.drive_access import GoogleDriveAccess

drive = GoogleDriveAccess(config)
docs = drive.get_documents()

for doc in docs:
    content = doc.get('content', '')
    print(f"{doc['name']}: {len(content)} caracteres")
    if len(content) < 100:
        print(f"Contenido: {content[:200]}...")
```

## 🧠 Errores de Procesamiento de Lenguaje Natural

### Error: "Can't find model 'en_core_web_sm'"

**Soluciones**:

1. **Descargar modelo**:
```bash
python -m spacy download en_core_web_sm
```

2. **Verificar instalación**:
```bash
python -c "import spacy; spacy.cli.info()"
```

3. **Forzar descarga**:
```bash
python -m spacy download en_core_web_sm --force
```

### Error: "Model version mismatch"

**Solución**: Actualizar spaCy y modelos
```bash
pip install -U spacy
python -m spacy validate
```

### Error: "MemoryError" en procesamiento de texto largo

**Soluciones**:

1. **Procesar en lotes**:
```python
def process_large_text(text, batch_size=100000):
    batches = [text[i:i+batch_size] for i in range(0, len(text), batch_size)]
    results = []
    for batch in batches:
        doc = nlp(batch)
        results.extend(extract_entities(doc))
    return results
```

2. **Optimizar pipeline de spaCy**:
```python
# Deshabilitar componentes no necesarios
nlp = spacy.load('en_core_web_sm', disable=['parser', 'tagger'])
```

## 🌐 Errores de Conexión y Red

### Error: "Connection timeout" en búsquedas web

**Soluciones**:

1. **Aumentar timeout**:
```python
import requests

response = requests.get(url, timeout=30)  # 30 segundos
```

2. **Implementar reintentos**:
```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def requests_retry_session(retries=3):
    session = requests.Session()
    retry = Retry(total=retries, backoff_factor=0.3)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session
```

3. **Verificar conectividad**:
```bash
# Probar conexión a Google
curl -I https://www.googleapis.com

# Verificar DNS
nslookup www.googleapis.com
```

### Error: "SSL certificate verify failed"

**Soluciones**:

1. **Actualizar certificados**:
```bash
# macOS
brew install openssl
export SSL_CERT_FILE=/usr/local/etc/openssl/cert.pem

# Linux
sudo apt install ca-certificates
```

2. **Deshabilitar verificación SSL** (solo desarrollo):
```python
requests.get(url, verify=False)
```

## 💾 Errores de Memoria y Rendimiento

### Error: "MemoryError" en documentos grandes

**Soluciones**:

1. **Procesar archivos en chunks**:
```python
def process_file_in_chunks(file_path, chunk_size=1024*1024):
    with open(file_path, 'r') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            process_chunk(chunk)
```

2. **Usar generadores** para procesamiento lazy:
```python
def read_large_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()
```

### Rendimiento lento

**Optimizaciones**:

1. **Usar multiprocessing**:
```python
from multiprocessing import Pool

def process_documents_parallel(documents):
    with Pool(processes=4) as pool:
        results = pool.map(process_single_document, documents)
    return results
```

2. **Implementar caché**:
```python
from functools import lru_cache

@lru_cache(maxsize=500)
def cached_analysis(text):
    return analyze_text(text)
```

## 🔄 Errores de Iteración y Feedback

### Error: "Maximum recursion depth exceeded"

**Causa**: Bucles infinitos en iteración de feedback

**Solución**: Implementar límite de iteraciones
```python
MAX_ITERATIONS = 5
iteration_count = 0

while feedback and feedback.get('improve', False) and iteration_count < MAX_ITERATIONS:
    # lógica de mejora
    iteration_count += 1
```

### Error: "Feedback format invalid"

**Validar formato de feedback**:
```python
def validate_feedback(feedback):
    required_fields = ['rating', 'improvements']
    for field in required_fields:
        if field not in feedback:
            raise ValueError(f"Campo requerido faltante: {field}")
    return True
```

## 🚀 Errores de Despliegue

### Error: "Port already in use" en Flask

**Soluciones**:

1. **Matar proceso existente**:
```bash
# Encontrar proceso
lsof -i :5000

# Matar proceso
kill -9 <PID>
```

2. **Cambiar puerto**:
```python
app.run(port=5001)  # Puerto alternativo
```

### Error: "Permission denied" en archivos de log

**Soluciones**:

1. **Verificar permisos**:
```bash
ls -la logs/
chmod 755 logs/
```

2. **Cambiar ubicación de logs**:
```python
import tempfile
log_file = os.path.join(tempfile.gettempdir(), 'agent.log')
```

## 📊 Monitoreo y Alertas

### Configurar logging avanzado

```python
import logging
from logging.handlers import RotatingFileHandler, SMTPHandler

# File handler con rotación
file_handler = RotatingFileHandler('agent.log', maxBytes=10485760, backupCount=5)
file_handler.setLevel(logging.INFO)

# Email handler para errores críticos
mail_handler = SMTPHandler(
    mailhost=('smtp.gmail.com', 587),
    fromaddr='agent@tu-dominio.com',
    toaddrs=['admin@tu-dominio.com'],
    subject='Error Crítico - Business Content Agent',
    credentials=('tu-email@gmail.com', 'tu-password'),
    secure=()
)
mail_handler.setLevel(logging.ERROR)

# Configurar logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[file_handler, mail_handler, logging.StreamHandler()]
)
```

### Métricas de rendimiento

```python
import time
import psutil

class PerformanceMonitor:
    def __init__(self):
        self.start_time = time.time()

    def get_metrics(self):
        return {
            'uptime': time.time() - self.start_time,
            'cpu_percent': psutil.cpu_percent(),
            'memory_percent': psutil.virtual_memory().percent,
            'disk_usage': psutil.disk_usage('/').percent
        }

# Uso
monitor = PerformanceMonitor()
metrics = monitor.get_metrics()
print(f"Uptime: {metrics['uptime']:.2f}s, CPU: {metrics['cpu_percent']}%, RAM: {metrics['memory_percent']}%")
```

## 🆘 Contacto y Soporte

Si los problemas persisten después de seguir esta guía:

### Información a proporcionar en reportes de bug:

1. **Entorno del sistema**:
   ```bash
   python --version
   pip list | grep -E "(spacy|flask|google)"
   uname -a  # Linux/macOS
   systeminfo  # Windows
   ```

2. **Logs completos**:
   ```bash
   # Ejecutar con logging completo
   PYTHONPATH=src python main.py 2>&1 | tee full_debug.log
   ```

3. **Configuración (sin credenciales)**:
   ```json
   {
     "google_drive": {"folder_id": "ID_PRESENTE"},
     "web_search": {"search_engine_id": "ID_PRESENTE"},
     "nlp": {"model": "en_core_web_sm"}
   }
   ```

4. **Pasos para reproducir** el error

### Canales de soporte:
- 📧 Email: support@business-content-agent.com
- 🐛 Issues: [GitHub Issues](https://github.com/tu-repo/issues)
- 📖 Foro: [Comunidad](https://community.business-content-agent.com)

---

**Nota**: Esta guía se actualiza regularmente. Para problemas no cubiertos aquí, consulta la documentación más reciente en el repositorio oficial.