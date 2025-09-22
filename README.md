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

- **NurseLink** : It is the root Directory 
- **NurseLink** : It is the directort which contains the manage.py which is essential to run the server
- **Authentication** : This is a django app which handles the Authentication part [Login/Signup]
- **booking** : This is a django app which takes you to the booking page
- **myapp** : This is a django app which handles the AI based user-profile matching 
- **.env** : This is the file which contains environment vaiables
- **nursedata.csv** : This is a CSV file which contains fake nurse data genrated using pandas.faker
- **requirements.txt** : Contains the requirements to be downloaded to run the code locally and also used while deploying the project

---

### **Note : You will find the code to the chatbot in a different repository, that code is deployed using streamlit, but a local chatbot will be integrated soo, [Chatbot repo: https://github.com/Adhikulkarn/Nurse_link-Chatbot]**
