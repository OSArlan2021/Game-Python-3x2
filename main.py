gamemap_1 = ["#","#","#"]
gamemap_2 = ["#","O","#"]
print(f"{(gamemap_1[0])}{(gamemap_1[1])}{(gamemap_1[2])}")
print(f"{(gamemap_2[0])}{(gamemap_2[1])}{(gamemap_2[2])}")
cordinate_x = 1
cordinate_y = 1
print(f"X={(cordinate_x)} Y={(cordinate_y)}")
rep = 0
while True:
    control = input("")
    if control == "w":
        cordinate_y = cordinate_y + 1
        gamemap_2[0] = "#"
        gamemap_2[1] = "#"
        gamemap_2[2] = "#"
        gamemap_1[cordinate_x] = "O"
        print(f"X={(cordinate_x)} Y={(cordinate_y)}")
        print(f"{(gamemap_1[0])}{(gamemap_1[1])}{(gamemap_1[2])}")
        print(f"{(gamemap_2[0])}{(gamemap_2[1])}{(gamemap_2[2])}")
    if control == "s":
        cordinate_y = cordinate_y - 1
        gamemap_1[0] = "#"
        gamemap_1[1] = "#"
        gamemap_1[2] = "#"
        gamemap_2[cordinate_x] = "O"
        print(f"X={(cordinate_x)} Y={(cordinate_y)}")
        print(f"{(gamemap_1[0])}{(gamemap_1[1])}{(gamemap_1[2])}")
        print(f"{(gamemap_2[0])}{(gamemap_2[1])}{(gamemap_2[2])}")
    if control == "a":
        if cordinate_y == 1:
            cordinate_x = cordinate_x - 1
            gamemap_2[0] = "#"
            gamemap_2[1] = "#"
            gamemap_2[2] = "#"
            gamemap_2[cordinate_x] = "O"
            print(f"X={(cordinate_x)} Y={(cordinate_y)}")
            print(f"{(gamemap_1[0])}{(gamemap_1[1])}{(gamemap_1[2])}")
            print(f"{(gamemap_2[0])}{(gamemap_2[1])}{(gamemap_2[2])}")
        if cordinate_y == 2:
            cordinate_x = cordinate_x - 1
            gamemap_1[0] = "#"
            gamemap_1[1] = "#"
            gamemap_1[2] = "#"
            gamemap_1[cordinate_x] = "O"
            print(f"X={(cordinate_x)} Y={(cordinate_y)}")
            print(f"{(gamemap_1[0])}{(gamemap_1[1])}{(gamemap_1[2])}")
            print(f"{(gamemap_2[0])}{(gamemap_2[1])}{(gamemap_2[2])}")
    if control == "d":
        if cordinate_y == 1:
            cordinate_x = cordinate_x + 1
            gamemap_2[0] = "#"
            gamemap_2[1] = "#"
            gamemap_2[2] = "#"
            gamemap_2[cordinate_x] = "O"
            print(f"X={(cordinate_x)} Y={(cordinate_y)}")
            print(f"{(gamemap_1[0])}{(gamemap_1[1])}{(gamemap_1[2])}")
            print(f"{(gamemap_2[0])}{(gamemap_2[1])}{(gamemap_2[2])}")
        if cordinate_y == 2:
            cordinate_x = cordinate_x + 1
            gamemap_1[0] = "#"
            gamemap_1[1] = "#"
            gamemap_1[2] = "#"
            gamemap_1[cordinate_x] = "O"
            print(f"X={(cordinate_x)} Y={(cordinate_y)}")
            print(f"{(gamemap_1[0])}{(gamemap_1[1])}{(gamemap_1[2])}")
            print(f"{(gamemap_2[0])}{(gamemap_2[1])}{(gamemap_2[2])}")
    if control == "/tp":
        tp_x = input("X:")
        tp_y = input("Y:")
        if tp_y == "1":
            cordinate_x = int(tp_x)
            gamemap_1[0] = "#"
            gamemap_1[1] = "#"
            gamemap_1[2] = "#"
            gamemap_2[0] = "#"
            gamemap_2[1] = "#"
            gamemap_2[2] = "#"
            gamemap_2[int(tp_x)] = "O"
            print(f"X={(cordinate_x)} Y={(cordinate_y)}")
            print(f"{(gamemap_1[0])}{(gamemap_1[1])}{(gamemap_1[2])}")
            print(f"{(gamemap_2[0])}{(gamemap_2[1])}{(gamemap_2[2])}")
        elif tp_y == "2":
            gamemap_2[0] = "#"
            gamemap_2[1] = "#"
            gamemap_2[2] = "#"
            gamemap_1[0] = "#"
            gamemap_1[1] = "#"
            gamemap_1[2] = "#"
            gamemap_1[int(tp_x)] = "O"
            print(f"X={(cordinate_x)} Y={(cordinate_y)}")
            print(f"{(gamemap_1[0])}{(gamemap_1[1])}{(gamemap_1[2])}")
            print(f"{(gamemap_2[0])}{(gamemap_2[1])}{(gamemap_2[2])}")
    rep = rep + 1
