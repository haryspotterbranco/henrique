senha_secreta = "python123"
senha_digitada = ""

while senha_digitada != senha_secreta:
    senha_digitada = input("Digite a senha: ")
    
    if senha_digitada == senha_secreta:
        print("\nAcesso Liberado!")
    else:
        print("Senha incorreta. Tente novamente.\n")