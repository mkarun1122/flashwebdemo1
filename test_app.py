# test_app.py
import unittest
from app import app

def test_app_exists():
    assert app is not None
