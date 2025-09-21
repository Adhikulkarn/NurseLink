# **NurseLink**  

**NurseLink** is a **centralized nurse booking platform** that integrates:  
- A **24/7 AI-powered chatbot** built on **Retrieval-Augmented Generation (RAG)**  
- An **AI-based nurse–user profile matching system** powered by **Gemini**  

---

## **Overview**  
This project provides a streamlined solution for patients and families to book qualified nurses easily and efficiently. The AI-driven features ensure:  
- **Instant query resolution** through the chatbot  
- **Smart profile matching** for better nurse–patient compatibility  

---

## **Setup Guide**  
This documentation will:  
- Walk you through the **file system**  
- Provide **step-by-step instructions** to set up and run the code on your local machine  

---

## **Lets go through the file system**

NURSELINK/
├── Authentication/ # Handles user authentication
├── booking/ # Booking-related functionality
├── myapp/ # Additional app (custom features)
├── NURSELINK/ # Core project files
│   ├── __init__.py
│   ├── asgi.py # ASGI config
│   ├── settings.py # Django settings
│   ├── urls.py # Project URLs
│   └── wsgi.py # WSGI config
├── venv/ # Virtual environment
├── .env # Environment variables
├── db.sqlite3 # SQLite database
├── manage.py # Django management script
├── nursedata.csv # Nurse dataset
├── requirements.txt # Project dependencies
├── Pipfile # Pipenv dependency manager
└── Pipfile.lock
