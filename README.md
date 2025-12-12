# 🧩 Python OOP Homework — Operator Overloading

This project contains several Python classes created to practice **Object-Oriented Programming** and **operator overloading**.  
Each task is implemented in its own module and demonstrated through `main.py`.

---

## 📌 Implemented Classes

### **1. Money & Product**
**Files:** `money.py`, `main.py`

Features:
- Stores currency in major/minor units.
- Automatic normalization (e.g., 7.150 → 8.50).
- Methods to set and display values.
- Ability to decrease price safely.
- `Product` uses a `Money` object as its price.

---

### **2. Circle**
**File:** `circle.py`

Overloaded operators:
- `==` — compare radii.
- `<`, `>`, `<=`, `>=` — compare circumference (2πr).
- `+`, `-` — return a new circle with modified radius.
- `+=`, `-=` — modify radius in place.

---

### **3. Airplane**
**File:** `airplane.py`

Overloaded operators:
- `==` — compare airplane types.
- `<`, `>`, `<=`, `>=` — compare by max passenger capacity.
- `+`, `-` — create a new airplane with changed passenger count.
- `+=`, `-=` — modify passenger count in place (with safety checks).

---

### **4. Flat**
**File:** `flat.py`

Overloaded operators:
- `==`, `!=` — compare apartments by area.
- `<`, `>`, `<=`, `>=` — compare apartments by price.

---
