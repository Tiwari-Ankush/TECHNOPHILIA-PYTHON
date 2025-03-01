import requests
import matplotlib.pyplot as plt


# GETTING DATA 
def get_pokemon_data():
    poke_name = input("Enter the name of Pokemon: ")
    url = "https://api.pokemontcg.io/v1/cards?name={}".format(poke_name)
    response = requests.get(url)
    return response.json()


# PLOTING A DATA 
def plot_pokemon_image(recieved_data):
    url_data = requests.get(recieved_data["cards"][1]["imageUrl"])
    with open('./MODULE-08/pokemon2.png','wb') as f:
        for item in url_data.iter_content(1024):
            f.write(item)

    image_data = plt.imread('./MODULE-08/pokemon2.png')
    plt.imshow(image_data)
    plt.show()          


if __name__ == "__main__":
    recieved_data = get_pokemon_data()
    plot_pokemon_image(recieved_data)

  