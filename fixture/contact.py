class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text('Добавить контакт').click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # fill contact form
        wd.find_element_by_name('firstname').click()
        wd.find_element_by_name('firstname').clear()
        wd.find_element_by_name('firstname').send_keys(contact.firstname)
        wd.find_element_by_name('lastname').click()
        wd.find_element_by_name('lastname').clear()
        wd.find_element_by_name('lastname').send_keys(contact.lastname)
        wd.find_element_by_name('title').click()
        wd.find_element_by_name('title').clear()
        wd.find_element_by_name('title').send_keys(contact.title)
        wd.find_element_by_name('address').click()
        wd.find_element_by_name('address').clear()
        wd.find_element_by_name('address').send_keys(contact.address)
        wd.find_element_by_name('mobile').click()
        wd.find_element_by_name('mobile').clear()
        wd.find_element_by_name('mobile').send_keys(contact.mobile)
        wd.find_element_by_name('email').click()
        wd.find_element_by_name('email').clear()
        wd.find_element_by_name('email').send_keys(contact.email)
        # submit contact creation
        wd.find_element_by_name('submit').click()
        self.return_to_home()

    def mark(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="1"]').click()

    def editbutton(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="maintable"]/tbody/tr[2]/td[8]').click()

    def edit(self, contact):
        wd = self.app.wd
        self.mark()
        self.editbutton()
        # fill contact form
        wd.find_element_by_name('firstname').click()
        wd.find_element_by_name('firstname').clear()
        wd.find_element_by_name('firstname').send_keys(contact.firstname)
        wd.find_element_by_name('lastname').click()
        wd.find_element_by_name('lastname').clear()
        wd.find_element_by_name('lastname').send_keys(contact.lastname)
        wd.find_element_by_name('title').click()
        wd.find_element_by_name('title').clear()
        wd.find_element_by_name('title').send_keys(contact.title)
        wd.find_element_by_name('address').click()
        wd.find_element_by_name('address').clear()
        wd.find_element_by_name('address').send_keys(contact.address)
        wd.find_element_by_name('mobile').click()
        wd.find_element_by_name('mobile').clear()
        wd.find_element_by_name('mobile').send_keys(contact.mobile)
        wd.find_element_by_name('email').click()
        wd.find_element_by_name('email').clear()
        wd.find_element_by_name('email').send_keys(contact.email)
        # submit contact creation
        wd.find_element_by_name('update').click()
        self.return_to_home()

    def delete_first_contact(self):
        wd = self.app.wd
        self.mark()
        # submit deletion
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]').click()
        wd.switch_to_alert().accept()

    def return_to_home(self):
        wd = self.app.wd
        wd.find_element_by_link_text('home page').click()
