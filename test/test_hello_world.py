import app
import pytest

def test_hello_world():
    assert app.hello_world() == 'Hello World'