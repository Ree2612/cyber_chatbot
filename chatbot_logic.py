import spacy
import cohere
import os
from dotenv import load_dotenv

# Load .env and API key
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Initialize Cohere client
co = cohere.Client(COHERE_API_KEY)

# Cybersecurity knowledge base
cyber_knowledge = {
    "phishing": "Phishing is a type of social engineering attack used to steal user data.",
    "malware": "Malware is malicious software designed to damage or gain unauthorized access.",
    "ransomware": "Ransomware locks your files and demands payment for access.",
    "sql injection": "SQL Injection exploits vulnerable input fields to run unauthorized SQL commands.",
    "xss": "XSS (Cross-Site Scripting) allows attackers to inject client-side scripts.",
    "hacking": "Hacking, in its simplest form, is the act of gaining unauthorized access to a computer system or network. This is often achieved by exploiting vulnerabilities or weaknesses in security measures."
}

# Detect threat terms in input
def detect_threat(user_input):
    lower = user_input.lower()
    return [term for term in cyber_knowledge if term in lower]

# Main chatbot logic
def get_bot_response(user_input):
    user_input = user_input.strip()
    doc = nlp(user_input.lower())

    # Rule-based replies
    if any(token.lemma_ in ["hi", "hello", "hey", "hii", "namaste"] for token in doc):
        return "👋 Hello! How can I help you with cybersecurity?", False, []
    if "name" in user_input.lower():
        return "🤖 I'm your Cybersecurity-Aware Assistant.", False, []
    if "thank" in user_input.lower():
        return "You're welcome! Stay safe online 🛡️", False, []
    if any(token.lemma_ in ["bye", "goodbye", "see", "later"] for token in doc):
        return "👋 Goodbye! Stay cyber-safe!", False, []
    if any(token.lemma_ in ["ok great","ok","great"] for token in doc):
        return "You're welcome:)", False, []
    if any(token.lemma_ in ["how are you?","how are you","what are you doing?"] for token in doc):
        return "I am doing great, Thanks for asking", False, []

    # Threat keyword detection
    threats_found = detect_threat(user_input)
    if threats_found:
        response = "\n\n".join(
            [f"{term.capitalize()}: {cyber_knowledge[term]}" for term in threats_found]
        )
        return response, True, threats_found

    # Skip fallback for very short input
    if len(user_input.split()) <= 2:
        return "🤔 Can you elaborate a bit? Try asking about malware, phishing, XSS, etc.", False, []

    # Fallback to Cohere AI
    try:
        response = co.chat(message=user_input, model="command-r")
        answer = response.text.strip()
        return f"🤖 {answer}", False, []
    except Exception as e:
        return f"❌ Error using Cohere: {str(e)}", False, []
