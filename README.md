🛡️ Cybersecurity-Aware AI Chatbot
A smart, interactive AI-powered chatbot that detects cybersecurity threats in real-time, logs user data for analysis, and helps users understand common security risks — all with a modern, glassmorphic UI and location tracking!

📸 Preview
Chatbot:
![cyber_bot1](https://github.com/user-attachments/assets/4f4cd44d-ac8b-4a47-b4c2-e5231898da5e)
Admin Panel:
![admin_cyber](https://github.com/user-attachments/assets/70674394-db1c-4200-b669-7858903ff9d2)

🚀 Features:

✅ ChatGPT-powered fallback for intelligent answers
🧠 Built-in cyber threat detection (e.g., phishing, ransomware, XSS)
🌐 IP and location tracking with map-based admin dashboard (Leaflet.js)
📍 Geolocation + country flags for each user
🧾 Admin panel with live log viewer and "Clear Logs" feature
🎨 Clean cyber-themed UI with typing animation, sound, and responsive design
🔒 Useful for demos, educational tools, or awareness training

🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: Flask (Python)
NLP: spaCy + OpenAI GPT-3.5 Turbo
IP Geolocation: ip-api.com
Map Visualization: Leaflet.js
UI Styling: Glassmorphic + Orbitron font + custom chatbot bubbles

📁 Folder Structure
cyber_chatbot/
│
├── templates/
│   ├── index.html          # Chatbot interface
│   └── admin.html          # Admin log/map view
│
├── static/
│   └── sounds/ping.mp3     # Bot reply sound
│
├── chatbot_logic.py        # Bot brain (spaCy + OpenAI)
├── back.py                 # Flask backend
├── logs.csv                # Stores IP logs & chat queries
├── threat_log.txt          # Plain text log
├── requirements.txt        # Dependencies
├── .env                    # API key (not shared!)

🧪 Try It
Clone repo
Install requirements
pip install -r requirements.txt
Run
Visit http://localhost:5000

⚠️ Notes
Your .env file must include:OPENAI_API_KEY=your_api_key_here
IP and location are logged for every chat
Meant for educational & ethical purposes only


