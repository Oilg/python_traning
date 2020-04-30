from model.contact import Contact


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
        self.change_field_value('mobile', contact.mobile)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def editbutton(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="maintable"]/tbody/tr[2]/td[8]').click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_index(index)
        # open modification form
        # self.editbutton()
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
                text = line.text.split()
                id = line.find_element_by_name('selected[]').get_attribute('id')
                name = text[1]
                self.contact_cache.append(Contact(firstname=name, id=id))
        return list(self.contact_cache)
