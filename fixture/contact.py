from model.contact import Contact
from model.group import Group
from fixture import group
import re
import time
from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_creation_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text('add new').click()

    def create(self, contact):
        wd = self.app.wd
        # self.return_to_home_page()
        self.open_contact_creation_page()
        self.fill_contact_form(contact)
        # submit group creation
        wd.find_element_by_name('submit').click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_field_value('firstname', contact.firstname)
        self.change_field_value('lastname', contact.lastname)
        self.change_field_value('title', contact.title)
        self.change_field_value('address', contact.address)
        self.change_field_value('email', contact.email)
        self.change_field_value('mobile', contact.mobilephone)
        self.change_field_value('home', contact.homephone)
        self.change_field_value('work', contact.workphone)
        self.change_field_value('phone2', contact.secondaryphone)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

    def editbutton(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_to_home_page()
        self.editbutton(index)
        # open modification form
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name('update').click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]').click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]').click()
        wd.switch_to.alert.accept()
        self.contact_cache = None
        self.waiting(0.1)

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def waiting(self, seconds):
        time.sleep(seconds)

    def return_to_home_page(self):
        wd = self.app.wd
        if not int(len(wd.find_elements_by_name('searchstring')) > 0):
            wd.find_element_by_link_text('home').click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name('selected[]'))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            for line in wd.find_elements_by_name('entry'):
                cells = line.find_elements_by_tag_name('td')
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name('input').get_attribute('value')
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        homephone = wd.find_element_by_name('home').get_attribute('value')
        workphone = wd.find_element_by_name('work').get_attribute('value')
        mobilephone = wd.find_element_by_name('mobile').get_attribute('value')
        secondaryphone = wd.find_element_by_name('phone2').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        # вытаскиваем из текста нужные элементы - номера телефонов с префиксами H, W, M, P
        homephone = re.search('H: (.*)', text)
        workphone = re.search('W: (.*)', text)
        mobilephone = re.search('M: (.*)', text)
        secondaryphone = re.search('P: (.*)', text)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def get_contacts_in_group(self, groupname):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            select = Select(wd.find_element_by_name('group'))
            select.select_by_visible_text(groupname)
            for line in wd.find_elements_by_name('entry'):
                cells = line.find_elements_by_tag_name('td')
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name('input').get_attribute('value')
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)
