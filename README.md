# AccuKnox_Django
Here’s a **GitHub README.md** for these files that explains each one professionally and makes your repository clean and attractive:

---

# 🐍 Python & HTML Mini Projects

This repository contains a collection of Python and HTML projects demonstrating concepts like **Django signals**, **Python iterators**, and interactive web visualization.

---

## 📦 Projects Included

### 1️⃣ Django Signals – Basic Example (`Question_1.py`)

Demonstrates how Django signals work synchronously.

* Defines a custom signal.
* Connects a receiver using the `@receiver` decorator.
* Prints output before and after sending the signal.

**Run:**

```bash
python Question_1.py
```

---

### 2️⃣ Django Signals with Thread Info (`Question_2.py`)

Extends the previous example to show the thread context of Django signals.

* Prints current thread name while sending and receiving signals.
* Confirms that signals run in the same thread as the sender by default.

**Run:**

```bash
python Question_2.py
```

---

### 3️⃣ Django Signals with Database Transactions (`Question_3.py`)

Demonstrates Django signals executed inside a database transaction.

* Uses `transaction.atomic()` to simulate a DB operation.
* Shows that signal handlers execute within the transaction scope.

**Run:**

```bash
python Question_3.py
```

---

### 4️⃣ Interactive Rectangle Visualization (`Rectangle.html`)

An interactive HTML demo visualizing a **Python Rectangle class** using the iterator protocol.

* Enter rectangle dimensions to visualize it dynamically.
* Highlights Python’s `__iter__` and `__next__` methods.
* Built with TailwindCSS for modern design.

**Open in Browser:**
Double-click `Rectangle.html` or open with any web browser.

---

## 🧰 Tech Stack

| Category | Technologies                   |
| -------- | ------------------------------ |
| Backend  | Python, Django                 |
| Frontend | HTML5, TailwindCSS, JavaScript |
| Database | Simulated with Django models   |

---

## 🚀 Getting Started

1. Clone this repository:

```bash
git clone https://github.com/YOUR-USERNAME/python-html-mini-projects.git
cd python-html-mini-projects
```

2. Run Python files directly with:

```bash
python <file_name>.py
```

3. Open `Rectangle.html` in your browser for the interactive demo.

---
