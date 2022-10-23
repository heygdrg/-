from email.headerregistry import HeaderRegistry
import requests
import random
import os 
from os import system

caracteres =  ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j','k','l','m','n', 'o', 'p', 'q', 'r','s',
                't', 'u', 'v', 'w', 'x','y','z','0','1','2', '3','4', '5','6','7','8','9',"A","B","C","D",
                "E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]
def guild_cheker():
    while True:
        number = ""

        for i in range(8):
            number = f"{number}{random.choice(caracteres)}"
        invite = f"https://discord.gg/{number}"
        res = requests.get(f"https://discord.com/api/v9/invites/{number}").json()
        if 'rate limit' in res.get('message', ''):
            print(f"You've juste get write limite of : {res['retry_after']} second")
            exit()
        else:
            pass



guild_cheker()
