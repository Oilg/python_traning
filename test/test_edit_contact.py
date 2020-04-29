# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Анзор', lastname='Шарипов'))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname='Новое имя'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Анзор', lastname='Шарипов'))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(lastname='Новая фамилия'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_title(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Анзор', lastname='Шарипов'))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(title='Новая должность'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Анзор', lastname='Шарипов'))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(address='Новый адрес'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Анзор', lastname='Шарипов'))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(email='Новая почта'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_mobile(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Анзор', lastname='Шарипов'))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(mobile='Новый телефон'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
