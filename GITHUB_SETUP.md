# 🚀 Guía para Subir Obliquo Automatizacion a GitHub

Esta guía te ayudará a subir el proyecto Obliquo Automatizacion a GitHub de manera segura y profesional.

## 📋 Prerrequisitos

- ✅ Cuenta de GitHub
- ✅ Git instalado en tu sistema
- ✅ Proyecto Obliquo Automatizacion configurado
- ✅ Credenciales de Google APIs (NO subir a GitHub)

## 🔐 Preparación del Repositorio

### Paso 1: Crear Repositorio en GitHub

1. Ve a [GitHub.com](https://github.com) y haz login
2. Haz clic en el botón **"New repository"** (botón verde)
3. Configura el repositorio:
   - **Repository name**: `obliquo-automatizacion` o `Obliquo-Automatizacion`
   - **Description**: `Agente automatizado que analiza información empresarial y genera ideas de contenido audiovisual`
   - **Visibility**: `Public` (público) o `Private` (privado)
   - ❌ **NO marques** "Add a README file" (ya tenemos uno)
   - ❌ **NO marques** "Add .gitignore" (ya tenemos uno)
   - ✅ **SI marca** "Add a license" (recomiendo MIT)

4. Haz clic en **"Create repository"**

### Paso 2: Preparar el Proyecto Local

```bash
# Navegar al directorio del proyecto
cd obliquo-automatizacion

# Verificar que Git esté inicializado
ls -la .git

# Si no existe .git, inicializar repositorio
git init
```

### Paso 3: Configurar Git (Primera vez)

```bash
# Configurar tu identidad
git config --global user.name "Tu Nombre Completo"
git config --global user.email "tu-email@ejemplo.com"

# Verificar configuración
git config --list
```

### Paso 4: Preparar Archivos para Commit

```bash
# Ver qué archivos están en el directorio
ls -la

# Verificar .gitignore está funcionando
git status

# Deberías ver que credentials.json, token.json, y config.json están ignorados
```

### Paso 5: Crear Commit Inicial

```bash
# Agregar todos los archivos (excepto los ignorados)
git add .

# Ver qué se va a commitear
git status

# Crear commit inicial
git commit -m "🚀 Initial commit: Obliquo Automatizacion

- Agente automatizado para análisis empresarial
- Integración con Google Drive y Custom Search
- Procesamiento NLP con spaCy
- Generación de 40 ideas de contenido audiovisual
- Documentación completa en español
- Sistema de feedback iterativo"
```

## 📤 Subir a GitHub

### Paso 6: Conectar con Repositorio Remoto

```bash
# Agregar el repositorio remoto (reemplaza TU_USUARIO y NOMBRE_REPO)
git remote add origin https://github.com/TU_USUARIO/NOMBRE_REPO.git

# Verificar conexión
git remote -v
```

### Paso 7: Subir el Código

```bash
# Subir la rama main
git push -u origin main

# Si tu rama principal se llama master, usa:
# git push -u origin master
```

### Paso 8: Verificar Subida

1. Ve a tu repositorio en GitHub
2. Deberías ver todos los archivos del proyecto
3. ✅ Los archivos sensibles deberían estar ausentes (.gitignore funcionando)
4. ✅ Deberías ver el README principal
5. ✅ La documentación debería estar en la carpeta `docs/`

## 🏷️ Etiquetas y Releases

### Crear Primera Release

1. Ve a la pestaña **"Releases"** en tu repositorio
2. Haz clic en **"Create a new release"**
3. Configura:
   - **Tag version**: `v1.0.0`
   - **Release title**: `Versión 1.0.0 - Lanzamiento Inicial`
   - **Describe this release**:
     ```
     🎉 Primera versión completa del Business Content Agent

     ✨ Características principales:
     - Análisis topológico de negocios
     - Integración con Google Drive
     - Generación de 40 ideas de contenido
     - Sistema de feedback iterativo
     - Documentación completa en español

     📚 Documentación: https://github.com/TU_USUARIO/NOMBRE_REPO/blob/main/README_ES.md
     🛠️ Instalación: https://github.com/TU_USUARIO/NOMBRE_REPO/blob/main/docs/GUIA_INSTALACION.md
     ```

4. Haz clic en **"Publish release"**

## 🔒 Seguridad y Mejores Prácticas

### Archivos que NUNCA debes subir

❌ **NUNCA subas estos archivos:**
- `credentials.json` (credenciales de Google)
- `token.json` (tokens de acceso)
- `config/config.json` (configuración con claves API)
- `.env` (variables de entorno)
- Archivos con contraseñas o claves

### Verificación de Seguridad

```bash
# Ver qué archivos están siendo rastreados
git ls-files

# Ver si hay archivos sensibles
git ls-files | grep -E "(credentials|token|config\.json|\.env)"

# Si aparecen archivos sensibles, removerlos
git rm --cached archivo_sensible.json
git commit -m "Remove sensitive file from tracking"
```

### Configuración de Branch Protection

1. Ve a **Settings** → **Branches** en tu repositorio
2. Haz clic en **"Add rule"**
3. Configura:
   - **Branch name pattern**: `main` o `master`
   - ✅ **Require pull request reviews**
   - ✅ **Require status checks**
   - ✅ **Restrict pushes**

## 📝 Actualizaciones Futuras

### Flujo de Trabajo para Updates

```bash
# Crear rama para nueva feature
git checkout -b feature/nueva-funcionalidad

# Hacer cambios y commits
git add .
git commit -m "Add nueva funcionalidad"

# Subir rama
git push origin feature/nueva-funcionalidad

# Crear Pull Request en GitHub
# Después de merge, actualizar main
git checkout main
git pull origin main
```

### Mantener Documentación Actualizada

```bash
# Actualizar documentación
git add docs/
git commit -m "docs: Update installation guide"

# Crear nueva release para versiones importantes
# Settings → Releases → Create new release
```

## 🌟 Mejores Prácticas para GitHub

### Estructura del Repositorio
```
obliquo-agente1-analisis/
├── 📁 docs/              # Documentación completa
├── 📁 src/               # Código fuente
├── 📁 config/            # Configuración (template)
├── 🔒 .gitignore         # Archivos ignorados
├── 📖 README_ES.md       # Documentación principal
├── 🧪 test_*.py          # Scripts de prueba
└── 🐍 main.py           # Punto de entrada
```

### Badges y Shields
Agrega estos badges al README:

```markdown
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/docs-completa-green.svg)](docs/INDICE_DOCUMENTACION.md)
```

### Temas y Etiquetas
- **Topics**: `python`, `nlp`, `business-intelligence`, `content-generation`, `google-drive`, `automation`
- **Etiquetas**: `hacktoberfest`, `first-timers`, `help-wanted`

## 🚨 Solución de Problemas

### Error: "Repository not found"

```bash
# Verificar URL del repositorio
git remote -v

# Corregir URL si es necesario
git remote set-url origin https://github.com/TU_USUARIO/CORRECTO_REPO.git
```

### Error: "Permission denied"

```bash
# Verificar credenciales
git config --global credential.helper

# Usar token de acceso personal
# GitHub → Settings → Developer settings → Personal access tokens
```

### Error: "Non-fast-forward"

```bash
# Sincronizar con repositorio remoto
git pull origin main --rebase

# O forzar push (cuidado!)
git push origin main --force-with-lease
```

## 📊 Métricas y SEO

### Optimización para GitHub
- ✅ **README atractivo** con badges y screenshots
- ✅ **Descripción clara** en el repositorio
- ✅ **Temas relevantes** para discoverability
- ✅ **Documentación completa** para credibilidad
- ✅ **Licencia clara** para contribuidores

### Métricas a Monitorear
- ⭐ **Stars**: Popularidad del proyecto
- 🍴 **Forks**: Interés de contribuidores
- 👀 **Watchers**: Seguidores activos
- 🐛 **Issues**: Problemas reportados
- 🔀 **Pull Requests**: Contribuciones

## 🎯 Próximos Pasos

Después de subir a GitHub:

1. ✅ **Compartir el enlace** con la comunidad
2. ✅ **Crear issues** para futuras mejoras
3. ✅ **Configurar CI/CD** (GitHub Actions)
4. ✅ **Agregar contribuidores** al proyecto
5. ✅ **Monitorear feedback** de usuarios

---

**¡Felicitaciones!** Tu Obliquo Automatizacion ahora está disponible en GitHub. Recuerda mantener la documentación actualizada y responder a issues de manera oportuna para construir una comunidad activa.

📧 **¿Necesitas ayuda?** Crea un issue en el repositorio o contacta al equipo de desarrollo.