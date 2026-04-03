<div align="center">
 
```
  ____      _               _    ___ 
 / ___|   _| |__   ___ _ __/ \  |_ _|
| |  | | | | '_ \ / _ \ '__/ _ \ | | 
| |__| |_| | |_) |  __/ | / ___ \| | 
 \____\__, |_.__/ \___|_|/_/   \_\___|
      |___/                           
```
 
**An intelligent cybersecurity assistant that doesn't just answer — it *watches*.**
 
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Cohere](https://img.shields.io/badge/Cohere_AI-39594A?style=flat-square&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy_NLP-09A3D5?style=flat-square&logoColor=white)
 
</div>
 
---

## What is this?
 
**Cyber AI** is a Streamlit-powered chatbot that teaches cybersecurity concepts through an interactive Q&A interface — while simultaneously running a live threat detection layer underneath every conversation.
 
Ask it about phishing, firewalls, or forensics and it answers like a tutor. Type something flagged — hacking, malware, ransomware, exploit, SQL injection — and the system silently identifies the threat class, logs your IP and geolocation, and still responds with the educational context you asked for. All of this feeds into a real-time admin dashboard that maps and visualizes every flagged interaction.
 
> It's a learning tool with a backbone.
 
---

## Features
 
| Feature | Description |
|---|---|
| **AI-Powered Responses** | Cohere API handles all NLP-driven answers with context awareness |
| **Live Keyword Detection** | spaCy scans every message for threat-class terms in real time |
| **Geo + IP Logging** | Flags risky queries and logs the session's IP address and geolocation |
| **Admin Dashboard** | Threat frequency charts and attack-type breakdowns at a glance |
| **Leaflet Attack Map** | Interactive world map plotting the origin of all logged threat queries |
| **Q&A Learning Mode** | Teaches core cybersecurity concepts conversationally — beginner friendly |
 
---
## Preview:

Chatbot:
![cyber_bot1](https://github.com/user-attachments/assets/4f4cd44d-ac8b-4a47-b4c2-e5231898da5e)
Admin Panel:
![admin_cyber](https://github.com/user-attachments/assets/70674394-db1c-4200-b669-7858903ff9d2)

## Tech Stack
 
```
Frontend       →  Streamlit
Backend        →  Python
AI / NLP       →  Cohere API  +  spaCy
Threat Engine  →  Custom keyword classifier
Geo Logging    →  ip-api
Map Layer      →  Leaflet.js (via streamlit-folium)
Data Store     →  JSON log files
```
 
---

## How It Works

<img width="750" height="522" alt="Screenshot 2026-04-03 162156" src="https://github.com/user-attachments/assets/c1573411-267f-42ab-bb72-556c14af949c" />


When a keyword like `malware`, `hacking`, `exploit`, `DDoS`, `brute force`, or `ransomware` is detected, the system:

- Classifies the threat type
- Records the session's IP address and resolves geolocation
- Appends to the threat log
- Updates the admin map and charts live
 
The user still gets their answer — they're learning, after all.


 Folder Structure
![structure](https://github.com/user-attachments/assets/83748c6d-485f-4e0c-bc3a-d9655d173ecd)

## 🧪 Try It
 
```bash
# Clone the repo
git clone https://github.com/Ree2612/cyber_chatbot.git
cd cyber_chatbot
 
# Install dependencies
pip install -r requirements.txt
 
# Add your Cohere API key
echo "COHERE_API_KEY=your_key_here" > .env
 
# Run
streamlit run app.py
```
 
> IP and location are logged for every flagged chat. Meant for educational and ethical purposes only.
 
---
 
<div align="center">
  <sub>Made as part of a B.Tech Cybersecurity project · Ethical use only</sub>
</div>

