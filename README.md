# BiodivProScope 🌿

**AI-powered biodiversity risk assessment platform for New Jersey hotel compliance**

BiodivProScope helps hotels understand and mitigate their environmental impact by analyzing biodiversity risks within a 5-mile radius of any property — combining real government datasets, geospatial analysis, and a Retrieval-Augmented Generation (RAG) system to generate actionable, regulation-cited mitigation strategies.

Originally developed as a graduate capstone project at Montclair State University, sponsored by the university's Environmental Department.

---

## 🎯 What It Does

1. A hotel enters its New Jersey zip code
2. The system geocodes the location and scans a 5-mile radius
3. Environmental risk data is pulled from 6+ real datasets (invasive species, IUCN threatened species, freshwater/marine/terrestrial pollution indices)
4. Risks are scored, classified (High / Moderate / Low), and visualized on an interactive map
5. A RAG-powered mitigation engine generates specific, regulation-cited recommendations for each risk
6. Reports export as PDF, CSV, or Excel

---

## 🏗️ Architecture
**Risk scoring pipeline:**
---

## 🛠️ Tech Stack

| Layer | Technologies |
|---|---|
| **Frontend** | React 18, Material UI, React Leaflet, Framer Motion, jsPDF |
| **Backend** | Python, Flask, Flask-Session |
| **Database** | PostgreSQL + PostGIS |
| **AI / RAG** | ChromaDB, SentenceTransformers (all-MiniLM-L6-v2) |
| **ML** | Random Forest (mitigation strategy classification), AHP (Analytic Hierarchy Process) risk weighting |
| **Geospatial** | Haversine formula, Nominatim geocoding API |

---

## 📊 Data Sources

- NJ Department of Environmental Protection — Invasive Species Sightings (14,500+ records, 1879–2024)
- NJ Invasive Species Strike Team — Species control recommendations
- IUCN Red List — Global threatened species data
- World Bank — Freshwater / Marine / Terrestrial Human Coexistence Index
- NJ DEP — Drinking water systems and nutrient monitoring
- NJ DEP — Real-time water quality monitoring (83 estuary stations)

---

## ✨ Key Features

- 🗺️ Interactive risk map with clustered markers and custom risk-type icons
- 🤖 AI-generated mitigation strategies with regulation citations (NJDEP, IUCN guidelines)
- 📄 Exportable reports (PDF / CSV / Excel)
- 🔐 User authentication with encrypted sessions
- 🏨 Multi-location management for hotel chains

---

## 🚀 Local Setup

**Requirements:** Python 3.10+, Node.js 16+, PostgreSQL 14+ with PostGIS, Git

```bash
# Clone the repo
git clone https://github.com/aldemirgozde/biodivproscope-ml.git
cd biodivproscope-ml

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Create your .env file (see .env.example)
cp .env.example .env
# then fill in your DB credentials

python app.py  # runs on http://localhost:5000

# Frontend setup (in a new terminal)
cd frontend
npm install
npm start  # runs on http://localhost:3000
```

---

## 📄 Research

This project is the subject of an ongoing research submission to the CESAC (Clean Energy and Sustainability Analytics Center) journal at Montclair State University.

---

## 👥 Team

Developed by graduate students at Montclair State University's School of Computing:
Gozde Aldemir, Nivas Reddy Pannala, Rahul Ega, Devendra Sakhamuri, Lokesh Reddy Janga

Faculty sponsors: Dr. Pankaj Lal, Dr. Manveer Mann (Montclair State University Environmental Department / CESAC)

---

## 📌 Note

This repository is an independently maintained portfolio version of the original team capstone project, restructured and deployed by Gozde Aldemir.
