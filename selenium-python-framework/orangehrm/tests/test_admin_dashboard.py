# test_admin_dashboard.py
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage

def test_admin_dashboard(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    LoginPage(driver).login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    dashboard.go_to_admin_tab()

    admin_page = AdminPage(driver)
    assert "Admin" in driver.title

    roles = admin_page.get_user_role_dropdown_options()
    assert "Admin" in roles
    assert "ESS" in roles

    admin_page.search_user("Admin")
    assert admin_page.is_result_table_displayed()
