import helloworld
import pytest

def test_hello_world():
    assert helloworld.hello_world() == 'Hello World'