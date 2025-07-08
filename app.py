from flask import Flask, render_template, request, jsonify, redirect
from chatbot_logic import get_bot_response
import logging
from datetime import datetime
import requests
import csv
import os

app = Flask(__name__)
logging.basicConfig(filename="threat_log.txt", level=logging.INFO)

# --- Geolocation Function ---
def get_geolocation(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}")
        data = res.json()
        return {
            "ip": ip,
            "city": data.get("city"),
            "region": data.get("regionName"),
            "country": data.get("country"),
            "countryCode": data.get("countryCode"),
            "isp": data.get("isp"),
            "lat": data.get("lat"),
            "lon": data.get("lon"),
        }
    except:
        return {
            "ip": ip, "city": None, "region": None, "country": None,
            "countryCode": None, "isp": None, "lat": None, "lon": None
        }

# --- Routes ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_msg = request.json.get("message")
   # Accurate IP detection logic for Flask
    if request.remote_addr == "127.0.0.1":
    # You're testing locally, so fetch your actual public IP
     user_ip = requests.get("https://api64.ipify.org").text
    else:
    # On real server, use the real IP directly
     user_ip = request.remote_addr


    geo = get_geolocation(user_ip)
    bot_reply, is_threat, threat_terms = get_bot_response(user_msg)

    log_msg = (
        f"[{datetime.now()}] IP: {user_ip} | Location: {geo['city']}, {geo['country']} "
        f"| ISP: {geo['isp']} | Msg: {user_msg} | Threat: {is_threat} | Terms: {', '.join(threat_terms)}"
    )
    logging.info(log_msg)

    with open("logs.csv", "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now(), user_ip, geo['city'], geo['region'], geo['country'],
            geo['countryCode'], geo['lat'], geo['lon'], geo['isp'], user_msg,
            is_threat, "|".join(threat_terms)
        ])

    return jsonify({
        "reply": bot_reply,
        "threat_detected": is_threat,
        "threats": threat_terms
    })


@app.route("/admin")
def admin_panel():
    entries = []
    if os.path.exists("logs.csv"):
        with open("logs.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 12:
                    entries.append({
                        "timestamp": row[0],
                        "ip": row[1],
                        "city": row[2],
                        "region": row[3],
                        "country": row[4],
                        "countryCode": row[5],
                        "lat": row[6],
                        "lon": row[7],
                        "isp": row[8],
                        "query": row[9],
                        "threat": row[10],
                        "terms": row[11].replace("|", ", ")
                    })
    return render_template("admin.html", entries=entries)

@app.route("/clear-log", methods=["POST"])
def clear_log():
    open("logs.csv", "w").close()
    open("threat_log.txt", "w").close()
    return redirect("/admin")

import os

# --- Run App ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

