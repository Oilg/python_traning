# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_edit_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.edit(Contact(firstname='Анзор', lastname='Шарипов',
                             title='Лалка', address='В горах жи есть',
                             email='azaza@mail.ru', mobile='11'))
    app.session.logout()
