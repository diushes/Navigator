from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ViewClientsPage:
    SURNAME_FIELD = (
        By.XPATH,
        "/html/body/app-root/app-clients/section/app-client-details/div[2]/div/app-client-contacts/form[1]/div[1]/mat-form-field/div/div[1]/div/input",
    )
    NAME_FIELD = (
        By.XPATH,
        "/html/body/app-root/app-clients/section/app-client-details/div[2]/div/app-client-contacts/form[1]/div[2]/mat-form-field[1]/div/div[1]/div/input",
    )
    EMAIL_FIELD = (
        By.XPATH,
        "/html/body/app-root/app-clients/section/app-client-details/div[2]/div/app-client-contacts/form[2]/div[2]/input[2]",
    )
    NUMBER_FIELD = (
        By.XPATH,
        "/html/body/app-root/app-clients/section/app-client-details/div[2]/div/app-client-contacts/form[2]/div[2]/input[1]",
    )
    BIRTH_FIELD = (
        By.XPATH,
        "/html/body/app-root/app-clients/section/app-client-details/div[2]/div/app-client-contacts/form[1]/div[3]/mat-form-field/div/div[1]/div[1]/input",
    )
    SAVE_BTN = (
        By.XPATH,
        "/html/body/app-root/app-clients/section/app-client-details/div[2]/div/app-client-contacts/form[2]/div[6]/button",
    )

    def __init__(self, driver):
        self.driver = driver

    def choose_recently_added_client(self):
        self.driver.refresh()
        wait = WebDriverWait(self.driver, 20)
        time.sleep(5)
        last_added = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "/html/body/app-root/app-clients/div/div/div[1]/table/tbody/tr[1]",
                )
            )
        )
        last_added.click()

    def check_client_info(self, surname, name, email, number, birth):
        wait = WebDriverWait(self.driver, 20)
        surname_field_value = str(
            wait.until(
                EC.visibility_of_element_located(self.SURNAME_FIELD)
            ).get_attribute("value")
        )
        name_field_value = str(
            wait.until(EC.visibility_of_element_located(self.NAME_FIELD)).get_attribute(
                "value"
            )
        )
        email_field_value = str(
            wait.until(
                EC.visibility_of_element_located(self.EMAIL_FIELD)
            ).get_attribute("value")
        )
        number_field_value = str(
            wait.until(
                EC.visibility_of_element_located(self.NUMBER_FIELD)
            ).get_attribute("value")
        )
        birth_field_value = str(
            wait.until(
                EC.visibility_of_element_located(self.BIRTH_FIELD)
            ).get_attribute("value")
        )

        if (
            surname_field_value == surname
            and name_field_value == name
            and email_field_value == email
            and number_field_value == "996" + number
            and birth_field_value == birth
        ):
            print("All client information is correct")
        else:
            print("Client information is incorrect")

    def change_client_name(self, newname):
        wait = WebDriverWait(self.driver, 20)
        name_field = wait.until(EC.visibility_of_element_located(self.NAME_FIELD))
        save_btn = wait.until(EC.visibility_of_element_located(self.SAVE_BTN))
        name_field.clear()
        name_field.send_keys(newname)
        save_btn.click()
