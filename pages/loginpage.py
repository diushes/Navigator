class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get("http://167.114.201.175:5000/login")

    def enter_username(self, username):
        username_field = self.driver.find_element_by_name("userName")
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element_by_class_name("auth-btn")
        login_button.click()
