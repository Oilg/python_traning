# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from model.contact import Contact
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username='admin', password='secret')
    app.group.create(Group(name='dfgdfg', header='dfgdfg', footer='dfgdfgdfgdfg'))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username='admin', password='secret')
    app.group.create(Group(name='', header='', footer=''))
    app.session.logout()


def test_add_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.create(Contact(firstname='Анзор', lastname='Шарипов', title='Лалка', address='В горах жи есть'))
    app.session.logout()


def test_edit_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.edit(Contact(firstname='Анзор', lastname='Шарипов',
                             title='Лалка', address='В горах жи есть',
                             email='azaza@mail.ru', mobile='11'))
    app.session.logout()
