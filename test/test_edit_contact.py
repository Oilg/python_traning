# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Анзор', lastname='Шарипов'))
    app.contact.modify_first_contact(Contact(firstname='Новое имя'))


def test_edit_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Анзор', lastname='Шарипов'))
    app.contact.modify_first_contact(Contact(lastname='Новая фамилия'))


def test_edit_contact_title(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Анзор', lastname='Шарипов'))
    app.contact.modify_first_contact(Contact(title='Новая должность'))


def test_edit_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Анзор', lastname='Шарипов'))
    app.contact.modify_first_contact(Contact(address='Новый адрес'))


def test_edit_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Анзор', lastname='Шарипов'))
    app.contact.modify_first_contact(Contact(email='Новая почта'))


def test_edit_contact_mobile(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Анзор', lastname='Шарипов'))
    app.contact.modify_first_contact(Contact(mobile='Новый телефон'))
