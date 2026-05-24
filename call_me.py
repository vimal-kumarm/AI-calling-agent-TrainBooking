#!/usr/bin/env python3
"""
Simple script to make a voice call using the voice agent
"""

import os
import sys
from service.voice_agent import call_summary_with_voice

# Windows encoding fix
def safe_print(text):
    """Print text safely on Windows by handling Unicode characters"""
    try:
        print(text)
    except UnicodeEncodeError:
        # Replace Unicode characters with ASCII equivalents for Windows
        safe_text = text.replace('🎯', '[TARGET]').replace('❌', '[ERROR]').replace('✅', '[OK]').replace('📞', '[PHONE]').replace('🚀', '[ROCKET]').replace('📋', '[CLIPBOARD]').replace('🎤', '[MIC]')
        print(safe_text)

def make_call(message=None):
    try:
        from config import ELEVENLABS_API_KEY, TWILIO_FROM_NUMBER, TO_NUMBER, DEFAULT_MESSAGE
    except ImportError:
        safe_print("❌ Configuration file not found or incomplete!")
        safe_print("Please create a config.py file with your API keys and phone numbers.")
        return None
    
    # Use provided message or default
    if message is None:
        message = DEFAULT_MESSAGE
    
    try:
        safe_print("📞 Making call...")
        safe_print(f"From: {TWILIO_FROM_NUMBER}")
        safe_print(f"To: {TO_NUMBER}")
        safe_print(f"Message: {message}")
        
        result = call_summary_with_voice(
            ELEVENLABS_API_KEY,
            TWILIO_FROM_NUMBER,
            TO_NUMBER,
            message
        )
        
        safe_print("✅ Call initiated successfully!")
        safe_print(f"Call SID: {result['call_sid']}")
        safe_print(f"Status: {result['status']}")
        return result
        
    except Exception as e:
        safe_print(f"❌ Error making call: {e}")
        return None

if __name__ == "__main__":
    safe_print("🎯 Voice Call Script")
    safe_print("===================")
    safe_print("")
    
    # Check if config exists
    try:
        from config import ELEVENLABS_API_KEY, TWILIO_FROM_NUMBER, TO_NUMBER
        safe_print("✅ Configuration loaded successfully!")
    except ImportError:
        safe_print("❌ Configuration not found!")
        safe_print("\n📋 Setup Instructions:")
        safe_print("1. Create a config.py file with your API keys")
        safe_print("2. Get ElevenLabs API key from: https://elevenlabs.io/")
        safe_print("3. Get Twilio credentials from: https://www.twilio.com/")
        safe_print("4. Update the phone numbers in config.py")
        safe_print("\nExample config.py:")
        safe_print("ELEVENLABS_API_KEY = 'your_key_here'")
        safe_print("TWILIO_ACCOUNT_SID = 'your_sid_here'")
        safe_print("TWILIO_AUTH_TOKEN = 'your_token_here'")
        safe_print("TWILIO_FROM_NUMBER = '+1234567890'")
        safe_print("TO_NUMBER = '+1234567890'")
        exit(1)
    
    # Check if credentials are set
    if (ELEVENLABS_API_KEY == "your_elevenlabs_api_key_here" or 
        TWILIO_FROM_NUMBER == "+1234567890" or 
        TO_NUMBER == "+1234567890"):
        safe_print("❌ Please update the configuration in config.py with your actual credentials!")
        exit(1)
    
    # Make the call
    safe_print("🚀 Ready to make call!")
    custom_message = input("Enter custom message (or press Enter for default): ").strip()
    
    if custom_message:
        make_call(custom_message)
    else:
        make_call()
