CodeCommunity — A Django-powered platform where developers learn together

A Django-based web application where users can create study rooms, join discussions, browse topics, and collaborate with other learners in real time.

🚀 Features
👤 User Authentication

Login / Register system

Custom user profiles

View profile activity, created rooms, and messages

🏠 Study Rooms

Create public rooms on any topic

Join and participate in ongoing discussions

View room host, topic, participants, and live messages

Edit or delete your own rooms

💬 Real-Time Messaging

Post messages inside rooms

Messages update instantly

Delete your own messages

Activity feed shows latest replies

🧠 Browse Topics

Sidebar with topics (Java, C++, Python, Golang, etc.)

Filter rooms by selected topic

Auto-updated room count

📰 Recent Activity Feed

Displays who replied, where, and when

Helps track all community discussions

🎨 Modern UI

Clean and dark-themed interface

Responsive and user-friendly

Smooth navigation

🔧 Tech Stack

Backend: Django

Frontend: HTML, CSS, JavaScript

Database: SQLite (default)

Auth: Custom Django User Model

📦 Installation & Setup

Follow the steps below to run the project locally.

1. Clone the repository
git clone <your-repository-link>
cd codecommunity

2. Create a virtual environment
python -m venv env
source env/bin/activate     # Mac/Linux
env\Scripts\activate        # Windows

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py migrate

5. Create a superuser (optional)
python manage.py createsuperuser

6. Run the development server
python manage.py runserver


Visit:

http://127.0.0.1:8000/

📁 Project Structure
codecommunity/
│── base/               # Main app (rooms, topics, messages)
│── users/              # User authentication, profiles
│── templates/          # HTML templates
│── static/             # CSS, JS, Images
│── db.sqlite3          # Default database
│── manage.py
│── requirements.txt
└── README.md
