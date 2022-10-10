import unittest
import requests

class FlaskTest(unittest.TestCase):

    def test_get_response(self):
        resp = requests.get(f"https://pokeapi.co/api/v2/pokemon?limit=10&offset=0")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(len(data["results"]), 10)
    
    
    def test_get_pokemon(self):
        response = requests.get("http://127.0.0.1:5000/pokemon")
        self.assertEqual(response.status_code, 200)
    


unittest.main()