# Ejemplos de Uso - Business Content Agent

Esta guía proporciona ejemplos prácticos de cómo usar el Agente de Contenido Empresarial en diferentes escenarios y casos de uso.

## 🚀 Inicio Rápido

### Ejemplo 1: Análisis Básico de Negocio

```bash
# 1. Preparar documentos en Google Drive
# Crear carpeta "Business_Analysis" en Google Drive
# Subir documentos: plan_negocio.pdf, analisis_mercado.docx, estrategia_marketing.txt

# 2. Configurar el agente
# Editar config/config.json con tus credenciales

# 3. Ejecutar análisis
source venv/bin/activate
python main.py

# Resultado: 40 ideas de contenido audiovisual generadas
```

### Ejemplo 2: Investigación de Mercado Automatizada

```python
from src.business_analyzer import BusinessAnalyzer
from src.web_search import WebSearch
import json

# Cargar configuración
with open('config/config.json') as f:
    config = json.load(f)

# Analizar negocio
analyzer = BusinessAnalyzer()
business_data = {
    'full_text': 'Empresa de tecnología especializada en IA para marketing digital',
    'key_ideas': ['marketing automation', 'machine learning', 'customer insights'],
    'entities': ['marketing', 'tecnología', 'IA'],
    'topics': [('marketing', 10), ('tecnología', 8), ('IA', 6)]
}

analysis = analyzer.analyze_business(business_data, [])

# Buscar información adicional
search = WebSearch(config['web_search'])
additional_info = search.search_related_info(['marketing automation 2024', 'AI marketing trends'])

print(f"Análisis completado. Información adicional: {len(additional_info)} resultados")
```

## 📊 Casos de Uso Detallados

### Caso 1: Startup de E-commerce

**Objetivo**: Generar contenido para lanzar un nuevo producto

**Documentos requeridos**:
- Descripción del producto
- Análisis de competencia
- Perfil del cliente ideal
- Estrategia de precios

**Configuración específica**:
```json
{
  "google_drive": {
    "folder_id": "1ABC123..."
  },
  "audience_profile": {
    "age_range": "25-45",
    "interests": ["compras online", "productos innovadores"],
    "platforms": ["Instagram", "TikTok", "YouTube"]
  }
}
```

**Resultado esperado**:
- 40 ideas de videos cortos para redes sociales
- Contenido enfocado en beneficios del producto
- Enfoque en audiencia millennial/Gen Z

### Caso 2: Consultoría Empresarial

**Objetivo**: Crear contenido educativo sobre transformación digital

**Documentos requeridos**:
- Casos de estudio
- Tendencias del mercado
- Metodologías de consultoría
- Testimonios de clientes

**Script de automatización**:
```python
from src.script_generator import ScriptGenerator
from src.audience_analyzer import AudienceAnalyzer

# Analizar audiencia B2B
audience = AudienceAnalyzer()
profile = audience.analyze_audience({
    'structure': {'industry': 'consulting', 'business_type': 'B2B'},
    'market_position': {'target_market': 'empresas medianas'}
})

# Generar contenido educativo
generator = ScriptGenerator()
ideas = generator.generate_ideas(
    business_analysis={'industry': 'consulting'},
    audience_profile=profile,
    count=40
)

# Filtrar por formato educativo
educational_content = [idea for idea in ideas
                      if 'educational' in idea['format'] or 'tutorial' in idea['format']]

print(f"Generadas {len(educational_content)} ideas educativas")
```

### Caso 3: Restaurante Familiar

**Objetivo**: Aumentar presencia local y atracción de clientes

**Documentos requeridos**:
- Menú y especialidades
- Historia del restaurante
- Opiniones de clientes
- Información de ubicación

**Enfoque de contenido**:
- Videos de preparación de platos
- Historias de la familia
- Testimonios de clientes locales
- Contenido estacional

