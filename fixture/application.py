from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome('C:\\Users\\LOG\\chromedriver.exe')
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get('http://localhost/addressbook/')


    def destroy(self):
        self.wd.quit()
