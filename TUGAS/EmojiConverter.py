
#! Durasi: 02:45:58
message = input(">>> ")

emoji_Mapping = {
    ":)": "😁",
    ":(": "😭",
    ":|": "😐"
}

output = ""
words = message.split(" ")

for w in words:
    output = output + emoji_Mapping.get(w, w)

print(output)
