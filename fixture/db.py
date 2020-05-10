import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True  # отключаем кэширование БД, что бы в тестах не было различий
                                          # (старые списки и новые)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                'select id, firstname, lastname, title, address, home, mobile, work, email, phone2 from addressbook '
                'where deprecated="0000-00-00 00:00"')
            for row in cursor:
                (id, firstname, lastname, title, address, home, mobile, work, email, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, title=title, address=address,
                                    homephone=home, mobilephone=mobile, workphone=work, secondaryphone=phone2,
                                    email=email))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
