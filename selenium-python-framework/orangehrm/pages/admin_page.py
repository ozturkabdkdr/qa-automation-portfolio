# admin_page.py
class AdminPage:
    def __init__(self, driver):
        self.driver = driver

    def get_user_role_dropdown_options(self):
        dropdown = self.driver.find_element("xpath", "//label[text()='User Role']/following::div[1]")
        dropdown.click()
        options = self.driver.find_elements("xpath", "//div[@role='listbox']//span")
        return [opt.text for opt in options]

    def search_user(self, username):
        self.driver.find_element("xpath", "//label[text()='Username']/following::input[1]").send_keys(username)
        self.driver.find_element("xpath", "//button[@type='submit']").click()

    def is_result_table_displayed(self):
        return self.driver.find_element("xpath", "//div[@class='oxd-table-body']").is_displayed()
