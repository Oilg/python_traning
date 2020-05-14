from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
import random


db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')


def test_check_contact_in_group(app):
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    dblist = db.get_contacts_in_group(Group(id=group.id))
    groupname = app.group.get_group_name_by_id(group.id)
    uilist = app.contact.get_contacts_in_group(groupname)
    assert sorted(dblist, key=Contact.id_or_max) == sorted(uilist,  key=Contact.id_or_max)
