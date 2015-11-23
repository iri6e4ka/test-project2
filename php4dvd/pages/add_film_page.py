from internal_page import InternalPage
from selenium.webdriver.common.by import By


class AddFilmPage(InternalPage):

    @property
    def title_field(self):
        return self.driver.find_element_by_xpath("//*[@id='updateform']/table/tbody/tr[2]/td[2]/input").send_keys("my film")

    @property
    def year_field(self):
        return self.driver.find_element_by_xpath("//*[@id='updateform']/table/tbody/tr[4]/td[2]/input").send_keys("1989")
    @property
    def submit_button(self):
        return self.driver.find_element_by_xpath("//*[@id='submit']").click()