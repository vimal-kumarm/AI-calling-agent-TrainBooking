# GMAIL_SETUP_GUIDE.md

# 📧 Gmail Integration Setup Guide

This guide will help you set up Gmail integration to send train status and call details directly to your Gmail account.

## 🔧 Prerequisites

1. **Gmail Account**: You need a Gmail account
2. **2-Factor Authentication**: Must be enabled on your Gmail account
3. **App Password**: Generated from Google Account settings

## 📋 Step-by-Step Setup

### Step 1: Enable 2-Factor Authentication

1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Sign in to your Google account
3. Under "Signing in to Google", click **2-Step Verification**
4. Follow the prompts to enable 2-factor authentication

### Step 2: Generate App Password

1. Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
2. Sign in to your Google account
3. Select **Mail** as the app
4. Select **Other (custom name)** as the device
5. Enter "Railway Assistant" as the name
6. Click **Generate**
7. Copy the 16-character password (it will look like: `abcd efgh ijkl mnop`)

### Step 3: Update Configuration

1. Open `config.py` in your project
2. Update the Gmail credentials:

```python
# Gmail Configuration for sending emails
GMAIL_USER = "your_email@gmail.com"  # Replace with your Gmail address
GMAIL_APP_PASSWORD = "your_app_password"  # Replace with your 16-character app password
```

**Example:**
```python
GMAIL_USER = "vimalkumarm196@gmail.com"
GMAIL_APP_PASSWORD = "abcd efgh ijkl mnop"
```

### Step 4: Test Gmail Integration

Run the test script to verify your setup:

```bash
python test_gmail.py
```

## 🚀 Features

Once configured, the Gmail integration provides:

### ✅ Train Status Emails
- Beautiful HTML emails with train information
- Real-time status updates
- Professional formatting with status badges
- Plain text fallback for all email clients

### ✅ Call Details Emails
- AI call information and details
- Call type and priority information
- Message content and timestamps
- Call ID for tracking

### ✅ App Integration
- Toggle Gmail sending in the Streamlit app
- Automatic email sending for train searches
- Call details sent after voice calls
- Error handling and status reporting

## 🔒 Security Notes

- **Never share your App Password**
- **App Passwords are safer than your main password**
- **You can revoke App Passwords anytime from Google Account settings**
- **Each App Password is unique and can be deleted independently**

## 🛠️ Troubleshooting

### Common Issues:

1. **"Authentication failed"**
   - Check if 2-factor authentication is enabled
   - Verify the App Password is correct (16 characters)
   - Make sure there are no extra spaces in the password

2. **"SMTP connection failed"**
   - Check your internet connection
   - Verify Gmail SMTP settings (smtp.gmail.com:587)
   - Check if your firewall blocks SMTP connections

3. **"Email not received"**
   - Check spam/junk folder
   - Verify the recipient email address is correct
   - Check Gmail's "Less secure app access" settings

### Test Commands:

```bash
# Test Gmail configuration
python -c "from service.gmail_service import GmailService; gs = GmailService(); print('Configured:', gs.is_configured())"

# Send test email
python -c "from service.gmail_service import send_train_status_gmail; result = send_train_status_gmail('your_email@gmail.com', {'train_number': '12617', 'status': 'On Time', 'last_station': 'Test Station'}); print(result)"
```

## 📞 Support

If you encounter issues:
1. Check the error messages in the terminal
2. Verify your Gmail credentials in `config.py`
3. Test with a simple email first
4. Check Google Account security settings

---

**Ready to send beautiful train status emails! 🚆📧**

