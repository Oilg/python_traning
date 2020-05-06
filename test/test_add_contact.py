# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string_letters(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_digits(maxlen):
    symbols = string.digits
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname=random_string_letters('firstname', 10), lastname=random_string_letters('lastname', 10),
            title=random_string_letters('title', 10), address=random_string_letters('address', 10),
            email=random_string_letters('email', 10), mobilephone=random_string_digits(10),
            homephone=random_string_digits(10), workphone=random_string_digits(10),
            secondaryphone=random_string_digits(10))
            for i in range(3)]


@pytest.mark.parametrize('contact', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
