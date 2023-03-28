from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ClientsPage:
    SURNAME_FIELD = (By.ID, "mat-input-1")
    NAME_FIELD = (By.ID, "mat-input-2")
    GENDER_FIELD = (By.ID, "mat-radio-2")
    EMAIL_FIELD = (By.ID, "mat-input-4")
    NUMBER_FIELD = (By.ID, "mat-input-5")
    BIRTH_FIELD = (By.ID, "mat-input-6")
    SAVE_BTN = (By.NAME, "save")

    def __init__(self, driver):
        self.driver = driver

    def go_to_add_client_page(self):
        wait = WebDriverWait(self.driver, 20)
        add_btn = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='sB']/button"))
        )
        add_btn.click()

    def fill_client_info(self, surname, name, email, number, birth):
        surname_field = self.driver.find_element(*self.SURNAME_FIELD)
        surname_field.send_keys(surname)

        name_field = self.driver.find_element(*self.NAME_FIELD)
        name_field.send_keys(name)

        gender_field = self.driver.find_element(*self.GENDER_FIELD)
        gender_field.click()

        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.send_keys(email)

        number_field = self.driver.find_element(*self.NUMBER_FIELD)
        number_field.send_keys(number)

        birth_field = self.driver.find_element(*self.BIRTH_FIELD)
        birth_field.send_keys(birth)

    def save_client(self):
        self.driver.find_element(*self.SAVE_BTN).click()
        wait = WebDriverWait(self.driver, 20)
        alert = wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert  # switch to the alert dialog
        alert.accept()
