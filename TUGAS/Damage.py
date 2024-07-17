import random
#! Sebuah Projek simpel untuk memberi damage pada sebuah objek

#! PLAYER AND BOT ATTRIBUTES
Player = {
    #? Player Attributes:
    "Nama": "divo",
    "Level": 80,
    "HitPoints": 100,
    "Critical_Bonus": 2
}

Bot = {
    "Name": "Computer",
    "Lvl": 90,
    "Darah": 150,
    "Crit_Bonus": 2
}


#Todo: Damage List
Damage = {
    "Normal": 20,
    "Critical": 60,
    "Super": 100
}

#! ====================================Main============================================

Dmg = random.choice(list(Damage.values())) #? Untuk mencetak random index dari Dictionary Damage

print((Player["Critical_Bonus"] * Damage["Critical"]) - Bot["Darah"]   ) 




