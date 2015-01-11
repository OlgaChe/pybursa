from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver 


class MySeleniumTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(MySeleniumTests, cls).setUpClass()
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()
   def test_login(self):
       self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
       username_input = self.selenium.find_element_by_name("username")
       username_input.send_keys('admin')
       password_input = self.selenium.find_element_by_name("password")
       password_input.send_keys('admin')
       self.selenium.find_element_by_xpath("//input[@type='submit']").click()


























