# AI-Based Cyber Threat Detection System (Encrypted Data)

**Authors:** Arsalan Khatri, Obaid Sheikh Ahmed, & Muhammad Talha Panhwar | Sindh Madressatul Islam University (SMIU)[cite: 13, 14]

## Project Overview
This project is an advanced, privacy-preserving Intrusion Detection System (IDS) designed to detect hidden cyber threats within encrypted network traffic[cite: 13]. Instead of decrypting payloads—which compromises user privacy and increases computational overhead—this system analyzes behavioral and statistical flow-based features to identify malicious activities with high precision[cite: 13]. 

## 🚀 Core Features
*   **Robust Data Engineering:** Consolidated multiple raw CSV files into unified datasets, performed extensive data cleaning (removing nulls, empty values, and duplicates), and applied min-max scaling for optimal model training[cite: 13].
*   **Novel Hybrid AI Architecture:** Engineered a two-stage hybrid model utilizing a Deep Learning Autoencoder for intelligent feature extraction and dimensionality reduction, paired with an XGBoost classifier for highly accurate threat detection[cite: 13].
*   **Comprehensive Model Evaluation:** Trained and evaluated multiple ML (XGBoost, Random Forest) and DL (CNN, LSTM) models, achieving up to **98.62% accuracy** on the CIC-IDS-2017 dataset and **99.23% accuracy** on the UNSW-NB15 dataset[cite: 13].
*   **Scalable Backend (Django):** Built a robust backend using Django and Django REST Framework to expose prediction endpoints and manage real-time data flow[cite: 13].
*   **Dynamic Web Dashboard:** Developed an interactive WordPress frontend that consumes Django APIs to display a Live Threat Detection Dashboard, visualizing network traffic, attack ratios, and model confidence scores dynamically.
*   **LLM-Powered Threat Advisory:** Integrated a custom LLM API that analyzes the prediction outputs (Entropy, Margin, Confidence) and provides actionable, human-readable mitigation strategies to security analysts[cite: 13].
*   **AI Cyber Expert Chatbot:** Deployed a dedicated AI-driven chatbot interface to answer cybersecurity-related queries and guide users on threat protection in real-time[cite: 13].

## Datasets Used
*   **CIC-IDS-2017:** Analyzed over 2.8 million entries covering 14 modern attack vectors (e.g., DDoS, Botnet, Brute Force, Web Attacks)[cite: 13].
*   **UNSW-NB15:** Utilized for cross-dataset generalization, featuring 49 flow-based features and 9 distinct attack categories[cite: 13].

## Technology Stack
*   **AI & Machine Learning:** XGBoost, Autoencoders, Scikit-Learn, TensorFlow/Keras, Prompt Engineering[cite: 13].
*   **LLM Integration:** OpenAI GPT-4 / Custom LLM APIs[cite: 13].
*   **Backend:** Python, Django, Django REST Framework[cite: 13].
*   **Frontend:** WordPress, HTML/CSS, JavaScript, AJAX[cite: 13].
*   **Deployment:** Ubuntu Virtual Machine (Cloud), Nginx, Gunicorn[cite: 13].

## System Workflow
1. **Data Upload:** User uploads network traffic data (CSV) via the WordPress frontend.
2. **API Processing:** Data is sent to the Django backend where it is cleaned, preprocessed, and scaled.
3. **Hybrid Prediction:** The Autoencoder extracts key features, and the XGBoost model classifies the traffic as `Benign` or `Attack`.
4. **LLM Analysis:** If an attack is detected, the metrics are sent to the LLM API to generate specific mitigation advice.
5. **Dashboard Render:** Results, charts, and AI suggestions are instantly rendered on the user's screen.
