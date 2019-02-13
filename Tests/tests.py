import os
import tempfile

import pytest

from app import app

#-----------CONFIG BASE PARA TESTES------------
@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
 
    yield client






