person = input("qual o personagem de harry potter?")

if person == "harry potter" or person == "harry" or person == "hermione" or person == "hermione granger" or person == "rony weasley" or person =="rony":
    print(f"o personagem {person} e da casa Grifnoria")

elif person == "draco malfoy" or person == "draco":
    print(f"o personagem {person} e da casa Sonserina")

elif person == "luna lovegood" or person == "luna":
    print(f"o personagem {person} e da casa Cornival")

elif person == "cedric" or person == "cedric diggory":
    print(f"o personagem {person} e da casa Lufa-Lufa")

else:
    print(f"personagem não encontrado")