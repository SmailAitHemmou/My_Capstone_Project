# 🎬 WatchLog

**WatchLog** is a personal web application built with **Django** that helps users **organize, track, and manage** their favorite movies and series.  
With a simple and elegant interface, WatchLog offers a smooth experience for users to keep track of what they’ve watched and what’s next on their list.

---

## 🌟 Overview

Welcome to **WatchLog**, your personal movie and series organizer.  
Whether you're an avid binge-watcher or a casual viewer, WatchLog keeps your watchlist neatly organized — all in one place.

Users can:
- Create an account and securely log in.
- Add movies or series to their personal list.
- Mark items as “watched” or “to watch”.
- Explore an intuitive, clean interface built for simplicity.

---

## ⚙️ Features

- 🧩 User authentication (Sign up, Login, Logout)
- 🎞️ Add, edit, or remove movies and series
- ✅ Mark watched content
- 🏠 Beautiful and simple homepage for new visitors
- 📁 Separate pages for Movies and Series
- 💻 Responsive design compatible with all devices

---

## REST API Features
This project now includes a REST API built with Django REST Framework.

**Endpoints:**
- `/series/` – List and create series
- `/series/<id>/` – Retrieve, update, or delete a series

Authenticated users can manage their own series.

- `/movies/` – List and create movies
- `/movies/<id>/` – Retrieve, update, or delete a movies

Authenticated users can manage their own movies.


## 🧰 Technologies Used

- **Python** (Django Framework)
- **HTML5**, **CSS3**, **Bootstrap 5**
- **SQLite** (Default Django database)
- **Git & GitHub** for version control

---

## 🚀 Installation Guide

Follow these steps to run the project locally 👇

```bash
# 1. Clone the repository
git clone https://github.com/SmailAitHemmou/My_Capstone_Project.git
cd My_Capstone_Project

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Apply database migrations
python manage.py migrate

# 6. Run the development server
python manage.py runserver


👨‍💻 Author

Developed by: Smail Ait Hemmou
🎓 University of Abdelmalek Essaadi — Physics Department, Morocco
📫 GitHub: https://github.com/SmailAitHemmou