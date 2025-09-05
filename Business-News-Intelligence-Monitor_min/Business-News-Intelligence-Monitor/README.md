# Agente de Monitoreo de Noticias  — Ejemplo 1 (Sección 4.0.1)

Este repositorio contiene el código correspondiente al **Ejemplo 1** del Trabajo de Fin de Grado *Exploración de sistemas multi-agente en IA generativa*:  
**Agente de Monitoreo de Noticias (Búsqueda y Análisis de Insights Ejecutivos)**.

El sistema implementa una pipeline de agentes con dos roles principales:

- **Researcher** → se encarga de buscar y recolectar información en distintas fuentes.  
- **Analyst** → sintetiza la información recolectada en un informe ejecutivo con citas a las fuentes.  

Este ejemplo acompaña la **Sección 4.0.1** de la memoria y la figura que ilustra la arquitectura de monitoreo de noticias.

---

## 📂 Estructura del repositorio

- `src/business_news_intelligence_monitor/`
  - `main.py` → punto de entrada del sistema  
  - `crew.py` → definición de la crew y orquestación de los agentes  
  - `config/agents.yaml` → configuración de agentes (roles, objetivos)  
  - `config/tasks.yaml` → configuración de tareas asignadas  
  - `tools/` → herramientas personalizadas usadas por los agentes  
- `knowledge/` → prompts o preferencias auxiliares  
- `pyproject.toml` → metadatos del proyecto  
- `requirements.txt` → dependencias mínimas (para instalación con `pip`)  
- `.env.example` → plantilla de credenciales y claves API  
- `.gitignore` → exclusiones recomendadas (para no subir `.env`, `.venv`, cachés, etc.)

---

## ⚙️ Instalación y uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/matiasgarciar/Latest-AI-Development.git
   cd Latest-AI-Development/Business-News-Intelligence-Monitor

2. **(Opcional) Crear un entorno virtual:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt

4.**Configurar variables de entorno:**
   ```bash
   cp .env.example .env
Después edita el archivo .env y añade tus claves:

   ```ini

   OPENAI_API_KEY=sk-...
   SERPER_API_KEY=...

5. **Ejecutar el sistema:**
   ```bash

python src/business_news_intelligence_monitor/main.py \
  --company "Tesla" \
  --date_from "2025-08-01" \
  --date_to "2025-08-31"
