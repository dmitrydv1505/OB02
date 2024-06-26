class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, 'admin')
        self.__users_list = []

    def add_user(self, user):
        self.__users_list.append(user)

    def remove_user(self, user):
        self.__users_list.remove(user)

    def get_users_list(self):
        return self.__users_list


# Пример использования системы
user1 = User(1, 'Alice')
user2 = User(2, 'Ivan')
user3 = User(3, 'Dmitry')

admin = Admin(101, 'AdminA')

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

admin.remove_user(user2)

users_list = admin.get_users_list()
for user in users_list:
    print(user.get_name(), user.get_access_level())
