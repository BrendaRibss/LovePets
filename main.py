# Oi professor, para este trabalho eu recebi ajuda do meu irmão, estou tendo muitas dificuldades na sua matéria e pedi ajuda para ele. É um trabalho que para mim é complexo mas estou usando ele para me preparar para o exame também.
# fiz o código pensando que apenas o ADM pode mexer nele, realmente como uma sistema usado nas lojas de petshop, onde o operador tem acesso a tudo
# Primeiro login é de ADM. Informações de login abaixo!
usuariosA = [{"nome": "Brenda", "senha": "9693", "tipo": "A"}]
# listas vazias que serão preenchidas pelos dados informados mais a frente do código
clientes = []
administradores = []
pets = []
servicos = []

# sistema de login, que foi passado em sala de aula. Puxa primeiro o login do ADM já cadastrado e depois só quando é pedido em uma das opções para cadastrar um novo ADM ou um novo usuário
while True:
    login = False 

    if len(usuariosA) == 0:
        print("Não achamos nenhum usuário cadastrado. \nSe desejar acessar, cadastre um usuário:")
        nomeUsuario = input("Nome de login: ")
        senha = input("Digite uma senha: ")
        usuariosA.append({"nome": nomeUsuario, "senha": senha, "tipo": "A"})
        login = True
    else:
        nomeUsuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        for usuario in usuariosA:
            if nomeUsuario == usuario["nome"] and senha == usuario["senha"]:
                print("Usuário Autenticado!")
                login = True
                break

    if login:
        break
    else:
        print("Usuário ou senha inválidos! Tente novamente!")

# Menu principal feito com função. Aqui consta as opções que dispóniveis para uso do adm
def menu():
    while True:
        print("\n\t ========== Bem-Vindo ao Love Pets========")
        print("\n\tAqui você encontra o que seu pet precisa!")
        print("\n1. Login Cliente") # usado quando tem um cliente cadastrado, necessário fazer o cadastro primeiro
        print("2. Login Administrador") # usado quando tem um adm cadastrado, necessário fazer o cadastro primeiro
        print("3. Cadastrar Cliente")
        print("4. Cadastrar Administrador")
        print("5. Cadastrar Pet")
        print("6. Cadastrar Serviço")
        print("7. Gerar Relatório de Serviços")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")
        # cada opção está chamando a função que dará início ao que foi escolhido
        if opcao == "1":
            login_usuario(clientes, "Cliente")
        elif opcao == "2":
            login_usuario(administradores, "Administrador")
        elif opcao == "3":
            cadastrar_cliente()
        elif opcao == "4":
            cadastrar_administrador()
        elif opcao == "5":
            cadastrar_pet()
        elif opcao == "6":
            cadastro_servico()
        elif opcao == "7":
            gerar_relatorio()
        elif opcao == "8":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")

menu() # como o menu foi feito usando função, é necessário que ele seja chamado para que seja executado

# função para fazer novos logins, de usuário e adm
def login_usuario(usuarios, tipo_usuario):
    print(f"\n\t =====Login {tipo_usuario}=====")
    email = input("Digite o email: ")
    senha = input("Digite a senha: ")
    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            print(f"{tipo_usuario} logado com sucesso!")
            return True
    print("Credenciais inválidas.")
    return False

# Funções para novos cadastros ( clientes, adms, pets e informar o serviço a ser prestado)
def cadastrar_cliente():
    print("\n\t===== Cadastrar Cliente =====")
    nomeCompleto = input("Nome do cliente: ")
    email = input("Email: ")
    cpf = input("Informe o seu CPF:")
    sexo = input("Feminino ou masculino?")
    senha = input("Senha: ")
    cliente = {"nome": nomeCompleto, "email": email, "CPF": cpf,"sexo": sexo, "senha": senha}
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def cadastrar_administrador():
    print("\n\t===== Cadastrar Administrador=====")
    nome = input("Nome do administrador: ")
    email = input("Email: ")
    senha = input("Senha: ")
    administrador = {"nome": nome, "email": email, "senha": senha}
    administradores.append(administrador)
    print("Administrador cadastrado com sucesso!")

#aqui você irá cadastrar e detalhar sobre o seu pet
def cadastrar_pet():
    print("\n\t===== Cadastrar Pet =====")
    nome = input("Nome do seu pet: ")
    especie = input("Espécie (cachorro, gato, etc.): ")
    tamanho = input("Seu pet é porte pequeno, médio ou grande?")
    comportamento = input("Como é o comportamento do seu pet?")
    idade = input("Idade: ")
    dono = input("Nome do dono: ")
    cpfDono = input("Informe o CPF do dono do pet:")
    pet = {"nome": nome, "especie": especie, "tamanho": tamanho, "comportamento": comportamento, "idade": idade, "dono": dono, "CPF do dono": cpfDono}
    pets.append(pet)
    print("Pet cadastrado com sucesso.")

# aqui estão os serviços possíveis e os dados que serão disponibilizados no relatório
def cadastro_servico():
    print("\n--- Serviços ---")
    cliente = input("Nome do dono do pet: ")
    nome_pet = input("Nome do pet: ")
    tipo_servico = input("Tipo de serviço (banho, tosa, consulta): ")
    descricao = input("Descrição: ")
    valor = float(input("Valor: "))
    servico = {"cliente": cliente,"nome_pet": nome_pet, "tipo_servico": tipo_servico, "descricao": descricao, "valor": valor}
    servicos.append(servico)
    print("Serviço cadastrado com sucesso.")

# relatório com os serviçõs prestados para o pet 
def gerar_relatorio():
    print("\n--- Relatório de Serviços ---")
    for servico in servicos:
        print(f"Pet: {servico['nome_pet']}")
        print(f"Serviço: {servico['tipo_servico']}")
        print(f"Descrição: {servico['descricao']}")
        print(f"Valor: R${servico['valor']:.2f}")
        print("-" * 20)