```python
# Configuración para negocio local
config_local = {
    'tone': 'casual',
    'language': 'storytelling',
    'cultural_elements': ['tradición familiar', 'cocina local'],
    'communication_preferences': ['video content', 'social media']
}

ideas_local = generator.generate_ideas(
    business_analysis={'business_type': 'restaurant', 'location': 'local'},
    audience_profile=config_local,
    count=40
)
```

## 🔧 Scripts de Automatización

### Script 1: Análisis Semanal Automático

```python
#!/usr/bin/env python3
"""
Script para análisis semanal automático de contenido
"""
import schedule
import time
from datetime import datetime
from src.main import main

def weekly_analysis():
    """Ejecutar análisis semanal"""
    print(f"Iniciando análisis semanal: {datetime.now()}")
    try:
        main()
        print("✓ Análisis semanal completado")
    except Exception as e:
        print(f"✗ Error en análisis semanal: {e}")

# Programar ejecución semanal
schedule.every().monday.at("09:00").do(weekly_analysis)

# Ejecutar indefinidamente
while True:
    schedule.run_pending()
    time.sleep(60)
```

### Script 2: Generador de Contenido por Lotes

```python
#!/usr/bin/env python3
"""
Generar contenido para múltiples temas empresariales
"""
from src.script_generator import ScriptGenerator
from src.audience_analyzer import AudienceAnalyzer
import json

def generate_bulk_content(themes, audience_profiles):
    """Generar contenido para múltiples temas"""

    generator = ScriptGenerator()
    analyzer = AudienceAnalyzer()

    all_ideas = []

    for theme in themes:
        for profile_name, profile_config in audience_profiles.items():

            # Analizar perfil de audiencia
            audience_profile = analyzer.analyze_audience(profile_config)

            # Generar ideas
            ideas = generator.generate_ideas(
                business_analysis={'theme': theme},
                audience_profile=audience_profile,
                count=20  # 20 ideas por combinación
            )

            # Agregar metadata
            for idea in ideas:
                idea['theme'] = theme
                idea['audience_profile'] = profile_name

            all_ideas.extend(ideas)

    return all_ideas

# Configuración de temas y audiencias
themes = ['innovación tecnológica', 'sostenibilidad', 'transformación digital']
audience_profiles = {
    'millennials': {'demographics': {'age_group': '25-40'}},
    'empresas': {'structure': {'business_type': 'B2B'}},
    'consumidores': {'communication_preferences': ['social media']}
}

# Generar contenido
bulk_content = generate_bulk_content(themes, audience_profiles)
print(f"Generadas {len(bulk_content)} ideas de contenido")
```

### Script 3: Sistema de Feedback Iterativo

```python
#!/usr/bin/env python3
"""
Sistema avanzado de feedback y mejora iterativa
"""
from src.script_generator import ScriptGenerator
from src.ui import UserInterface
import json

class ContentOptimizer:
    """Optimizador de contenido con feedback"""

    def __init__(self):
        self.generator = ScriptGenerator()
        self.feedback_history = []

    def optimize_content(self, initial_ideas, max_iterations=3):
        """Optimizar contenido basado en feedback"""

        current_ideas = initial_ideas
        iteration = 0

        while iteration < max_iterations:
            print(f"\n--- Iteración {iteration + 1} ---")

            # Presentar ideas al usuario
            ui = UserInterface({'ui': {'port': 5000}})
            selected_ideas, feedback = ui.present_ideas_and_get_feedback(current_ideas)

            if not feedback or not feedback.get('improve', False):
                print("Usuario satisfecho con los resultados")
                break

            # Aplicar mejoras
            current_ideas = self._apply_improvements(selected_ideas, feedback)
            self.feedback_history.append(feedback)

            iteration += 1

        return current_ideas, self.feedback_history

    def _apply_improvements(self, ideas, feedback):
        """Aplicar mejoras basadas en feedback"""

        improved_ideas = []

        for idea in ideas:
            improved = idea.copy()

            # Aplicar cambios de tono
            if 'tone_change' in feedback:
                improved['description'] = improved['description'].replace(
                    idea.get('tone', ''), feedback['tone_change']
                )

            # Aplicar cambios de formato
            if 'format_change' in feedback:
                improved['format'] = feedback['format_change']

            # Agregar elementos adicionales
            if 'additional_elements' in feedback:
                improved['key_elements'].extend(feedback['additional_elements'])

            improved_ideas.append(improved)

        return improved_ideas

# Uso del optimizador
optimizer = ContentOptimizer()

# Generar ideas iniciales
initial_ideas = generator.generate_ideas(
    business_analysis={'industry': 'technology'},
    audience_profile={'tone': 'professional'},
    count=10
)

# Optimizar con feedback
optimized_ideas, history = optimizer.optimize_content(initial_ideas)

print(f"Optimización completada. {len(history)} iteraciones de feedback.")
```

