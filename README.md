# SHL Assessment Recommender System 🎯

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green.svg)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25-red.svg)](https://streamlit.io)

An intelligent recommendation system that helps hiring managers quickly find relevant SHL assessments using natural language queries.

![Demo Screenshot](https://via.placeholder.com/800x400?text=SHL+Recommender+Demo)

## ✨ Features
- **Natural Language Search**: Input job descriptions or keywords
- **Smart Filtering**: 
  - Duration limits (10-120 minutes)
  - Remote testing availability
  - Adaptive/IRT support status
- **Top 10 Recommendations**: Ordered by relevance
- **Mock Data Included**: 15+ sample assessments

## 🛠 Tech Stack
| Component       | Technology                          |
|-----------------|-------------------------------------|
| Backend         | FastAPI + Uvicorn                   |
| Frontend        | Streamlit                           |
| Data Handling   | Pandas                              |
| Deployment      | Render (API) + Streamlit Cloud (UI) |

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip package manager

### Installation
```bash
git clone https://github.com/yourusername/SHL-Assessment-Recommender
cd SHL-Assessment-Recommender
pip install -r requirements.txt
