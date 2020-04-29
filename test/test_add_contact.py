# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname='Анзор', lastname='Шарипов',
                               title='Лалка', address='В горах жи есть',
                               email='azaza@mail.ru', mobile='11'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
