import time

print("ANDAR 1")
andar=1
resposta=input("20 x 45 = ")
if resposta=="900":
    print("Oba, você foi pro: Andar 2")
    andar=2
    print("ANDAR 2")
    resp_two=input("35 x 40 = ")
    if resp_two=="1400":
        print("Oba, você foi pro: Andar 3")
        andar=3
        print("ANDAR 3")
        resp_three=input("120 ÷ 20 = ")
        if resp_three=="6":
            print("Oba, você foi pro: Andar 4")
            andar=4
            print("ANDAR 4")
            resp_four=input("57 x 8 = ")
            if resp_four=="456":
                print("Oba, você foi pro: Andar 5")
                andar=5
                print("ANDAR 5")
                resp_five=input("(45 - 6) x 34 = ")
                if resp_five=="1326":
                    print("Oba!")
                    andar=6
                    print("ANDAR OBA")
                    print("Você conseguiu superar a matemática e venceu todos os 5 andares!")
                    time.sleep(10)
                    quit
                else:
                    print(f"Você foi bem, andares sucedidos: {andar-1}, resposta: 1326")
            else:
                print(f"Você foi bem, andares sucedidos: {andar-1}, resposta: 456")
        else:
            print(f"Você foi bem, andares sucedidos: {andar-1}, resposta: 6")
    else:
        print(f"Você foi bem, andares sucedidos: {andar-1}, resposta: 1400")
else:
    print(f"Você foi bem, andares sucedidos: {andar-1}, resposta: 900")
