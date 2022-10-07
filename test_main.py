'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'TestSecret'
TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjE1dEhKZ0NJOUlqTFF4R3p6dVk2TiJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFjay11ZGFjaXR5LW5kZy51cy5hdXRoMC5jb20vIiwic3ViIjoiaVVwUGx3SHN6ek1nMHFNMlFPSmF0SUNSUU04cXJtcmVAY2xpZW50cyIsImF1ZCI6ImRlcGxveS1jb250YWluZXIiLCJpYXQiOjE2NjUxNTQwMzMsImV4cCI6MTY2NjAxODAzMywiYXpwIjoiaVVwUGx3SHN6ek1nMHFNMlFPSmF0SUNSUU04cXJtcmUiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6W119.j6x8PWKik3ifoLhh9S1h4HJQGGLg_v0RPdAiUhpqTG9kLwqP_1jFrskdiaV_A7vjfaZknKBeZ4PrueldbrypDFL4IzT0zzC4ecOnFY_dKSWddkNiDYeIsrtuyD5uhk9BwIh3wj2oZ57XDxOku_58TLwv45tFZqMpXEzR3b82i8ZXzRyr640S74j2NHiZk3qIeEIjdnyLMLwiPNlI2styij4BLP2MAkRY6qRiFpkEOhjm-O5syqknopCaxDOxMOS8ZkGf2JlyLwEPx-smUmi_RvFzeYeuWRirmeK2nsGFQRP6DPPCfNbB5D-73TWIBUhTRjjrHvL28ZGKonZ1HIJqdg'
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
    assert False 


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
