'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'TestSecret'
TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjE1dEhKZ0NJOUlqTFF4R3p6dVk2TiJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFjay11ZGFjaXR5LW5kZy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjMyOGY1YWVkOGQ5MGIyNDc0ODE0ZDY3IiwiYXVkIjoiZGNvbnRhaW5lciIsImlhdCI6MTY2NDQ4MTI5MCwiZXhwIjoxNjY0NTUzMjkwLCJhenAiOiJpMTVtZ3NUMUp3SEoxcGJuWkd4RzRTeHMxRVlMMWEwVyIsInNjb3BlIjoiIn0.svcvDIT0Wu5IZZR4ibxv6PiuxXDuWWYLXOJYunwvm_BJ4oEbzg_Vwndb20r0Pozy-Ebt2c-faJp-0AA9T2rC7F6LaV_IBQppcGzzjBM6lnVijIVA_U6Vw08YC7R9Azp1XcwabXju3Is_WI_xvxeamV52DmqQFPwNBxLYAacamFU9Gq5hv-bnGOmSOPuWFov9P6dkEERDK87gzsaS7iX5wAouY8fvqFaAhVXK8cVtNYkkwyTmS_U03cujR7qPSoNuXLWEBFlGHm1uYpUdr8tKDu8DMgDhA8SAi527xT5low48dOm21ITEJNszd06oC9qQ_bo9JVBrO0HNtRPLC8qRMQ'
EMAIL = 'jean@gmail.com'
PASSWORD = '2002'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
