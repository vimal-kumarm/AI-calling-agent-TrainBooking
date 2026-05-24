
## Prerequisites

- Python 3.10+
- Google ai Studio API Key
- Pipedream URLs for integrations (YouTube and either Drive or Notion)



  🚆 Indian Train Tracker + Voice Assistant
A real-time Indian Railway tracking app built with Streamlit, powered by the IRCTC RapidAPI for live train data, Twilio + ElevenLabs for AI voice calls, and Gmail for email notifications.
---
🖥️ Live Demo
```
streamlit run app.py
```
---
✨ Features
🔍 Train Search (Real Data)
Search trains between any two stations by IRCTC station code
Live results from IRCTC RapidAPI — train name, number, departure, arrival, duration, class types, running days
Optional SMS summary to your phone after search
Optional Gmail/email notification with full results
📊 Live Train Status (Real Data)
Real-time location and delay info for any running train
Station-wise status — scheduled vs actual arrival, delay per stop
Shows current station the train is near right now
Optional SMS + email delivery of the status report
🤖 AI Railway Voice Agent
Select booking type: Book tickets, Check availability, Get schedule, Check booking status, Cancel/modify, General info
Set urgency level: Normal / Urgent / Emergency
Enter your travel route and date
Click Call Me Now — AI speaks a personalised message to your phone via ElevenLabs TTS + Twilio
Optional: Interactive Call mode for two-way conversation (requires webhook server)
📍 Location Detection
Auto-detects your city via IP and suggests nearby railway station codes
📧 Gmail / Email Notifications
Send train search results and live status directly to your Gmail
Fallback to local file-based email if Gmail is not configured
HTML-formatted emails with full train details
---
🗂️ Project Structure
```
├── app.py                          # Main Streamlit app (all UI + API calls)
├── config.py                       # API keys and credentials
├── call\\\_me.py                      # CLI script to trigger a voice call directly
├── prompt.py                       # Learning path generator prompt template
├── railway\\\_helper.py               # Helper for Indian Railway MCP server
├── utils.py                        # LangChain + LangGraph agent utilities
├── webhook\\\_server.py               # Flask server for interactive two-way voice calls
├── requirements.txt                # Python dependencies
│
├── service/
│   ├── voice\\\_agent.py              # Twilio + ElevenLabs voice call logic
│   ├── interactive\\\_voice\\\_agent.py  # Full interactive voice agent (webhook-based)
│   ├── simple\\\_interactive\\\_agent.py # Demo interactive call
│   ├── gmail\\\_service.py            # Gmail SMTP email service
│   ├── gmail\\\_mcp\\\_service.py        # Gmail via MCP API
│   └── simple\\\_file\\\_email\\\_service.py# File-based email fallback
│
├── test\\\_voice.py                   # Test voice call integration
├── test\\\_gmail.py                   # Test Gmail integration
├── test\\\_interactive.py             # Test interactive voice calls
├── test\\\_mcp\\\_only.py                # Test Gmail MCP API
│
├── GMAIL\\\_SETUP\\\_GUIDE.md            # Step-by-step Gmail setup
└── INTERACTIVE\\\_SETUP.md            # Step-by-step interactive voice setup
```
---
⚙️ Setup & Installation
1. Clone the Repository
```bash
git clone https://github.com/YOUR\\\_USERNAME/indian-train-tracker.git
cd indian-train-tracker
```
2. Install Dependencies
```bash
pip install -r requirements.txt
```
3. Configure Credentials
Open `config.py` and fill in your credentials:
```python
# ElevenLabs — Text-to-Speech for voice calls
# Get from: https://elevenlabs.io/
ELEVENLABS\\\_API\\\_KEY = "your\\\_elevenlabs\\\_api\\\_key"

# Twilio — Outbound phone calls
# Get from: https://www.twilio.com/
TWILIO\\\_ACCOUNT\\\_SID  = "your\\\_twilio\\\_account\\\_sid"
TWILIO\\\_AUTH\\\_TOKEN   = "your\\\_twilio\\\_auth\\\_token"
TWILIO\\\_FROM\\\_NUMBER  = "+1XXXXXXXXXX"   # Your Twilio number

# Gmail — Email notifications
# Generate App Password: https://myaccount.google.com/apppasswords
GMAIL\\\_USER         = "your\\\_email@gmail.com"
GMAIL\\\_APP\\\_PASSWORD = "your\\\_16\\\_char\\\_app\\\_password"

# Google AI Studio — For learning path generator
GOOGLE\\\_API\\\_KEY = "your\\\_google\\\_api\\\_key"
```
> \\\*\\\*Note:\\\*\\\* Train data uses the IRCTC RapidAPI key that is already embedded in `app.py`. No setup needed for train search.
4. Run the App
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`
---
🔑 API Keys & Services
Service	Purpose	Free Tier	Get Key
IRCTC RapidAPI	Real train data	✅ Free plan	Already embedded in app
Twilio	Voice calls & SMS	✅ Trial credits	twilio.com
ElevenLabs	AI Text-to-Speech	✅ Free tier	elevenlabs.io
Gmail App Password	Email notifications	✅ Free	myaccount.google.com/apppasswords
Google AI Studio	Learning path agent	✅ Free tier	aistudio.google.com
---
📞 Voice Call Setup
Basic Voice Calls (Works Immediately)
Add your `TWILIO\\\_ACCOUNT\\\_SID`, `TWILIO\\\_AUTH\\\_TOKEN`, `TWILIO\\\_FROM\\\_NUMBER` in `config.py`
Add your `ELEVENLABS\\\_API\\\_KEY` in `config.py`
Enter your phone number in the sidebar (with country code, e.g. `+91XXXXXXXXXX`)
Click Call Me Now in the Voice Agent tab
> ⚠️ \\\*\\\*Twilio Trial Accounts:\\\*\\\* You can only call verified numbers. Verify your number at \\\[console.twilio.com → Verified Caller IDs](https://console.twilio.com/).
Interactive Two-Way Calls (Optional)
For full two-way AI conversations, see INTERACTIVE_SETUP.md.
---
📧 Gmail Setup
For step-by-step Gmail configuration, see GMAIL_SETUP_GUIDE.md.
Quick summary:
Enable 2-Factor Authentication on your Google account
Generate an App Password at myaccount.google.com/apppasswords
Add `GMAIL\\\_USER` and `GMAIL\\\_APP\\\_PASSWORD` to `config.py`
---
🚉 Common Station Codes
City	Code	City	Code
Chennai Central	MAS	New Delhi	NDLS
Salem	SA	Mumbai Central	BCT
Bangalore City	SBC	Ernakulam	ERS
Hyderabad	HYB	Kolkata (Howrah)	HWH
Coimbatore	CBE	Madurai	MDU
Pune	PUNE	Ahmedabad	ADI
Secunderabad	SC	Yesvantpur	YPR
---
🧪 Testing
```bash
# Test voice call integration
python test\\\_voice.py

