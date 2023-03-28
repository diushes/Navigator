from pages.loginpage import LoginPage

# this code performs login
def test_login(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.enter_username("Admin")
    login_page.enter_password("Admin@Navi")
    login_page.click_login()

    assert "Navigator" in driver.title
