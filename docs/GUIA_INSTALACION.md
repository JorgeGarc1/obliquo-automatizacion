# Guía de Instalación - Business Content Agent

Esta guía proporciona instrucciones detalladas paso a paso para instalar y configurar el Agente de Contenido Empresarial en diferentes sistemas operativos.

## 📋 Requisitos Previos

### Sistema Operativo
- **macOS**: 10.15 o superior
- **Linux**: Ubuntu 18.04+, CentOS 7+, Debian 9+
- **Windows**: 10 o superior (con WSL recomendado)

### Software Base
- **Python**: Versión 3.8 a 3.11
- **Git**: Para clonar el repositorio
- **pip**: Gestor de paquetes de Python (incluido con Python 3.4+)

### Verificación de Requisitos

```bash
# Verificar versión de Python
python3 --version

# Verificar pip
python3 -m pip --version

# Verificar git (opcional)
git --version
```

## 🚀 Instalación Automática (Recomendado)

### Paso 1: Descargar el Proyecto

```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/business-content-agent.git
cd business-content-agent

# O descargar ZIP y extraer
# wget https://github.com/tu-usuario/business-content-agent/archive/main.zip
# unzip main.zip
# cd business-content-agent-main
```

### Paso 2: Ejecutar Instalador Automático

```bash
# Hacer ejecutable el script de instalación
chmod +x install.sh

# Ejecutar instalación
./install.sh
```

El script de instalación automáticamente:
- ✅ Verifica requisitos del sistema
- ✅ Crea entorno virtual
- ✅ Instala todas las dependencias
- ✅ Descarga modelos de IA
- ✅ Ejecuta pruebas de verificación

## 🛠️ Instalación Manual

Si prefieres instalar manualmente o el script automático falla:

### Paso 1: Crear Entorno Virtual

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### Paso 2: Actualizar pip

```bash
python -m pip install --upgrade pip
```

### Paso 3: Instalar Dependencias Core

```bash
# Instalar dependencias básicas
pip install requests flask beautifulsoup4

# Instalar dependencias de Google
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

# Instalar spaCy y modelo de lenguaje
pip install spacy
python -m spacy download en_core_web_sm
```

### Paso 4: Instalar Dependencias Adicionales

```bash
# Instalar dependencias restantes
pip install pandas openpyxl python-dotenv
```

### Paso 5: Verificar Instalación

```bash
# Ejecutar pruebas
python test_imports.py
python test_main.py
```

## 🔧 Instalación en Diferentes Sistemas

### macOS con Homebrew

```bash
# Instalar Python si no está disponible
brew install python@3.11

# Instalar dependencias del sistema
brew install openssl readline sqlite3 xz zlib

# Proceder con instalación normal
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Ubuntu/Debian Linux

```bash
# Instalar Python y pip si no están disponibles
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Instalar dependencias del sistema para spaCy
sudo apt install build-essential

# Proceder con instalación normal
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### CentOS/RHEL Linux

```bash
# Instalar Python 3.8+
sudo yum install python38 python38-pip python38-devel

# O usando dnf en CentOS 8+
sudo dnf install python38 python38-pip python38-devel

# Instalar herramientas de desarrollo
sudo yum groupinstall "Development Tools"

# Proceder con instalación normal
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Windows con PowerShell

```powershell
# Instalar Python desde Microsoft Store o python.org
# Crear entorno virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Windows con WSL (Recomendado)

```bash
# Instalar WSL2
wsl --install

# En WSL, proceder como Ubuntu
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 📁 Estructura Post-Instalación

Después de la instalación exitosa, deberías tener:

```
business_content_agent/
├── venv/                    # Entorno virtual
├── src/                     # Código fuente
├── config/                  # Archivos de configuración
├── docs/                    # Documentación
├── test_imports.py          # Pruebas de importación
├── test_main.py            # Pruebas funcionales
├── main.py                 # Script principal
└── requirements.txt        # Dependencias
```

## ✅ Verificación de Instalación

### Prueba Básica

```bash
# Activar entorno virtual
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Verificar Python
python --version

# Verificar importaciones
python -c "import spacy, flask, googleapiclient; print('✓ Dependencias OK')"
```

### Prueba de Funcionalidad

```bash
# Ejecutar pruebas incluidas
python test_imports.py
python test_main.py
```

### Prueba de Componentes Individuales

```bash
# Probar spaCy
python -c "import spacy; nlp = spacy.load('en_core_web_sm'); print('✓ spaCy OK')"

# Probar Flask
python -c "from flask import Flask; print('✓ Flask OK')"

# Probar Google API (sin credenciales)
python -c "from googleapiclient.discovery import build; print('✓ Google API OK')"
```

## 🔄 Actualización del Sistema

Para actualizar el agente a una nueva versión:

```bash
# Activar entorno virtual
source venv/bin/activate

# Actualizar código
git pull origin main

# Actualizar dependencias
pip install -r requirements.txt --upgrade

# Actualizar modelo de spaCy si es necesario
python -m spacy download en_core_web_sm --force

# Ejecutar pruebas
python test_imports.py
python test_main.py
```

## 🐛 Solución de Problemas de Instalación

### Error: "python3: command not found"

**Solución**: Instalar Python 3
```bash
# macOS
brew install python@3.11

# Ubuntu/Debian
sudo apt install python3 python3-pip

# CentOS
sudo yum install python38
```

### Error: "ModuleNotFoundError" después de instalación

**Solución**: Verificar entorno virtual
```bash
# Asegurarse de activar el entorno virtual
source venv/bin/activate

# Reinstalar dependencias
pip install -r requirements.txt
```

### Error: "spaCy model not found"

**Solución**: Descargar modelo manualmente
```bash
source venv/bin/activate
python -m spacy download en_core_web_sm
```

### Error: "Permission denied" en instalación

**Solución**: Usar `--user` o verificar permisos
```bash
# Opción 1: Instalar para usuario actual
pip install --user -r requirements.txt

# Opción 2: Usar sudo (no recomendado)
sudo pip install -r requirements.txt
```

### Error: "SSL module not available"

**Solución**: Reinstalar Python con SSL
```bash
# macOS con Homebrew
brew reinstall python@3.11

# Linux - instalar dependencias SSL
sudo apt install libssl-dev
```

## 📞 Soporte de Instalación

Si encuentras problemas durante la instalación:

1. **Verifica los logs** de error completos
2. **Ejecuta las pruebas** de verificación
3. **Comprueba la versión** de Python y pip
4. **Revisa los requisitos** del sistema
5. **Consulta la documentación** de troubleshooting

Para soporte adicional, crea un issue en el repositorio con:
- Sistema operativo y versión
- Versión de Python
- Log completo del error
- Pasos que seguiste

---

**Nota**: Esta guía se actualiza regularmente. Para la versión más reciente, consulta el repositorio oficial.