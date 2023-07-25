import requests

# https://app.freecurrencyapi.com/  website
# url = "https://currencyapi.net/api/v1/rates?key=AZcoollxIoPSPU9G5GeS6rsOtf9odRYRATKw"
url="https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_3r8rYFxy1iOw9s2JGekZ0VarY3C6aZPsESHbEVLy"

response = requests.get(url)
# print(response)

data = response.json()
# print(data)

for x in data.keys():
    if x == "data":
        currency_data = data['data']
        for d in currency_data.keys():
            if d == 'INR':
                print("\n {} : {}".format(d, currency_data[d]))
                inr = currency_data[d]
                break

inr = data["data"]["INR"]

user_input = int(input("Enter the Dollars: "))
k = user_input*inr
print("The Dollars when converted in Indian Rupees will be equal to: {}".format(k))

