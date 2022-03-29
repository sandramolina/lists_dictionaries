users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(f'Jonny\'s twitter is {users["Jonathan"]["twitter"]}')

# 2. Get Erik's hometown
print(f'Erik\'s hometown is {users["Erik"]["home_town"]}')

# 3. Get the list of Erik's lottery numbers
print(f'Erik\'s lottery numbers list is {users["Erik"]["lottery_numbers"]}')

# 4. Get the species of Avril's pet Monty
print(f'Avril\'s pet is a {users["Avril"]["pets"][0]["species"]}')

# 5. Get the smallest of Erik's lottery numbers
erik_min_lottery = min(users["Erik"]["lottery_numbers"])
print(f'Smallest Erik\'s lottery number is {erik_min_lottery}')

# 6. Return an list of Avril's lottery numbers that are even
avril_lottery_list = users["Avril"]["lottery_numbers"]
avril_lottery_list_even = []
for number in avril_lottery_list:
  if number % 2 == 0:
    avril_lottery_list_even.append(number)
print(f'List of Avril\'s lottery numbers is: {avril_lottery_list_even}')

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)
# print(users["Erik"]["lottery_numbers"])

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"
print(f'New Erik\'s hometown is {users["Erik"]["home_town"]}')

# 9. Add a pet dog to Erik called "fluffy"
new_erik_pet = {"name": "fluffy"}
users["Erik"]["pets"].append(new_erik_pet)
print(f'New Erik\'s pets collection: {users["Erik"]["pets"]}')

# 10. Add another person to the users dictionary
users["Sandra"] = {}
print(users)