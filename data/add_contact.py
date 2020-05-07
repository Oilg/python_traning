from model.contact import Contact
import random
import string


constant = [
    Contact(firstname='firstname1', lastname='lastname1', title='title1', address='address1',
            email='email1', mobilephone='12345', homephone='12345', workphone='12345', secondaryphone='12345'),
    Contact(firstname='firstname1', lastname='lastname1', title='title1', address='address1',
            email='email1', mobilephone='12345', homephone='12345', workphone='12345', secondaryphone='12345')]


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
