"""
 IAmListening Main
"""

import asyncio
import threading

from loguru import logger

from iamlistening import __version__

from .config import settings
from .platform.platform_manager import PlatformManager


class Listener:

    """
    Listener Class for IAmListening.

    """

    def __init__(self, chat_platform=None):
        """
        Initialize the listener.

        Args:
            chat_platform (str): The platform to use


        Raises:
            Exception: Platform missing


        """
        self.logger = logger
        self.version = __version__
        self.platform = chat_platform or settings.chat_platform
        self.handler = None

        if self.platform is None:
            raise Exception("Platform missing")

    async def start(self):
        """
        Start the listener.

        self.handler = PlatformManager.get_handler(self.platform)
        if self.platform if None it is defaulted to telegram handler

        """

        self.handler = PlatformManager.get_handler(self.platform)

        if self.handler:
            asyncio.create_task(await self.handler.start())
 