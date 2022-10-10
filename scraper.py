import requests

class Scraper:

    def __init__(self) -> None:
        self.number = 10

    def get_response(self):
        url = "https://pokeapi.co/api/v2/pokemon"
        payload = {
            'limit': self.number,
            'offset': 0
        }

        response = requests.get(url, params=payload)
        if response.ok:
            return response
        else:
            print("unable to get suitable response")
    
    def get_data(self, response):
        pokemon_data = response.json()

        return pokemon_data["results"]
    
    def extract_data(self, data):
        pokemon_list = []

        for item in data:
            response = requests.get(item["url"])

            extra_data = response.json()
            ability = extra_data["abilities"][0]["ability"]["name"]
            experience = extra_data["base_experience"]
            height = extra_data["height"]

            details = {
                "name": item["name"],
                "ability": ability,
                "experience": experience,
                "height": height
            }

            pokemon_list.append(details)
        
        return pokemon_list






    
