import os
player = {"nome": "python", "x": 0, "y": 0}

def andar(direcao):
    if direcao == "d":
        player['x'] +=1
    elif direcao == "a":
        player['x'] -=1
    elif direcao == "w":
        player['y'] -=1
    elif direcao == "s":
        player['y'] +=1

while True:
    os.system('clear')

    print("------------------------------------")
    for y in range(5):
        print("\n")
        for x in range(10):
            if player['x'] == x and player['y'] == y:
                print("🐍", end="")
            else:
                print("🟩", end="")
    print("\n\n------------------------------------")


    direcao = input("proxima direção {w,s,a,d}: ")
    andar(direcao)