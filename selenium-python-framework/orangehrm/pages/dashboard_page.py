# dashboard_page.py
class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_admin_tab(self):
        self.driver.find_element("xpath", "//span[text()='Admin']").click()
