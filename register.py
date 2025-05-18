from user import User


class RegisterUser:
    def __init__(self):
        self.users = []

    def add_user(self):
        name = input("Insira o nome: ")
        email = input("Insira o email: ")
        age = int(input("Insira a idade: "))

        try:
            user = User(name, email, age)
            self.users.append(user)
            print("\nUsuário cadastrado =)\n")
        except Exception as e:
            print(f'Erro ao cadastrar o usuário: {e}')

    def delete_user_by_id(self):
        id_delete = int(input("\nInsira o id do usuário que deseja deletar: "))
        user_delete = None

        for user in self.users:
            if user.id == id_delete:
                user_delete = user
                break

        if user_delete:
            self.users.remove(user_delete)
            print(f"\nUsuário de ID {id_delete} removido do banco")
        else:
            print(f"\nUsuário de ID {id_delete} não encontrado")

    def list_users(self):
        if not self.users:
            print("\nO banco de dados de usuarios esta vazio.")
            return
        print("|------USUARIOS------|")
        for user in self.users:
            print(f"{user}")

    def search_by_name(self):
        name_searched = input ("\nInsira o nome do usuario para busca-lo: ").title()
        found = []

        for user in self.users:
            if user.name == name_searched:
                found.append(user)

        if found:
            print(f"\nOs usuarios encontrados com  nome '{name_searched}':")
            for user in found:
                print(user)
        else:
            print(f"\nNenhum usuario presente no banco de dados.")

    def change_name_user(self):
        id_user = int(input("Insira o id do usuário que deseja trocar informações: "))
        for user in self.users:
            if user._id == id_user:
                print(f"{user}")
            new_name = input("Insira o novo nome do usuário: ")
            user.change_name(new_name)
            break

    def change_email_user(self):
        id_user = int(input("Insira o id do usuário que deseja trocar informações: "))
        for user in self.users:
            if user._id == id_user:
                print(f"{user}")
            try:
                new_email = input("Insira o novo email do usuário: ")
                user.change_email(new_email)
            except Exception as e:
                print(f'Erro ao trocar email do usuário: {e}')
            break

    def change_age_user(self):
        id_user = int(input("Insira o id do usuário que deseja trocar informações: "))
        for user in self.users:
            if user._id == id_user:
                print(f"{user}")
            try:
                new_age = int(input("Insira a nova idade do usuário: "))
                user.change_age(new_age)
            except Exception as e:
                print(f'Erro ao trocar a idade do usuário: {e}')
            break

