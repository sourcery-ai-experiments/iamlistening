# """
# RocketChat Testing
# """

# import asyncio
# from unittest.mock import AsyncMock

# import pytest

# from iamlistening import Listener
# from iamlistening.config import settings
# from iamlistening.platform.chat_manager import ChatManager


# @pytest.fixture(scope="session", autouse=True)
# def set_test_settings():
#     settings.configure(FORCE_ENV_FOR_DYNACONF="testingrocketchat")

# @pytest.mark.asyncio
# async def test_fixture():
#     assert settings.VALUE == "On Testing Rocket Chat"
