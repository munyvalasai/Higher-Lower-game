import random
import os

logo = """
    /$$   /$$ /$$           /$$                                           /$$                                                  
| $$  | $$|__/          | $$                                          | $$                                                  
| $$  | $$ /$$  /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$       | $$        /$$$$$$  /$$  /$$  /$$  /$$$$$$   /$$$$$$ 
| $$$$$$$$| $$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$      | $$       /$$__  $$| $$ | $$ | $$ /$$__  $$ /$$__  $$
| $$__  $$| $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/      | $$      | $$  \ $$| $$ | $$ | $$| $$$$$$$$| $$  \__/
| $$  | $$| $$| $$  | $$| $$  | $$| $$  | $$| $$_____/| $$            | $$      | $$  | $$| $$ | $$ | $$| $$_____/| $$      
| $$  | $$| $$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$| $$            | $$$$$$$$|  $$$$$$/|  $$$$$/$$$$/|  $$$$$$$| $$      
|__/  |__/|__/ \____  $$|__/  |__/ \____  $$ \_______/|__/            |________/ \______/  \_____/\___/  \_______/|__/      
               /$$  \ $$           /$$  \ $$                                                                                
              |  $$$$$$/          |  $$$$$$/                                                                                
               \______/            \______/    
"""
vs = """               
 /$$    /$$ /$$$$$$$
|  $$  /$$//$$_____/
 \  $$/$$/|  $$$$$$ 
  \  $$$/  \____  $$
   \  $/   /$$$$$$$/
    \_/   |_______/ 
"""

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 145,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 138,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'National Geographic',
        'follower_count': 135,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'Maluma',
        'follower_count': 50,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Camila Cabello',
        'follower_count': 49,
        'description': 'Musician',
        'country': 'Cuba'
    }
]

# to fromate the account data in printable formate
def data_formate(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country} "


def check_guess(guess, follwer_one, follower_two):
    if follwer_one > follower_two:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = False
account_temp = random.choice(data)

while not game_should_continue:

    account_one = account_temp
    account_two = random.choice(data)
    if account_one == account_two:
        account_two = random.choice(data)

    print(f"Compare A: {data_formate(account_one)}.")
    print(vs)
    print(f"Against B: {data_formate(account_two)}.")

    # Ask user to guess
    guess = input("Who has more follower? Type 'A'  or 'B': ").lower()

    # check user account followers
    follower_count_one = account_one["follower_count"]
    follower_count_two = account_two["follower_count"]

    os.system("cls")
    print(logo)

    is_right = check_guess(guess, follower_count_one, follower_count_two)
    if is_right:
        score += 1
        print(f"You'r right! Current score: {score}")
    else:
        game_should_continue = True
        print(f"Sorry, That's wrong. final score: {score} ")