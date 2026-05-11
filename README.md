# vic-os Dashboard

A production-ready Django web application for remote monitoring and interaction with the vic-os project.

## 🚀 Features
- **Real-time Monitoring**: Live CPU/RAM/Storage metrics via WebSockets.
- **Terminal Interface**: Interactive command execution.
- **Cyberpunk UI**: Glassmorphism, neon colors, and animated gradients.
- **REST API**: Health checks and project status endpoints.
- **Diagnostics**: Built-in system health check panel.
- **Deployment Ready**: Configured for Render with PostgreSQL and WhiteNoise.

## 🛠️ Local Setup

1. **Clone & Install**:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure Environment**:
   Edit `.env` if necessary. By default, it uses SQLite for local development.

3. **Migrations & Admin**:
   ```powershell
   python manage.py migrate
   python create_admin.py
   ```
   *Default Admin: `admin` / `adminpassword`*

4. **Run Server**:
   ```powershell
   python manage.py runserver
   ```
   Access at `http://127.0.0.1:8000`

## ☁️ Deployment (Render)

1. **Create a New Web Service** on Render.
2. **Connect your GitHub Repository**.
3. **Select "Docker"** as the runtime (Render will automatically find the `Dockerfile`).
4. **Environment Variables**:
   - `SECRET_KEY`: (generate one)
   - `ALLOWED_HOSTS`: `.render.com`
   - `DEBUG`: `False`
   - `DATABASE_URL`: (from your Render Postgres instance)
5. **Render will build and deploy** the container automatically.

## 🔧 Diagnostics
Access `/diagnostics/` after logging in to verify:
- Database connectivity
- WebSocket layer status
- REST API health
- vic-os project detection

---
(C) 2026 vic-os Project | Built for Premium Performance
