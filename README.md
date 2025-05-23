# Parent‑Teacher Communication App

A simple Django web platform enabling parents and teachers to message each other, view student progress, and schedule meetings — all in a clean dark‑theme interface.

---

## ✨ Features

* **Role‑based authentication** (Parent / Teacher)
* Secure **one‑to‑one messaging** with reply threads
* **Student progress** table (demo scores)
* **Meeting scheduler** with date‑time picker
* Dark theme, cobalt accent, responsive Bootstrap 5 UI
* Ready for deployment on Render, Railway, or Vercel (via gunicorn)

---

## 🛠️ Tech Stack

| Layer    | Tech                                   |
| -------- | -------------------------------------- |
| Backend  | Django 4+, Python 3                     |
| Frontend | Bootstrap 5, custom CSS                |
| Database | SQLite (dev) → PostgreSQL (prod)       |
| Deploy   | Render / Railway / Vercel (Py‑Runtime) |

---

## 🚀 Quick Start (Local)

```bash
# 1. Clone & enter
git clone https://github.com/Morg3an/parent-teacher-comm-app.git
cd parent-teacher-comm-app

# 2. Create virtual env & install deps
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. DB migrate & superuser
python manage.py migrate
python manage.py createsuperuser

# 4. Run server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` and log in.

---

## 🌐 Deployment (Render example)

1. Add `Procfile`:

   ```Procfile
   web: gunicorn core.wsgi:application
   ```
2. Push to GitHub.
3. In Render dashboard → **New Web Service** → connect repo.
4. Set environment variable `SECRET_KEY`.
5. Deploy — Render gives a public URL.

*(Railway or Vercel follow similar steps; ensure `gunicorn` and `requirements.txt` are committed.)*

---

## 📂 Project Structure (key parts)

```
├─ core/            # Django project settings
│  └─ templates/
├─ comm/            # app: models, views, forms
├─ static/
│  └─ theme.css
├─ db.sqlite3       # dev DB (git‑ignored)
├─ requirements.txt
├─ Procfile         # for gunicorn deploy
└─ README.md
```

---

## 🤝 Contributing

Pull requests welcome! Please open an issue first to discuss significant changes.

---

## 📜 License

MIT License — free to modify and distribute.
