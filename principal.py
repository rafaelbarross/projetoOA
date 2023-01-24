from time import sleep

print("""\n  === Olá estudante, isso é um Objeto de Aprendizagem (OA) ===
- O assunto que iremos ver é: The Present Continuous Tense/Inglês -\n
Não se preocupe, iremos tirar todas as suas duvidas (-_-)7

Bons estudos! :) \n""")
nome = str(input("Digite seu nome: "))
print(f"\nOlá, \033[1;36m{nome}\033[m, seja bem-vindo/a!")
cont = 0
resp_quest = [[1, 3, 2, 1, 2, 3, 1, 2, 1, 3], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
opçao = 0
while opçao != 4:
    print("\n[MENU DE OPÇÕES]")
    print("\033[1;34m1 - Conteúdo\033[m")
    print("\033[1;34m2 - Exercicios\033[m")
    print("\033[1;34m3 - Gabarito\033[m")
    print("\033[1;34m4 - Sair\033[m")
    opçao = int(input("\nDigite aqui: -> "))
    if opçao == 1:
        print("""\nThe Present Continuous Tense Usamos o Present Continuous Tense para expressar
uma ação que acontece no momento em que alguém fala.

Example: She is eating a sandwich at the moment.
We are stutying for our English test.
I am dancing now.

Formation: verb to (simple present: am, is, are) + main verb with the -ing.

1ª. Verbos terminados em "e" perdem o "e" e recebem -ing.
Examples: dance = dancing
                    move = moving 
                    receive = receiving
Obs.: verbos terminados em "ee" não seguem essa regra.
agree = agreeing 
see = seeing 
fee = feeing

2ª Regra: verbos terminados em "ie" têm essa terminação trocada por "y" e recebem -ing.
Examples: lie = lying
	       tie = tying

3ª Regra: verbos monossílabos terminados em c-v-c (consoante-vogal-consoante) têm a última consoante dobrada e depois recebem a terminação -ing.	
Examples: run = running 
	  stop = stopping
	  prefer = preferring
          visit = visiting
          open = opening
          arrest = arresting
          begin = beginning
          happen = happening
          sing = singing
          ski = skiing""")

    elif opçao == 2:

        print("\nPreencha os espaços em branco com o Present Continuous Tense dos verbos entre parênteses.")

        while True:
            resp_quest[1][0] = input(
                "\n\033[1;31;47mQuestão 1\033[m. Jane _______ dinner now. (cook)\n1- is cooking\n2- are cooking\n3- am cooking\nR: ")
            if resp_quest[1][0].isdigit() and 1 <= int(resp_quest[1][0]) <= 3:
                resp_quest[1][0] = int(resp_quest[1][0])
                break

            else:
                print("\033[1;31m\nInforme uma opção válida para a resposta!\033[m")
              
                    
        while True:
            resp_quest[1][1] = input("\n\033[1;31;47mQuestão 2\033[m. Mary and I ______ on a new project. (work)\n1- am working\n2- is working\n3- are working\nR: ")
            if resp_quest[1][1].isdigit() and 1 <= int(resp_quest[1][1]) <= 3:
                resp_quest[1][1] = int(resp_quest[1][1])
                break

            else:
                print("\033[1;31m\nInforme uma opção válida para a resposta!\033[m")
                                                                                                        
        while True:
            resp_quest[1][2] = input(
                "\n\033[1;31;47mQuestão 3\033[m. It _____ a lot outside.  (rain)\n1- are raining\n2- is raining\n3- am raining\nR: ")
            if resp_quest[1][2].isdigit() and 1 <= int(resp_quest[1][2]) <= 3:
                resp_quest[1][2] = int(resp_quest[1][2])
                break
            else:
                print("\033[1;31m\nInforme uma opção válida para a resposta!\033[m")
                                                   
        while True:
            resp_quest[1][3] = input(
                "\n\033[1;31;47mQuestão 4\033[m. Billy _______ a letter to his mother. (write)\n1- is writing\n2- am writing\n3- are writing\nR: ")
            if resp_quest[1][3].isdigit() and 1 <= int(resp_quest[1][3]) <= 3:
                resp_quest[1][3] = int(resp_quest[1][3])
                break
            else:
                print("\033[1;31m\nInforme uma opção válida para a resposta!\033[m")     
                
        while True:
            resp_quest[1][4] = input(
                "\n\033[1;31;47mQuestão 5\033[m. My mother ______ a movie. (watch)\n1- are watching\n2- is watching\n3- am watching\nR:")
            if resp_quest[1][4].isdigit() and 1 <= int(resp_quest[1][4]) <= 3:
                resp_quest[1][4] = int(resp_quest[1][4])
                break
            else:
                print("\033[1;31m\nInforme uma opção válida para a resposta!\033[m")
              
        while True:
            resp_quest[1][5] = input(
                "\n\033[1;31;47mQuestão 6\033[m. The girls _____ volleyball. (play)\n1- am playing\n2- is playing\n3- are playing\nR: ")
            if resp_quest[1][5].isdigit() and 1 <= int(resp_quest[1][5]) <= 3:
                resp_quest[1][5] = int(resp_quest[1][5])
                break
            else:
                print("\033[1;31m\nInforme uma opção válida para a resposta!\033[m") 
                                                                                                          
        while True:
            resp_quest[1][6] = input(
                "\n\033[1;31;47mQuestão 7\033[m. I ______ my shoes. (tie)\n1- am tying\n2- is tying\n3- are tying\n\nR: ")
            if resp_quest[1][6].isdigit() and 1 <= int(resp_quest[1][6]) <= 3:
                resp_quest[1][6] = int(resp_quest[1][6])
                break
            else:
                print("\033[1;31m\nInforme uma opção válida para a resposta!\033[m") 
                                                                                            
        while True:
            resp_quest[1][7] = input(
                "\n\033[1;31;47mQuestão 8\033[m. The Gordons _______ at the moment. (travel)\n1- is traveling\n2- are traveling\n3- am traveling\nR: ")
            if resp_quest[1][7].isdigit() and 1 <= int(resp_quest[1][7]) <= 3:
                resp_quest[1][7] = int(resp_quest[1][7])
                break
            else:
                print("\033[1;31m\nInforme uma opção válida para a resposta!\033[m")

        while True:
            resp_quest[1][8] = input(
                "\n\033[1;31;47mQuestão 9\033[m. We _____ for the teacher here. (wait)\n1- are waiting\n2- is waiting\n3- am waiting\nR: ")
            if resp_quest[1][8].isdigit() and 1 <= int(resp_quest[1][8]) <= 3:
                resp_quest[1][8] = int(resp_quest[1][8])
                break
            else:
                print("\033[1;31m\nInforme uma opção válida para a resposta!\033[m")
                                                                                
        while True:
            resp_quest[1][9] = input(
                "\n\033[1;31;47mQuestão 10\033[m. Robert and Donavan _____ together. (study)\n1- am studying\n2- is studying\n3- are studying\nR: ")
            if resp_quest[1][9].isdigit() and 1 <= int(resp_quest[1][9]) <= 3:
                resp_quest[1][9] = int(resp_quest[1][9])
                break

            else:
                print(
                    "\033[1;31m\nInforme uma opção válida para a resposta!\033[m")

        for i in range(10):
            if resp_quest[1][i] == resp_quest[0][i]:
                cont = cont + 1
        print(f"\n\033[1;32mParabéns\033[m \033[1;36m{nome}\033[m, você acertou \033[1;32m{cont}\033[m de \033[1;32m10\033[m questoes!")

    elif opçao == 3:
        for i in range(10):
            print(F"\nQuestão: {i + 1}\nResposta: {resp_quest[0][i]}\n")

    elif opçao == 4:
        print("\nFinalizando...")
    else:
        print("\033[1;31mOpção inválida. Tente novamente!\033[m")
    sleep(2)
print("\033[1;32mVocê saiu do programa!\n\033[m")