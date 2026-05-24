#!/usr/bin/env python3
"""
Gmail Integration Test Script
Tests the Gmail service functionality
"""

from service.gmail_service import GmailService, send_train_status_gmail, send_call_details_gmail
from datetime import datetime

def test_gmail_configuration():
    """Test if Gmail credentials are properly configured"""
    print("🔧 Testing Gmail Configuration...")
    print("=" * 50)
    
    gmail_service = GmailService()
    
    if gmail_service.is_configured():
        print("✅ Gmail credentials are configured!")
        print(f"📧 Gmail User: {gmail_service.gmail_user}")
        print(f"🔑 App Password: {'*' * len(gmail_service.gmail_password)}")
        return True
    else:
        print("❌ Gmail credentials not configured!")
        print("\n📋 Setup Required:")
        print("1. Enable 2-factor authentication on your Gmail account")
        print("2. Generate an App Password from Google Account settings")
        print("3. Update config.py with your Gmail credentials:")
        print("   GMAIL_USER = 'your_email@gmail.com'")
        print("   GMAIL_APP_PASSWORD = 'your_16_character_app_password'")
        return False

def test_train_status_email():
    """Test sending train status email"""
    print("\n🚆 Testing Train Status Email...")
    print("=" * 50)
    
    # Test data
    train_data = {
        'train_number': '12617',
        'status': 'On Time',
        'last_station': 'Chennai Central',
        'arrival': '12:35 PM',
        'next_station': 'Bangalore',
        'delay': '0 minutes',
        'platform': 'Platform 3'
    }
    
    # Get recipient email from user
    recipient = input("Enter recipient email address: ").strip()
    
    if not recipient:
        print("❌ No email address provided!")
        return False
    
    print(f"📧 Sending train status email to: {recipient}")
    print(f"🚆 Train: {train_data['train_number']} - {train_data['status']}")
    
    try:
        result = send_train_status_gmail(recipient, train_data)
        
        if result['status'] == 'success':
            print("✅ Train status email sent successfully!")
            print(f"📧 Method: {result['method']}")
            print(f"🕒 Timestamp: {result['timestamp']}")
            return True
        else:
            print(f"❌ Failed to send email: {result['message']}")
            return False
            
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False

def test_call_details_email():
    """Test sending call details email"""
    print("\n📞 Testing Call Details Email...")
    print("=" * 50)
    
    # Test data
    call_details = {
        'call_type': 'Railway Booking Assistant',
        'priority': 'Normal',
        'call_sid': 'CA1234567890abcdef',
        'status': 'Completed',
        'message': 'Hello! This is your AI Railway Assistant calling to help with train booking.',
        'timestamp': datetime.now().isoformat()
    }
    
    # Get recipient email from user
    recipient = input("Enter recipient email address: ").strip()
    
    if not recipient:
        print("❌ No email address provided!")
        return False
    
    print(f"📧 Sending call details email to: {recipient}")
    print(f"📞 Call Type: {call_details['call_type']}")
    
    try:
        result = send_call_details_gmail(recipient, call_details)
        
        if result['status'] == 'success':
            print("✅ Call details email sent successfully!")
            print(f"📧 Method: {result['method']}")
            print(f"🕒 Timestamp: {result['timestamp']}")
            return True
        else:
            print(f"❌ Failed to send email: {result['message']}")
            return False
            
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False

def main():
    """Main test function"""
    print("📧 Gmail Integration Test Suite")
    print("=" * 50)
    
    # Test 1: Configuration
    config_ok = test_gmail_configuration()
    
    if not config_ok:
        print("\n❌ Please configure Gmail credentials first!")
        print("📖 See GMAIL_SETUP_GUIDE.md for detailed instructions")
        return
    
    # Test 2: Train Status Email
    print("\n" + "=" * 50)
    test_train = input("Test train status email? (y/n): ").lower().strip()
    if test_train == 'y':
        test_train_status_email()
    
    # Test 3: Call Details Email
    print("\n" + "=" * 50)
    test_call = input("Test call details email? (y/n): ").lower().strip()
    if test_call == 'y':
        test_call_details_email()
    
    print("\n🎉 Gmail integration testing completed!")
    print("📧 Check your email inbox for the test messages")

if __name__ == "__main__":
    main()