## 📈 Métricas y Análisis de Resultados

### Script de Evaluación de Contenido

```python
#!/usr/bin/env python3
"""
Evaluar calidad y efectividad del contenido generado
"""
import json
from collections import Counter, defaultdict

def analyze_content_quality(ideas):
    """Analizar calidad del contenido generado"""

    # Métricas básicas
    metrics = {
        'total_ideas': len(ideas),
        'formats': Counter(idea['format'] for idea in ideas),
        'themes': Counter(idea['theme'] for idea in ideas),
        'platforms': Counter(platform for idea in ideas
                           for platform in idea.get('target_platforms', [])),
        'avg_duration': sum(len(idea['description'].split()) for idea in ideas) / len(ideas)
    }

    # Análisis de diversidad
    unique_titles = len(set(idea['title'] for idea in ideas))
    metrics['title_uniqueness'] = unique_titles / len(ideas)

    # Cobertura de plataformas
    all_platforms = set()
    for idea in ideas:
        all_platforms.update(idea.get('target_platforms', []))
    metrics['platform_coverage'] = len(all_platforms)

    return metrics

def generate_content_report(ideas, output_file='content_report.json'):
    """Generar reporte completo de contenido"""

    metrics = analyze_content_quality(ideas)

    # Análisis por categorías
    category_analysis = defaultdict(list)
    for idea in ideas:
        category = idea.get('theme', 'uncategorized')
        category_analysis[category].append(idea)

    report = {
        'summary': metrics,
        'categories': dict(category_analysis),
        'recommendations': generate_recommendations(metrics),
        'generated_at': str(datetime.now())
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    return report

def generate_recommendations(metrics):
    """Generar recomendaciones basadas en métricas"""

    recommendations = []

    if metrics['title_uniqueness'] < 0.8:
        recommendations.append("Mejorar diversidad de títulos para evitar repetición")

    if metrics['platform_coverage'] < 3:
        recommendations.append("Expandir cobertura de plataformas sociales")

    if metrics['avg_duration'] < 50:
        recommendations.append("Desarrollar contenido más detallado")

    format_counts = metrics['formats']
    dominant_format = max(format_counts, key=format_counts.get)
    if format_counts[dominant_format] > len(metrics) * 0.6:
        recommendations.append(f"Demasiado contenido en formato '{dominant_format}'. Diversificar formatos.")

    return recommendations

# Uso del sistema de evaluación
ideas = load_generated_ideas()  # Cargar ideas generadas
report = generate_content_report(ideas)
print("Reporte generado:", report['summary'])
```

## 🔄 Integración con Herramientas Externas

### Exportar a Hootsuite/Trello

```python
import requests

def export_to_hootsuite(ideas, api_key, social_profiles):
    """Exportar ideas a Hootsuite para programación"""

    hootsuite_posts = []

    for idea in ideas[:10]:  # Primeras 10 ideas
        post = {
            'text': f"{idea['title']}\n\n{idea['description'][:200]}...",
            'socialProfileIds': social_profiles,
            'scheduledSendTime': None,  # Programar manualmente
            'media': []  # Agregar URLs de medios si existen
        }
        hootsuite_posts.append(post)

    # API call a Hootsuite
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.post(
        'https://platform.hootsuite.com/v1/messages',
        json=hootsuite_posts,
        headers=headers
    )

    return response.json()
```

