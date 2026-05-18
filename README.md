# 🚀 Crypto Market ETL Pipeline

## 📌 Project Overview
This project is an end-to-end Crypto Data Pipeline built using Python.

The pipeline extracts live cryptocurrency market data from the CoinGecko API, transforms and cleans the data, stores it in a SQLite database, and visualizes market trends.

---

## 🛠 Technologies Used
- Python
- Pandas
- Requests
- SQLite
- Matplotlib

---

## ⚡ Features
- Real-time Crypto API Integration
- Data Cleaning & Transformation
- Database Storage
- Automated ETL Workflow
- Data Visualization

---

## 📂 Project Structure

```bash
CryptoPipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── visualize.py
│   └── main.py
│
├── crypto.db
├── requirements.txt
└── README.md