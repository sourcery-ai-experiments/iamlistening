"""
 IAmListening Main
"""

import asyncio
import logging
import threading

from iamlistening import __version__

from .config import settings
from .platform import (
    DiscordHandler,
    MatrixHandler,
    RockerChatHandler,
    TelegramHandler,
)


class Listener:
    """ 👂 Listener class """

    def __init__(self):
        self.logger = logging.getLogger("Listener")
        self.latest_message = None
        self.loop = asyncio.get_event_loop()
        self.lock = threading.Lock()
        self.stopped = False
        self.handler = None

    async def get_info_listener(self):
        return (f"ℹ️ {__class__.__name__} {__version__}\n")

    async def start(self):
        """start"""

        if settings.telethon_api_id:
            # TELEGRAM
            telegram_handler = TelegramHandler()
            await telegram_handler.start()

        elif settings.matrix_hostname:
            # MATRIX
            matrix_handler = MatrixHandler()
            await matrix_handler.start()
        elif settings.rocket_chat_server:
            # ROCKET CHAT
            rocket_chat_handler = RockerChatHandler()
            await rocket_chat_handler.start()

        elif settings.bot_token:
            # DISCORD
            discord_handler = DiscordHandler()
            await discord_handler.start()

        else:
            self.logger.warning("Check settings")
            await asyncio.sleep(7200)
    

    async def get_latest_message(self):
        """Return the latest message."""
        while True:
            with self.lock:
                if self.latest_message is not None:
                    msg = self.latest_message
                    self.latest_message = None
                    return msg

            await asyncio.sleep(0.1)

    async def handle_message(self, message_content):
        """Handle a new message."""
        self.latest_message = message_content


    async def run_forever(self, max_iterations=None):
        """Run the listener for a specified number of iterations or until stopped."""
        iteration = 0
        while not self.stopped and (
            max_iterations is None or iteration < max_iterations):
            await self.start()
            iteration += 1

    async def post_init(self):
        return "bot is online"

    def stop(self):
        """Stop the listener."""
        self.stopped = True