### Integración con Canva

```python
def generate_canva_templates(ideas):
    """Generar plantillas para Canva"""

    templates = []

    for idea in ideas:
        template = {
            'name': idea['title'],
            'description': idea['description'],
            'format': idea['format'],
            'dimensions': get_dimensions_for_format(idea['format']),
            'elements': [
                {'type': 'text', 'content': idea['title'], 'position': 'center'},
                {'type': 'text', 'content': idea['description'][:100], 'position': 'bottom'}
            ]
        }
        templates.append(template)

    return templates

def get_dimensions_for_format(format_type):
    """Obtener dimensiones óptimas para cada formato"""

    dimensions = {
        'instagram_post': {'width': 1080, 'height': 1080},
        'youtube_thumbnail': {'width': 1280, 'height': 720},
        'twitter_post': {'width': 1200, 'height': 675},
        'linkedin_post': {'width': 1200, 'height': 627}
    }

    return dimensions.get(format_type, {'width': 1080, 'height': 1080})
```

## 📋 Casos de Uso Avanzados

### 1. Campaña de Lanzamiento de Producto

```python
# Configuración para lanzamiento
launch_config = {
    'business_analysis': {
        'product_name': 'Nuevo Software',
        'target_market': 'PYMEs',
        'unique_selling_points': ['fácil uso', 'precio competitivo', 'soporte 24/7']
    },
    'audience_profile': {
        'tone': 'professional',
        'language': 'persuasive',
        'communication_preferences': ['video content', 'social media']
    },
    'campaign_timeline': '4 semanas',
    'content_mix': {
        'educational': 0.4,
        'testimonial': 0.3,
        'product_demo': 0.3
    }
}

# Generar calendario de contenido
content_calendar = generate_launch_calendar(launch_config)
```

### 2. Rebranding Corporativo

```python
# Análisis de cambio de marca
rebrand_analysis = {
    'old_brand': 'Marca Antigua',
    'new_brand': 'Nueva Identidad',
    'key_messages': ['innovación', 'sostenibilidad', 'confianza'],
    'stakeholders': ['empleados', 'clientes', 'socios']
}

# Generar contenido de transición
transition_content = generate_rebrand_content(rebrand_analysis)

# Crear plan de comunicación interna
internal_comms = generate_internal_communications(rebrand_analysis)
```

### 3. Expansión Internacional

```python
# Configuración multi-idioma
international_config = {
    'markets': ['México', 'Colombia', 'Chile'],
    'languages': ['es', 'es-CO', 'es-CL'],
    'cultural_adaptations': {
        'México': ['tradición', 'familia'],
        'Colombia': ['innovación', 'café'],
        'Chile': ['naturaleza', 'emprendimiento']
    }
}

# Generar contenido localizado
localized_content = generate_multilingual_content(international_config)
```

## 🎯 Mejores Prácticas

### Optimización de Resultados

1. **Preparar documentos de calidad**: Asegurar que los documentos en Google Drive contengan información relevante y actualizada

2. **Configurar audiencias específicas**: Definir perfiles de audiencia detallados para contenido más preciso

3. **Iterar con feedback**: Usar el sistema de feedback para refinar resultados

4. **Monitorear métricas**: Rastrear rendimiento del contenido generado

### Escalabilidad

1. **Procesamiento por lotes**: Dividir grandes volúmenes de contenido en lotes manejables

2. **Caché inteligente**: Implementar caché para búsquedas y análisis repetitivos

3. **Paralelización**: Usar múltiples procesos para análisis concurrente

### Mantenimiento

1. **Actualizar dependencias**: Mantener bibliotecas actualizadas regularmente

2. **Monitorear cuotas**: Controlar uso de APIs para evitar límites

3. **Backup de configuraciones**: Mantener copias de seguridad de configuraciones críticas

---

**Nota**: Estos ejemplos pueden adaptarse según necesidades específicas. Para casos de uso personalizados, consulta la documentación de la API o contacta al soporte técnico.