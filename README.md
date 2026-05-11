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

1. Connect your GitHub repository to Render.
2. Render will automatically detect `render.yaml`.
3. The build process uses `scripts/build.sh`.
4. The start command uses `daphne` for ASGI/WebSocket support.

## 🔧 Diagnostics
Access `/diagnostics/` after logging in to verify:
- Database connectivity
- WebSocket layer status
- REST API health
- vic-os project detection

---
(C) 2026 vic-os Project | Built for Premium Performance
