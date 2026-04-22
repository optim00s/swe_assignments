import random

# Spell out number
num_dict = {
    1 : "one",
    2 : "two",
    3 : "three"
}

user_choice = int(input("Type 1 or 2, 3: "))
print(num_dict[user_choice])

# Translation
lang_dict = {
    0 : "mon",
    1 : "rouge",
    2 : "stylo"
}

user_text = input("Type my red pen for translate to French: ").strip().split()
for idx in range(len(user_text)):
    user_text[idx] = lang_dict[idx]
print(" ".join(user_text))

# Capital Game
capital_dict = {
    "Azerbaijan" : "Baku",
    "China" : "Beijing",
    "USA" : "Washington",
    "Hong Kong" : "Hong Kong",
    "Switzerland" : "Bern",
    "Singapore" : "Singapore",
    "Japan" : "Tokyo",
    "Italia" : "Rome",
    "Germany" : "Berlin",
}

while True:
    country = random.choice(list(capital_dict.keys()))
    user_type = input(f"Guess the capital of {country} (for exit type q): ").strip().lower()

    if user_type == "q":
        break

    if user_type == capital_dict[country].strip().lower():
        print("Correct")
    else:
        print(f"Wrong, capital of {country} is {capital_dict[country]}")
