# README 


A simple Django-powered web app that lets users upload `.vcf` (vCard) files and instantly download them as formatted `.xlsx` Excel spreadsheets.

---

## 🚀 Features

- Upload `.vcf` files directly through the browser
- Automatically parses contacts into Name, Phone, Email
- Clean Bootstrap interface
- Instant Excel file download — no account required

---

## 🛠️ Requirements

- Python 3.8+
- Django 4.x or 5.x
- `vobject` for parsing `.vcf` files
- `pandas` for handling data
- `openpyxl` for Excel file creation

---

## 📦 Installation

1. **Clone the repo:**

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. **Set up virtual environment:**

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate

3. **Install dependencies:**

pip install django vobject pandas openpyxl

4. **Run the Dev Server**

python manage.py migrate
python manage.py runserver

5. **Visit the app in your browser:**
http://127.0.0.1:8000

## 💻 Usage

Upload your .vcf file using the form.

The app will automatically convert it into an Excel spreadsheet.

Your browser will download contacts.xlsx immediately.

## 📂 Project Structure

contacts/
├── views.py
├── forms.py
├── utils.py           # VCF parsing + Excel export
├── templates/
│   └── contacts/
│       ├── base.html
│       └── upload.html

