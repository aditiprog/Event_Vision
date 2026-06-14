 # ⚡ EventVision
## Event-Driven Neuromorphic Video Analytics

EventVision is a real-time video analytics system that uses computer vision and neuromorphic processing concepts to detect movement, generate event spikes, and display live analytics through a web dashboard.

The system converts normal camera frames into event-based data, processes activity using an SNN-inspired pipeline, and provides real-time monitoring through a React dashboard.

---

# 🚀 Features

- Real-time camera motion detection
- Frame difference based event generation
- Spike event counting
- Neuromorphic computing workflow
- SNN processing using Brian2
- STDP-inspired learning pipeline
- FastAPI backend API
- React + Vite dashboard
- Live activity monitoring
- Data efficiency calculation
- Vercel frontend deployment

---

# 🏗️ System Architecture

```
Camera
   |
   ↓
OpenCV Event Generation
   |
   ↓
Neuromorphic Processing
   |
   ↓
SNN / STDP Pipeline
   |
   ↓
FastAPI Backend
   |
   ↓
React Dashboard
   |
   ↓
Vercel Deployment
```

---

# 📂 Project Structure

```
Event_Vision
│
├── backend
│   ├── main.py
│   ├── final_eventvision.py
│   └── Python modules
│
├── frontend
│   ├── src
│   ├── package.json
│   └── React files
│
├── README.md
└── .gitignore
```

---

# 🛠️ Technologies Used

## Backend

- Python
- OpenCV
- NumPy
- Brian2
- FastAPI
- Uvicorn

## Frontend

- React
- Vite
- JavaScript
- CSS

## Deployment

- GitHub
- Vercel

---

# ⚙️ Installation & Setup

## Backend Setup

Go to backend folder:

```bash
cd backend
```

Install dependencies:

```bash
pip install opencv-python numpy brian2 fastapi uvicorn requests
```

Run FastAPI server:

```bash
uvicorn main:app --reload
```

Run the vision system:

```bash
python final_eventvision.py
```

---

## Frontend Setup

Go to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run React application:

```bash
npm run dev
```

Open:

```
http://localhost:5173/
```

---

# 📊 Dashboard

The dashboard displays:

- Current movement status
- Spike event count
- Data efficiency percentage

Example:

```
Status:
Movement Detected

Spike Events:
XXXX

Data Saved:
XX%
```

---

# 🌐 Project Links

## Live React Dashboard

https://frontend-7obzm9ald-aditi-s-projects2521.vercel.app


## Vercel Deployment

https://vercel.com/aditi-s-projects2521/frontend

---

# 🎥 Demo Video


```

https://github.com/user-attachments/assets/c824674b-5096-4c3d-aeec-f907ba39ad3a





---

# 🔮 Future Improvements

- Public deployment of FastAPI backend
- Real-time graphs and analytics
- Better SNN training
- Event camera hardware support
- User authentication

---

# 👩‍💻 Author

---

# 👥 Team

## **XOR**

This project was developed as a group project by:

- **Aditi**
- **Sandeep**
- **Rachita**
- **Sachin**
- **Deepakkumar**

---

# 👩‍💻 Project

**EventVision - Event Driven Neuromorphic Video Analytics**

A collaborative project focused on real-time event-based video processing, neuromorphic computing concepts, and intelligent analytics.

---

EventVision - Event Driven Neuromorphic Video Analytics
