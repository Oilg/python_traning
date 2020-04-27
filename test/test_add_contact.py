# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname='Анзор', lastname='Шарипов',
                               title='Лалка', address='В горах жи есть',
                               email='azaza@mail.ru', mobile='11'))
