<div align="center">
```
  ____      _               _    ___ 
 / ___|   _| |__   ___ _ __/ \  |_ _|
| |  | | | | '_ \ / _ \ '__/ _ \ | | 
| |__| |_| | |_) |  __/ | / ___ \| | 
 \____\__, |_.__/ \___|_|/_/   \_\___|
      |___/                           
```
An intelligent cybersecurity assistant that doesn't just answer — it watches.
<br/>
<p>
<n>What is this?</n>
<n>Cyber AI is a Streamlit-powered chatbot that teaches cybersecurity concepts through an interactive Q&A interface — while simultaneously running a live threat detection layer underneath every conversation.
Ask it about phishing, firewalls, or forensics and it answers like a tutor. Type something flagged — hacking, malware, ransomware, exploit, SQL injection — and the system silently identifies the threat class, logs your IP and geolocation, and still responds with the educational context you asked for. All of this feeds into a real-time admin dashboard that maps and visualizes every flagged interaction.
It's a learning tool with a backbone.</n>
</p>
Features:
1) AI-Powered Responses : Cohere API handles all NLP-driven answers with context awareness
2) Live Keyword Detection : spaCy scans every message for threat-class terms in real time
3) Geo + IP Logging : Flags risky queries and logs the session's IP address and geolocation
4) Admin Dashboard : Threat frequency charts and attack-type breakdowns at a glance
5) Leaflet Attack Map : Interactive world map plotting the origin of all logged threat queries
6) Q&A Learning Mode : Teaches core cybersecurity concepts conversationally — beginner friendly
  
Preview:
Chatbot:
![cyber_bot1](https://github.com/user-attachments/assets/4f4cd44d-ac8b-4a47-b4c2-e5231898da5e)
Admin Panel:
![admin_cyber](https://github.com/user-attachments/assets/70674394-db1c-4200-b669-7858903ff9d2)

Tech stack:
Frontend       →  Streamlit
Backend        →  Python
AI / NLP       →  Cohere API  +  spaCy
Threat Engine  →  Custom keyword classifier
Geo Logging    →  ip-api
Map Layer      →  Leaflet.js (via streamlit-folium)
Data Store     →  JSON log files


How It Works:
User types a message
        │
        ▼
  spaCy scans for threat-class keywords
        │
   ┌────┴────┐
   │ flagged │──► Log IP + Geolocation ──► Update admin dashboard + map
   └────┬────┘
        │
        ▼
  Cohere API generates educational response
        │
        ▼
  Answer displayed to user

  When a keyword like malware, hacking, exploit, DDoS, brute force, or ransomware is detected, the system:

Classifies the threat type
Records the session's IP address and resolves geolocation
Appends to the threat log
Updates the admin map and charts live

The user still gets their answer — they're learning, after all.


📁 Folder Structure
![structure](https://github.com/user-attachments/assets/83748c6d-485f-4e0c-bc3a-d9655d173ecd)

🧪 Try It

Clone repo
Install requirements : *pip install -r requirements.txt*
Run it and  "*Visit http://localhost:5000*"
Notes:
Your .env file must include:OPENAI_API_KEY=your_api_key_here
IP and location are logged for every chat
Meant for educational(learning) & ethical purposes only
<div align="center">
  <sub>Made as part of a B.Tech Cybersecurity project · Ethical use only</sub>
</div>



