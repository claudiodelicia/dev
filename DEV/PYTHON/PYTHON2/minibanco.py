while True:
    



    while True:
       criar_login = input("deseja criar um novo login  ? (sim/não): ").strip().lower()
    
       if criar_login == "sim":
           print("acessando...")
           usuario = input("qual o nome do usuario ? ")
           guardar = input("oque voce deseja guardar ? ")
           senha = input("qual a senha voce deseja escolher ? ")
           print("senha escolhida")
        
           break
        

       elif criar_login == "não":
            

            login_jafeito = input("voce ja tem algum login ? (sim/não): ").strip().lower()

            if login_jafeito == "sim":
                print("saindo...")
                break

            elif login_jafeito =="não":

                print("Repetindo a pergunta...")

            else:

                print("Resposta inválida! Digite 'sim' ou 'não'.")





       else:
           print("Resposta inválida! Digite 'sim' ou 'não'.")


        
   
   
   
   
    def validador():
            while True:
                 usuariopergunta = input("qual o usuario ? ")
                 if usuario == usuariopergunta:
                     senhapergunta = input("qual a senha ? ")
                     if senha == senhapergunta:
                        print("isso estava guardado: ")
                        print(guardar)
                        break
                     else:
                         senha_erro = input("usuario errado, deseja tentar denovo ? (sim/não): ").strip().lower()
                         if senha_erro == "sim":
                            print("Repetindo a pergunta...")
                         elif senha_erro == "não":
                             print("pulando...")
                             break
                         else:
                             print("Resposta inválida! Digite 'sim' ou 'não'.")
                 else:
                
                   user_erro = input("usuario errado, deseja tentar denovo ? (sim/não): ").strip().lower()
                   if user_erro == "sim":
                      print("Repetindo a pergunta...")
                   elif user_erro == "não":
                      print("pulando...")
                      break
                   else:
                         print("Resposta inválida! Digite 'sim' ou 'não'.")

        







   
    def acesso():
        while True:
           resposta = input("Você deseja acessar? (sim/não): ").strip().lower()
    
           if resposta == "sim":
                print("acessando...")
                validador()
                break
        

           elif resposta == "não":
                refazer_login = input("voce deseja criar outro login ? (sim/não): ").strip().lower()

                if refazer_login == "sim":
                   print("saindo...")
                   break

                elif refazer_login =="não":

                   print("Repetindo a pergunta...")

                else:

                    print("Resposta inválida! Digite 'sim' ou 'não'.")

    acesso()


                
                
