import importlib
import sys
import types
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

@pytest.fixture
def main_module(monkeypatch):
    fake_google = types.ModuleType("googlesearch")
    fake_google.search = lambda *args, **kwargs: []
    # Ensure the project root is on sys.path
    root = Path(__file__).resolve().parent.parent
    monkeypatch.syspath_prepend(str(root))
    monkeypatch.setitem(sys.modules, "pyautogui", MagicMock())
    monkeypatch.setitem(sys.modules, "googlesearch", fake_google)
    if "main" in sys.modules:
        del sys.modules["main"]
    module = importlib.import_module("main")
    return module


def test_get_current_track_playing(main_module):
    track = {
        "is_playing": True,
        "item": {
            "name": "Title",
            "artists": [{"name": "Artist"}]
        }
    }
    with patch("spotipy.Spotify.current_user_playing_track", return_value=track):
        assert main_module.get_current_track() == "Artist Title"


def test_get_current_track_none(main_module):
    with patch("spotipy.Spotify.current_user_playing_track", return_value=None):
        assert main_module.get_current_track() is None
