# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname='Новое имя'))


def test_edit_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname='Новая фамилия'))


def test_edit_contact_title(app):
    app.contact.modify_first_contact(Contact(title='Новая должность'))


def test_edit_contact_address(app):
    app.contact.modify_first_contact(Contact(address='Новый адрес'))


def test_edit_contact_email(app):
    app.contact.modify_first_contact(Contact(email='Новая почта'))


def test_edit_contact_mobile(app):
    app.contact.modify_first_contact(Contact(mobile='Новый телефон'))
