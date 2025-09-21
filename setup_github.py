#!/usr/bin/env python3
"""
Script de ayuda para configurar el proyecto para GitHub
Obliquo Automatizacion - GitHub Setup Assistant
"""

import os
import shutil
import json
from pathlib import Path

def main():
    """Asistente de configuración para GitHub"""

    print("🚀 Obliquo Automatizacion - GitHub Setup Assistant")
    print("=" * 60)

    project_root = Path(__file__).parent

    # Verificar estructura del proyecto
    print("\n📁 Verificando estructura del proyecto...")
    required_files = [
        'README_ES.md',
        'requirements.txt',
        'main.py',
        '.gitignore',
        'LICENSE',
        'GITHUB_SETUP.md',
        'setup_github.py'
    ]

    missing_files = []
    for file in required_files:
        if not (project_root / file).exists():
            missing_files.append(file)

    if missing_files:
        print(f"❌ Archivos faltantes: {', '.join(missing_files)}")
        return False
    else:
        print("✅ Estructura del proyecto correcta")

    # Verificar archivos sensibles
    print("\n🔒 Verificando seguridad...")
    sensitive_files = [
        'credentials.json',
        'token.json',
        'config/config.json'
    ]

    exposed_files = []
    for file in sensitive_files:
        if (project_root / file).exists():
            exposed_files.append(file)

    if exposed_files:
        print(f"⚠️  ADVERTENCIA: Archivos sensibles encontrados: {', '.join(exposed_files)}")
        print("   Estos archivos NO deberían subirse a GitHub")
        print("   Asegúrate de que estén en .gitignore")

        response = input("   ¿Quieres ver el contenido de .gitignore? (y/n): ").lower()
        if response == 'y':
            gitignore_path = project_root / '.gitignore'
            if gitignore_path.exists():
                with open(gitignore_path, 'r') as f:
                    print("\n   Contenido de .gitignore:")
                    print("   " + "-" * 40)
                    for line in f:
                        print(f"   {line.rstrip()}")
                    print("   " + "-" * 40)
            else:
                print("   ❌ .gitignore no encontrado")

    # Crear template de configuración si no existe
    config_template = project_root / 'config' / 'config.template.json'
    config_real = project_root / 'config' / 'config.json'

    if not config_template.exists() and config_real.exists():
        print("\n📋 Creando template de configuración...")
        shutil.copy(config_real, config_template)

        # Limpiar datos sensibles del template
        with open(config_template, 'r') as f:
            config_data = json.load(f)

        # Reemplazar valores sensibles
        if 'google_drive' in config_data:
            config_data['google_drive']['folder_id'] = 'TU_FOLDER_ID_DE_GOOGLE_DRIVE_AQUI'

        if 'web_search' in config_data:
            config_data['web_search']['api_key'] = 'TU_CLAVE_DE_API_DE_GOOGLE_SEARCH_AQUI'
            config_data['web_search']['search_engine_id'] = 'TU_ID_DE_MOTOR_DE_BUSQUEDA_AQUI'

        with open(config_template, 'w', encoding='utf-8') as f:
            json.dump(config_data, f, indent=2, ensure_ascii=False)

        print("✅ Template de configuración creado: config/config.template.json")

    # Verificar documentación
    print("\n📖 Verificando documentación...")
    docs_dir = project_root / 'docs'
    doc_files = [
        'GUIA_INSTALACION.md',
        'GUIA_INTEGRACIONES.md',
        'SOLUCION_PROBLEMAS.md',
        'EJEMPLOS_USO.md',
        'INDICE_DOCUMENTACION.md'
    ]

    missing_docs = []
    for doc in doc_files:
        if not (docs_dir / doc).exists():
            missing_docs.append(doc)

    if missing_docs:
        print(f"⚠️  Documentos faltantes: {', '.join(missing_docs)}")
    else:
        print("✅ Documentación completa")

    # Preparar comandos Git
    print("\n🔧 Comandos recomendados para GitHub:")
    print("   1. Crear repositorio en GitHub")
    print("   2. Ejecutar los siguientes comandos:")
    print()
    print("   cd \"Obliquo Automatizacion\"")
    print("   git init")
    print("   git add .")
    print("   git commit -m \"🚀 Initial commit: Obliquo Automatizacion\"")
    print("   git branch -M main")
    print("   git remote add origin https://github.com/TU_USUARIO/NOMBRE_REPO.git")
    print("   git push -u origin main")
    print()
    print("   3. Crear primera release en GitHub")
    print("   4. Configurar branch protection rules")

    # Checklist final
    print("\n📋 Checklist de verificación:")
    checks = [
        ("✅ README principal presente", (project_root / 'README_ES.md').exists()),
        ("✅ Licencia MIT presente", (project_root / 'LICENSE').exists()),
        (".gitignore configurado", (project_root / '.gitignore').exists()),
        ("✅ Dependencias listadas", (project_root / 'requirements.txt').exists()),
        ("✅ Script principal presente", (project_root / 'main.py').exists()),
        ("✅ Tests incluidos", (project_root / 'test_imports.py').exists()),
        ("✅ Documentación completa", docs_dir.exists() and len(list(docs_dir.glob('*.md'))) >= 5),
        ("✅ Archivos sensibles protegidos", not any((project_root / f).exists() for f in ['credentials.json', 'token.json'])),
    ]

    for check, status in checks:
        status_icon = "✅" if status else "❌"
        print(f"   {status_icon} {check}")

    print("\n🎯 Próximos pasos:")
    print("   1. Revisar y ajustar .gitignore si es necesario")
    print("   2. Crear repositorio en GitHub")
    print("   3. Ejecutar comandos Git mostrados arriba")
    print("   4. Configurar GitHub Actions para CI/CD (opcional)")
    print("   5. Crear primera release")

    print("\n📚 Recursos adicionales:")
    print("   📖 Guía completa: GITHUB_SETUP.md")
    print("   🐛 Issues: Reportar problemas en GitHub")
    print("   💬 Comunidad: Discusiones en GitHub")

    print("\n✨ ¡Tu proyecto está listo para GitHub!")

if __name__ == "__main__":
    main()