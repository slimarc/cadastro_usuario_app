from register import RegisterUser


def menu():
    register = RegisterUser()

    while True:
        print("\n|-------MENU-------|")
        print("1. Cadastro de usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario pelo nome")
        print("4. Deletar usuario pelo id")
        print("5. Alterar o nome de um usuário")
        print("6. Alterar o email de um usuário")
        print("7. Alterar a idade de um usuário")
        print("8. Sair")
        option = input("\nEscolha uma opcao: ")

        if option == '1':
            register.add_user()
        elif option == '2':
            register.list_users()
        elif option == '3':
            register.search_by_name()
        elif option == '4':
            register.delete_user_by_id()
        elif option == '5':
            register.change_name_user()
        elif option == '6':
            register.change_email_user()
        elif option == '7':
            register.change_age_user()
        elif option == '8':
            print("\nAdeus =(")
            break
        else:
            print("Insira uma opção válida.\n")


if __name__ == "__main__":
    menu()

