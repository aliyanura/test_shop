from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Присоединяемся к группе "notifications"
        await self.channel_layer.group_add(
            "notifications",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Убираем пользователя из группы
        await self.channel_layer.group_discard(
            "notifications",
            self.channel_name
        )

    async def send_notification(self, event):
        message = event['message']
        # Отправляем сообщение через WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
