# 🌸 Iris Flower Classification - Dockerized App

## 📌 Project Overview
This is a **full-stack machine learning web application** that classifies iris flowers based on their petal and sepal measurements. The project consists of:

- **Frontend:** Built using **Vue.js** + TypeScript (for UI interaction)
- **Backend:** A **Flask API** serving a trained machine learning model
- **Machine Learning Model:** A **RandomForestClassifier** trained on the Iris dataset
- **Docker:** The entire project is containerized for easy deployment

## 🏗️ Technologies Used
| Component  | Technology |
|------------|-----------|
| **Frontend**  | Vue.js, TypeScript, Vite |
| **Backend**   | Flask, Python, Scikit-learn |
| **ML Model**  | RandomForestClassifier |
| **Database**  | N/A (Model trained using Iris dataset from sklearn) |
| **State Management** | Pinia (for Vue.js) |
| **Testing**   | Vitest |
| **Deployment** | Docker & Docker Compose |

---

## 🚀 How to Run Locally

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/ArnoldMathew1998/Iris-Flower-Classification.git
cd iris-flower-classification
```

### **2️⃣ Build & Run with Docker**
Ensure you have **Docker** and **Docker Compose** installed. Then, run:
```sh
docker-compose up --build
```
This will build and run both the **frontend (Vue)** and **backend (Flask)**.

### **3️⃣ Access the Application**
- 🌍 **Frontend (Vue.js UI):** `http://localhost:5173`
- ⚙️ **Backend API (Flask):** `http://localhost:5000`

---

## 🛠️ Development & Setup

### **Manual Setup Without Docker**
#### **Backend Setup**
```sh
cd Backend
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python app.py
```
Runs the **Flask API** at `http://127.0.0.1:5000`

#### **Frontend Setup**
```sh
cd Frontend/iris-classifier
npm install
npm run dev
```
Runs the **Vue.js UI** at `http://127.0.0.1:5173`

---

## 📡 API Endpoints
| Method | Endpoint       | Description |
|--------|---------------|-------------|
| `POST` | `/predict`    | Predict flower species (expects JSON input) |

#### Example Request:
```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```
#### Example Response:
```json
{
  "prediction": "setosa"
}
```


## 💡 Contributing
Feel free to fork the repo and create pull requests! 😊

---

## 📜 License
MIT License © 2025 Arnold Mathew

