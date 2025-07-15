# How to run our API

This project demonstrates a simple API-to-API call setup using FastAPI, intended as a starting point for an end-to-end ML pipeline.

## 🧱 Project Structure

```
ai_benchmark-quiz/
├── api1/
│   ├── main.py
│   ├── DockerFile
│   └── requirements.txt
├── api2/
│   ├── main.py
│   ├── DockerFile
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## 🚀 Running the Project

### ✅ Option 1: Run Locally (Without Docker)

#### Prerequisites:
- Python 3.10+
- `pip` and `virtualenv` installed

### Step-by-step:

Open **Terminal 1** and run API2:

```bash
cd api2
python -m venv venv && source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8001
```

Open **Terminal 2** and run API1:

```bash
cd api1
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

Test the relay endpoint:

```bash
curl http://localhost:8000/relay
```

Expected output:

```json
{"message": "Hello from API2"}
```

---

### 🐳 Option 2: Run via Docker Compose

#### Prerequisites:
- Docker Desktop installed
- Docker is running in **Linux container mode**

### Step-by-step:

From the project root:

```bash
docker-compose up --build
```

Test the API:

```bash
curl http://localhost:8000/relay
```

Expected output:

```json
{"message": "Hello from API2"}
```

### To stop the containers:

```bash
docker-compose down
```

### To view logs:

```bash
docker-compose logs -f
```
