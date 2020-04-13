file = open("Correos.txt", "r")
email_lists = []
file = file.read().rstrip().split(",")

for txt in file:
    if "@" in txt:
        email_lists.append((txt.split("\n")[0]).replace("\"",""))

file = open("Lista_Correos.txt", "w")

for line in email_lists:
    file.write(line + "\n")



