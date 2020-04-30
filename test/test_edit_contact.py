# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Анзор', lastname='Шарипов'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname='Салам')
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Анзор', lastname='Шарипов'))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(lastname='Новая'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_title(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Анзор', lastname='Шарипов'))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(title='Новая'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Анзор', lastname='Шарипов'))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(address='Новый'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Анзор', lastname='Шарипов'))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(email='Новая'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_mobile(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Анзор', lastname='Шарипов'))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(mobile='Новый'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
