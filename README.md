# 📧 Gmail Email Fetcher

🚀 **Gmail Email Fetcher** is a Python-based tool that helps you fetch emails from your Gmail account, extract important details, and store them securely in an Excel file.

---

## 📌 Features
✅ Fetch emails from Gmail using **Gmail API**  
✅ Automatically extract and store important email data in an **Excel file**  
✅ Secure authentication using **OAuth 2.0**  
✅ Supports **CSV and Excel Export**  
✅ Easy to setup and run  

---

## 🛠️ **Installation Guide**

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/amitsh06/gmail-email-fetcher.git
cd gmail-email-fetcher
```

### 2️⃣ **Create a Virtual Environment** (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### 3️⃣ **Install Required Packages**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Setup Gmail API**
- Go to **Google Cloud Console** → Create a new project  
- Enable **Gmail API**  
- Download **credentials.json** and place it in the project folder  

---

## 🚀 **How to Run**
```bash
python read_emails.py
```

---

## ❗ Issues Faced & Fixes

### 🔴 **1. GitHub Push Error: "error: failed to push some refs"**
✅ **Solution:** Run this command before pushing the changes:
```bash
git pull --rebase origin main
git push origin main
```

---

### 🔴 **2. Gmail API Authentication Issues**
✅ **Solution:**  
1. Make sure `credentials.json` is in the correct folder.  
2. Delete the `token.json` file and re-run the script.  

---

### 🔴 **3. Virtual Environment Not Activating in Windows**
✅ **Solution:**  
Run this command in PowerShell (Admin mode):
```bash
Set-ExecutionPolicy Unrestricted -Scope Process
```
Then activate the virtual environment again.

---

## 📝 **Project Structure**
```
📂 gmail-email-fetcher
│-- 📄 README.md
│-- 📄 requirements.txt
│-- 📄 authenticate.py
│-- 📄 read_emails.py
│-- 📄 emails.xlsx
│-- 📄 credentials.json (Not uploaded to GitHub)
│-- 📄 .gitignore
│-- 📄 .env
```

---

## 🤝 **Contributing**
Want to improve this project? Feel free to submit a **pull request** or report issues!  

---

## 📜 **License**
This project is **MIT Licensed** – Free to use and modify!  

---

### ✨ **Author**: [amitsh06](https://github.com/amitsh06)  
