import json
import asyncio
import psutil
from channels.generic.websocket import AsyncWebsocketConsumer

class SystemConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.keep_running = True
        asyncio.create_task(self.send_metrics())

    async def disconnect(self, close_code):
        self.keep_running = False

    async def send_metrics(self):
        while self.keep_running:
            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory().percent
            storage = psutil.disk_usage('/').percent
            
            await self.send(text_data=json.dumps({
                'type': 'system_metrics',
                'cpu': cpu,
                'ram': ram,
                'storage': storage,
            }))
            await asyncio.sleep(2)

class LogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        # Simulated logs for now
        await self.send(text_data=json.dumps({
            'message': 'Connected to vic-os log stream...'
        }))
        
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message', '').strip()
        
        if message == 'help':
            resp = "Available commands: status, build, info, help"
        elif message == 'status':
            resp = "SYSTEM_STATUS: NOMINAL | UPTIME: 04:22:11 | LOAD: 12%"
        elif message == 'build':
            resp = "INITIATING BUILD SEQUENCE... [WAIT]"
            await self.send(text_data=json.dumps({'message': resp}))
            await asyncio.sleep(1)
            resp = "PARSING RECIPE.YML... DONE"
            await self.send(text_data=json.dumps({'message': resp}))
            await asyncio.sleep(1)
            resp = "BUILD SUCCESSFUL. IMAGE READY AT predicamental/vic-os.zip"
        elif message == 'info':
            resp = "VIC-OS DASHBOARD V1.0.0 | RUNNING ON DJANGO + CHANNELS"
        else:
            resp = f"Command '{message}' not recognized. Type 'help' for options."

        await self.send(text_data=json.dumps({
            'message': f'> {message}\n{resp}'
        }))
