import random
#! Sebuah Projek simpel untuk memberi damage pada sebuah objek

#! PLAYER AND BOT ATTRIBUTES
Player = {
    #? Player Attributes:
    "Nama": "divo",
    "Level": 80,
    "HitPoints": 100,
}

Bot = {
    "Name": "Computer",
    "Lvl": 90,
    "Darah": 150,
}


#Todo: Damage List
Damage = {
    "Normal": 20,
    "Super": 60,
    "Critical": 100
}

#! ====================================Main============================================

Dmg = random.choice(list(Damage.values())) #? Untuk mencetak random index dari Dictionary Damage