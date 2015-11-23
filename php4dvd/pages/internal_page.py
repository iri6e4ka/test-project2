from php4dvd.pages.page import Page
from selenium.webdriver.common.by import By


class InternalPage(Page):

    @property
    def logout_button(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?logout']")

    @property
    def user_profile_link(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?go=profile']")

    @property
    def user_management_link(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?go=users']")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "nav"))

    @property
    def add_movie_link(self):
        return self.driver.find_element_by_link_text("Add movie").click()

    @property
    def add_movie_link(self):
        return self.driver.find_element_by_xpath("//*[@id='updateform']/table/tbody/tr[2]/td[2]/input").send_keys("my film")

    @property
    def search_field(self):
        return self.driver.find_element_by_id("q")

