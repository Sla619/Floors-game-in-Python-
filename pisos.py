print("PISO 1")
andar=1
resposta=input("20 x 45 = ")
if resposta=="900":
    print("¡Fantástico! Subiste al piso 2.")
    andar=2
    print("PISO 2")
    resp_two=input("35 x 40 = ")
    if resp_two=="1400":
        print("¡Fantástico! Subiste al piso 3.")
        andar=3
        print("PISO 3")
        resp_three=input("120 ÷ 20 = ")
        if resp_three=="6":
            print("¡Fantástico! Subiste al piso 4.")
            andar=4
            print("PISO 4")
            resp_four=input("57 x 8 = ")
            if resp_four=="456":
                print("¡Fantástico! Subiste al piso 5.")
                andar=5
                print("PISO 5")
                resp_five=input("(45 - 6) x 34 = ")
                if resp_five=="1326":
                    print("¡Hurra!")
                    andar=6
                    print("PISO HURRA")
                    print("¡Lograste superar el obstáculo matemático y conquistar los 5 pisos!")
                else:
                    print(f"Lo hiciste bien, total de pisos completados: {andar-1}, respuesta: 1326")
            else:
                print(f"Lo hiciste bien, total de pisos completados: {andar-1}, respuesta: 456")
        else:
            print(f"Lo hiciste bien, total de pisos completados: {andar-1}, respuesta: 6")
    else:
        print(f"Lo hiciste bien, total de pisos completados: {andar-1}, respuesta: 1400")
else:
    print(f"Lo hiciste bien, total de pisos completados: {andar-1}, respuesta: 900")