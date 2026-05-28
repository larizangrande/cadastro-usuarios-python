# Sistema de Cadastro de Usuários

usuarios = []

while True:
    print("\n" + "=" * 30)
    print(" SISTEMA DE CADASTRO ")
    print("=" * 30)
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Buscar usuário")
    print("4 - Excluir usuário")
    print("5 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do usuário: ")
        usuarios.append(nome)
        print(f"\n✅ {nome} cadastrado com sucesso!")

    elif opcao == "2":
        if len(usuarios) == 0:
            print("\n⚠ Nenhum usuário cadastrado.")
        else:
            print("\n📋 Lista de usuários:")
            for i, usuario in enumerate(usuarios, start=1):
                print(f"{i}. {usuario}")

    elif opcao == "3":
        busca = input("Digite o nome para buscar: ")

        if busca in usuarios:
            print(f"\n✅ Usuário '{busca}' encontrado!")
        else:
            print(f"\n❌ Usuário '{busca}' não encontrado.")

    elif opcao == "4":
        excluir = input("Digite o nome que deseja excluir: ")

        if excluir in usuarios:
            usuarios.remove(excluir)
            print(f"\n🗑 Usuário '{excluir}' removido.")
        else:
            print("\n❌ Usuário não encontrado.")

    elif opcao == "5":
        print("\n👋 Encerrando o sistema...")
        break

    else:
        print("\n❌ Opção inválida!")
