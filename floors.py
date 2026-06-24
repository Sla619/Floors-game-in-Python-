import time

print("FLOOR 1")
andar=1
resposta=input("20 x 45 = ")
if resposta=="900":
    print("Great, you went to: Floor 2")
    andar=2
    print("FLOOR 2")
    resp_two=input("35 x 40 = ")
    if resp_two=="1400":
        print("Great, you went to: Floor 3")
        andar=3
        print("FLOOR 3")
        resp_three=input("120 ÷ 20 = ")
        if resp_three=="6":
            print("Great, you went to: Floor 4")
            andar=4
            print("FLOOR 4")
            resp_four=input("57 x 8 = ")
            if resp_four=="456":
                print("Great, you went to: Floor 5")
                andar=5
                print("FLOOR 5")
                resp_five=input("(45 - 6) x 34 = ")
                if resp_five=="1326":
                    print("Yay!")
                    andar=6
                    print("FLOOR: YAY")
                    print("You managed to beat the math and conquered all 5 floors!")
                    time.sleep(10)
                    quit
                else:
                    print(f"You were good, successful floors: {andar-1}, answer: 1326")
            else:
                print(f"You were good, successful floors: {andar-1}, answer: 456")
        else:
            print(f"You were good, successful floors: {andar-1}, answer: 6")
    else:
        print(f"You were good, successful floors: {andar-1}, answer: 1400")
else:
    print(f"You were good, successful floors: {andar-1}, answer: 900")
