# **NurseLink**  

**NurseLink** is a **centralized nurse booking platform** that integrates:  
- A **24/7 AI-powered chatbot** built on **Retrieval-Augmented Generation (RAG)**  
- An **AI-based nurse–user profile matching system** powered by **Gemini**  

---

## **Overview**  
This project provides a streamlined solution for patients and families to book qualified nurses easily and efficiently.  

The AI-driven features ensure:  
- ⚡ **Instant query resolution** through the chatbot  
- 🧠 **Smart nurse–patient matching** for better compatibility  

---

## **Setup Guide**  
This documentation will:  
- Walk you through the **file system**  
- Provide **step-by-step instructions** to set up and run the code on your local machine  

---

## **📁 File Structure**

```bash
NurseLink/
├── Authentication
├── booking
├── myapp
├── NurseLink
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── venv/ 
├── .env 
├── db.sqlite3
├── manage.py 
├── nursedata.csv 
├── requirements.txt
├── Pipfile 
└── Pipfile.lock
```

### **Folder Descriptions**
- **NurseLink/** → Root directory of the project  
- **NurseLink/** → Contains `manage.py`, essential for running the server  
- **Authentication/** → Handles user login and signup  
- **booking/** → Manages nurse booking functionality  
- **myapp/** → Handles AI-based user–profile matching logic  
- **.env** → Stores environment variables (ignored in version control)  
- **nursedata.csv** → Contains generated nurse data using `pandas` and `faker`  
- **requirements.txt** → Lists dependencies required for local setup and deployment  

---

## **🤖 Chatbot Info**
> The chatbot is hosted in a separate repository and deployed using Streamlit.  
> A local chatbot integration is planned soon.  

🔗 **Chatbot Repo:** [https://github.com/Adhikulkarn/Nurse_link-Chatbot](https://github.com/Adhikulkarn/Nurse_link-Chatbot)

---

## **⚙️ Environment Setup**

Before running the project, create a `.env` file in the **root directory** and add your Gemini API key:  

```bash
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ This file will be ignored when committing to the main branch.

### **Get Your Gemini API Key**
You can obtain a free Gemini API key from Google AI Studio:  
👉 [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

---

## **🚀 Running the Project**

### **Step 1: Create a Virtual Environment**

#### For Windows:
```bash
pip install pipenv
pipenv shell
```

#### For Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### **Step 2: Install Dependencies**

First, ensure you’re in the root directory and `requirements.txt` is present:
```bash
ls
```

If you see `requirements.txt` listed, run the following:

#### For Windows:
```bash
pipenv install -r requirements.txt
```

#### For Linux:
```bash
pip install -r requirements.txt
```

---

### **Step 3: Run the Server**

Once dependencies are installed, start the Django development server:

```bash
python manage.py runserver
```

Your application will be available at:  
👉 `http://127.0.0.1:8000/`

---

✅ You’re now ready to explore **NurseLink** locally!

---

📬 **For any queries**, contact the developer at:  
**adityask200615@gmail.com**
