"""
Discord Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, create_autospec, patch

import pytest
from loguru import logger
from telethon import TelegramClient, events

import iamlistening
from iamlistening import Listener
from iamlistening.config import settings
from iamlistening.platform.chat_manager import ChatManager


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testingdiscord")

@pytest.mark.asyncio
async def test_fixture():
    assert settings.VALUE == "On Testing Discord"

@pytest.fixture(name="handler")
def handler(listener):
    return listener.chat_manager.get_handler(listener.platform)

@pytest.fixture(name="listener")
def listener():
    return Listener()

@pytest.fixture(name="message")
def message():
    return "hello"

def test_handler(listener, handler):
    assert listener.platform == "discord"
    assert handler is not None

@pytest.mark.asyncio
async def test_get_handler(listener):
    get_handler = AsyncMock()
    with patch.object(listener, "start"):
        await listener.start()
        get_handler.assert_called_once
        
