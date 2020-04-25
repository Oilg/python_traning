# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact_firstname(app):
    app.session.login(username='admin', password='secret')
    app.contact.modify_first_contact(Contact(firstname='Новое имя'))
    app.session.logout()


def test_edit_contact_lastname(app):
    app.session.login(username='admin', password='secret')
    app.contact.modify_first_contact(Contact(lastname='Новая фамилия'))
    app.session.logout()


def test_edit_contact_title(app):
    app.session.login(username='admin', password='secret')
    app.contact.modify_first_contact(Contact(title='Новая должность'))
    app.session.logout()


def test_edit_contact_address(app):
    app.session.login(username='admin', password='secret')
    app.contact.modify_first_contact(Contact(address='Новый адрес'))
    app.session.logout()


def test_edit_contact_email(app):
    app.session.login(username='admin', password='secret')
    app.contact.modify_first_contact(Contact(email='Новая почта'))
    app.session.logout()


def test_edit_contact_mobile(app):
    app.session.login(username='admin', password='secret')
    app.contact.modify_first_contact(Contact(mobile='Новый телефон'))
    app.session.logout()