# Test Gmail email sending
python test\\\_gmail.py

# Test interactive voice call
python test\\\_interactive.py

# Test Gmail MCP API (no SMTP)
python test\\\_mcp\\\_only.py

# Make a quick voice call from terminal
python call\\\_me.py
```
---
🚀 Deployment
Deploy on Streamlit Cloud
Push this repository to GitHub
Go to share.streamlit.io
Connect your GitHub repo
Set Main file path to `app.py`
Add secrets under Settings → Secrets:
```toml
ELEVENLABS\\\_API\\\_KEY   = "your\\\_key"
TWILIO\\\_ACCOUNT\\\_SID   = "your\\\_sid"
TWILIO\\\_AUTH\\\_TOKEN    = "your\\\_token"
TWILIO\\\_FROM\\\_NUMBER   = "+1XXXXXXXXXX"
GMAIL\\\_USER           = "your\\\_email@gmail.com"
GMAIL\\\_APP\\\_PASSWORD   = "your\\\_app\\\_password"
```
Deploy on Railway / Heroku
```bash
# Railway
railway login
railway init
railway up

# Heroku
heroku create your-app-name
git push heroku main
```
---
🛠️ Troubleshooting
Problem	Solution
Train search returns no data	Check internet connection; IRCTC API may be temporarily down
Voice call not connecting	Verify Twilio credentials in `config.py`; ensure number is verified for trial accounts
Gmail not sending	Confirm 2FA is enabled; check App Password is 16 characters with no spaces
`ModuleNotFoundError: service`	Make sure the `service/` directory exists and contains `\\\_\\\_init\\\_\\\_.py`
Twilio `unverified number` error	Verify the destination number at console.twilio.com
`403` from train API	The embedded IRCTC API key may have expired — open an issue
---
📦 Dependencies
```
streamlit>=1.56
requests
twilio
flask
langchain
langgraph
langchain-mcp-adapters
langchain-google-genai
elevenlabs
```
---
🤝 Contributing
Fork the repository
Create a feature branch: `git checkout -b feature/your-feature`
Commit your changes: `git commit -m "Add your feature"`
Push to the branch: `git push origin feature/your-feature`
Open a Pull Request
---
⚠️ Security Notice
Never commit real API keys, tokens, or passwords to a public repository
The IRCTC RapidAPI key in `app.py` is a shared demo key — for production use, move all keys to environment variables or Streamlit secrets
Rotate your Twilio and ElevenLabs keys if you suspect they've been exposed
---
📄 License
MIT License — feel free to use, modify, and distribute.
---
Built with ❤️ using Streamlit · Twilio · ElevenLabs · IRCTC RapidAPI
  
