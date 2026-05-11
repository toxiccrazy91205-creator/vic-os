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

This project is configured for **Zero-Config Deployment**. You don't need to set any environment variables manually.

1. **Create a New Web Service** on Render.
2. **Connect your GitHub Repository**.
3. **Select "Docker"** as the runtime.
4. **Deploy**. The project will use an internal SQLite database by default.

> [!NOTE]
> Since Render's file system is ephemeral, data in the SQLite database will be reset on every deployment. For persistent storage, you can later connect a PostgreSQL database by simply adding the `DATABASE_URL` environment variable.

## 🔧 Diagnostics
Access `/diagnostics/` after logging in to verify:
- Database connectivity
- WebSocket layer status
- REST API health
- vic-os project detection

---
(C) 2026 vic-os Project | Built for Premium Performance
