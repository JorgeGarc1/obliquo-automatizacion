# Agente de Contenido Empresarial

Un agente automatizado inteligente desarrollado en Python que analiza información empresarial desde repositorios de Google Drive, realiza análisis topológico de negocios y genera 40 ideas de guiones para contenido audiovisual adaptadas al público objetivo.

## 🚀 Características Principales

- **Integración con Google Drive**: Acceso automático a documentos empresariales
- **Procesamiento de Texto con IA**: Extracción de contexto e ideas clave usando NLP avanzado
- **Investigación Web Automática**: Búsqueda de información adicional relevante
- **Análisis Topológico Empresarial**: Evaluación profunda de estructura y relaciones de negocio
- **Análisis de Audiencia**: Determinación de tono, lenguaje y elementos culturales óptimos
- **Generación de Ideas Creativas**: Creación de 40 conceptos únicos para contenido audiovisual
- **Interfaz Interactiva**: Presentación de ideas con sistema de retroalimentación iterativa
- **Arquitectura Modular**: Diseño escalable y mantenible

## 📋 Tabla de Contenidos

- [Requisitos del Sistema](#requisitos-del-sistema)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Guía de Integraciones](#guía-de-integraciones)
- [Uso del Agente](#uso-del-agente)
- [Arquitectura del Sistema](#arquitectura-del-sistema)
- [Solución de Problemas](#solución-de-problemas)
- [Soporte y Contribución](#soporte-y-contribución)

## 💻 Requisitos del Sistema

### Requisitos Mínimos
- **Python**: 3.8 o superior
- **Sistema Operativo**: macOS, Linux, o Windows
- **Memoria RAM**: 4GB mínimo, 8GB recomendado
- **Espacio en Disco**: 2GB para instalación y modelos de IA

### Dependencias Externas
- Cuenta de Google con Google Drive
- Credenciales de Google Cloud Platform
- Conexión a internet para investigación web

## 🛠️ Instalación

### Paso 1: Clonar o Descargar el Proyecto

```bash
# Si tienes Git instalado
git clone <url-del-repositorio>
cd business_content_agent

# O descarga y extrae el archivo ZIP
unzip business_content_agent.zip
cd business_content_agent
```

### Paso 2: Crear Entorno Virtual

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate  # En macOS/Linux
# venv\Scripts\activate   # En Windows
```

### Paso 3: Instalar Dependencias

```bash
# Instalar todas las dependencias
pip install -r requirements.txt

# Descargar modelo de lenguaje de spaCy
python -m spacy download en_core_web_sm
```

### Paso 4: Verificar Instalación

```bash
# Ejecutar pruebas de importación
python test_imports.py

# Ejecutar pruebas funcionales
python test_main.py
```

Si ambas pruebas pasan exitosamente, la instalación está completa.

## ⚙️ Configuración

### Archivo de Configuración Principal

Edita el archivo `config/config.json`:

```json
{
  "google_drive": {
    "credentials_path": "credentials.json",
    "token_path": "token.json",
    "folder_id": "TU_FOLDER_ID_DE_GOOGLE_DRIVE"
  },
  "web_search": {
    "api_key": "TU_CLAVE_DE_API_DE_GOOGLE_SEARCH",
    "search_engine_id": "TU_ID_DE_MOTOR_DE_BUSQUEDA"
  },
  "nlp": {
    "model": "en_core_web_sm"
  },
  "ui": {
    "port": 5000
  }
}
```

### Configuración de Google Drive API

#### Paso 1: Crear Proyecto en Google Cloud Console

1. Ve a [Google Cloud Console](https://console.cloud.google.com/)
2. Crea un nuevo proyecto o selecciona uno existente
3. Habilita la API de Google Drive

#### Paso 2: Crear Credenciales OAuth 2.0

1. Ve a "Credenciales" en el menú lateral
2. Haz clic en "Crear credenciales" → "ID de cliente OAuth"
3. Configura la pantalla de consentimiento OAuth:
   - Tipo de usuario: Externo
   - Nombre de la aplicación: Business Content Agent
   - Correo de soporte: tu-email@ejemplo.com
4. Agrega alcances (scopes): `https://www.googleapis.com/auth/drive.readonly`
5. Descarga el archivo JSON de credenciales como `credentials.json`
6. Coloca el archivo en la raíz del proyecto

#### Paso 3: Obtener ID de Carpeta de Google Drive

1. Abre Google Drive en tu navegador
2. Crea o selecciona la carpeta con documentos empresariales
3. Copia el ID de la carpeta desde la URL:
   ```
   https://drive.google.com/drive/folders/FOLDER_ID_AQUI
   ```
4. Actualiza el `folder_id` en `config.json`

### Configuración de Google Custom Search API

#### Paso 1: Habilitar la API

1. En Google Cloud Console, habilita "Custom Search JSON API"
2. Crea credenciales de API Key

#### Paso 2: Crear Motor de Búsqueda Personalizado

1. Ve a [Custom Search Engine](https://cse.google.com/)
2. Crea un nuevo motor de búsqueda
3. Configura el alcance de búsqueda (opcional)
4. Obtén el "Search Engine ID"

#### Paso 3: Actualizar Configuración

```json
{
  "web_search": {
    "api_key": "AIzaSyD...tu_clave_aqui",
    "search_engine_id": "012345678901234567890:abcdefghijk"
  }
}
```

## 🔗 Guía de Integraciones

### Integración con Google Drive

El agente se conecta automáticamente a Google Drive usando OAuth 2.0:

```python
from src.drive_access import GoogleDriveAccess

config = {
    "credentials_path": "credentials.json",
    "token_path": "token.json",
    "folder_id": "tu_folder_id"
}

drive_access = GoogleDriveAccess(config)
documents = drive_access.get_documents()
```

**Nota**: La primera ejecución requerirá autenticación manual en el navegador.

### Integración con APIs de Búsqueda Web

```python
from src.web_search import WebSearch

config = {
    "api_key": "tu_api_key",
    "search_engine_id": "tu_search_engine_id"
}

search = WebSearch(config)
results = search.search_related_info(["marketing digital", "estrategia de contenido"])
```

### Integración con Modelos de Lenguaje (spaCy)

```python
from src.text_processor import TextProcessor

processor = TextProcessor({"model": "en_core_web_sm"})
processed_data = processor.process_documents(documents)
```

## 🎯 Uso del Agente

### Ejecución Básica

```bash
# Activar entorno virtual
source venv/bin/activate

# Ejecutar el agente
python main.py
```

### Flujo de Trabajo del Agente

1. **Acceso a Documentos**: Conecta con Google Drive y descarga documentos
2. **Procesamiento de Texto**: Extrae contexto e ideas clave usando NLP
3. **Investigación Web**: Busca información adicional relevante
4. **Solicitud de Información**: Pide datos adicionales si es necesario
5. **Análisis Empresarial**: Realiza análisis topológico del negocio
6. **Análisis de Audiencia**: Determina características del público objetivo
7. **Generación de Ideas**: Crea 40 conceptos para contenido audiovisual
8. **Presentación y Retroalimentación**: Muestra ideas y recopila feedback

### Interfaz Web

Para usar la interfaz web completa:

```python
from src.ui import UserInterface
import json

with open('config/config.json') as f:
    config = json.load(f)

ui = UserInterface(config['ui'])
ui.run_web_app()  # Accede en http://localhost:5000
```

### Modo Consola Interactivo

El agente incluye un modo consola para selección manual de ideas:

```
Script Ideas Generated
========================================
ID: 1
Title: How Digital Marketing Changed Everything
Format: educational video
Theme: success story
Description: This educational video explores success story...
Duration: 3-5 minutes
Platforms: YouTube, LinkedIn, Website

Select this idea? (y/n): y
```

## 🏗️ Arquitectura del Sistema

```
business_content_agent/
├── config/
│   └── config.json          # Configuraciones del sistema
├── src/
│   ├── drive_access.py      # Integración Google Drive
│   ├── text_processor.py    # Procesamiento NLP
│   ├── web_search.py        # Búsqueda web
│   ├── form_handler.py      # Manejo de formularios
│   ├── business_analyzer.py # Análisis empresarial
│   ├── audience_analyzer.py # Análisis de audiencia
│   ├── script_generator.py  # Generación de ideas
│   └── ui.py                # Interfaz de usuario
├── main.py                  # Punto de entrada principal
├── requirements.txt         # Dependencias Python
├── test_imports.py          # Pruebas de importación
├── test_main.py            # Pruebas funcionales
└── README_ES.md            # Esta documentación
```

### Componentes Principales

| Componente | Responsabilidad | Tecnologías |
|------------|----------------|-------------|
| `drive_access` | Acceso a Google Drive | Google API Client |
| `text_processor` | Análisis de texto | spaCy, NLP |
| `web_search` | Investigación web | Google Custom Search |
| `business_analyzer` | Lógica de negocio | Algoritmos propietarios |
| `audience_analyzer` | Perfiles de audiencia | Análisis heurístico |
| `script_generator` | Creación de contenido | Plantillas dinámicas |
| `ui` | Interfaz usuario | Flask, HTML/CSS/JS |

## 🔧 Solución de Problemas

### Problemas Comunes

#### Error: "ModuleNotFoundError"

**Síntoma**: ImportError al ejecutar el agente

**Solución**:
```bash
# Asegurarse de que el entorno virtual esté activado
source venv/bin/activate

# Reinstalar dependencias
pip install -r requirements.txt

# Verificar instalación
python test_imports.py
```

#### Error: "Google Drive Authentication Failed"

**Síntoma**: Fallo en la conexión con Google Drive

**Soluciones**:
1. Verificar que `credentials.json` existe y es válido
2. Eliminar `token.json` y volver a autenticar
3. Verificar permisos de la carpeta en Google Drive
4. Confirmar que la API de Google Drive está habilitada

#### Error: "spaCy Model Not Found"

**Síntoma**: Error al cargar modelo de lenguaje

**Solución**:
```bash
# Descargar modelo específico
python -m spacy download en_core_web_sm

# Verificar instalación
python -c "import spacy; spacy.load('en_core_web_sm')"
```

#### Error: "Web Search API Quota Exceeded"

**Síntoma**: Límite de API de búsqueda alcanzado

**Soluciones**:
1. Esperar a que se renueve la cuota (diaria)
2. Cambiar la clave API
3. Reducir la frecuencia de búsquedas en el código

### Logs y Depuración

Para habilitar logs detallados:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Verificación del Entorno

Ejecuta las pruebas incluidas:

```bash
# Pruebas de importación
python test_imports.py

# Pruebas funcionales
python test_main.py
```

## 📞 Soporte y Contribución

### Canales de Soporte

- **Documentación**: Consulta esta guía completa
- **Issues**: Reporta problemas en el repositorio del proyecto
- **Discussions**: Participa en debates de la comunidad

### Reportar Problemas

Al reportar un problema, incluye:

1. **Descripción clara** del problema
2. **Pasos para reproducir** el error
3. **Logs completos** del error
4. **Versión de Python** y sistema operativo
5. **Configuración relevante** (sin credenciales sensibles)

### Contribuir al Proyecto

1. Fork el repositorio
2. Crea una rama para tu feature: `git checkout -b feature/nueva-funcionalidad`
3. Realiza tus cambios siguiendo las guías de estilo
4. Agrega pruebas para nuevas funcionalidades
5. Envía un Pull Request

### Guías de Desarrollo

- **Estilo de Código**: PEP 8
- **Documentación**: Docstrings en inglés
- **Pruebas**: Incluir pruebas unitarias para nuevas funciones
- **Commits**: Mensajes descriptivos en inglés

## 📄 Licencia

Este proyecto está disponible bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## 🙏 Agradecimientos

- **spaCy** por el procesamiento de lenguaje natural
- **Google** por las APIs de Drive y Custom Search
- **Comunidad Open Source** por las bibliotecas utilizadas

---

**Versión**: 1.0.0
**Última actualización**: Diciembre 2024
**Autor**: Business Content Agent Team