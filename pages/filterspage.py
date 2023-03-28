from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FilterPage:
    SEARCHBAR = (By.XPATH, "/html/body/app-root/app-clients/header/form")
    LOYALTYFILTER = (
        By.XPATH,
        "/html/body/app-root/app-clients/header/aside/div[1]/app-client-loyality-level-filter/div/div[1]",
    )
    OPTION = (
        By.XPATH,
        "/html/body/app-root/app-clients/header/aside/div[1]/app-client-loyality-level-filter/div/div[2]/mat-checkbox[1]/label/div",
    )
    SEARCH_BTN = (
        By.XPATH,
        "/html/body/app-root/app-clients/header/aside/div[2]/button[1]",
    )

    def __init__(self, driver):
        self.driver = driver

    def check_filters(self):
        wait = WebDriverWait(self.driver, 20)
        searchbar = wait.until(EC.visibility_of_element_located(self.SEARCHBAR))
        searchbar.click()
        loyaltyfilter = wait.until(EC.visibility_of_element_located(self.LOYALTYFILTER))
        loyaltyfilter.click()
        option = wait.until(EC.visibility_of_element_located(self.OPTION))
        option.click()
        loyaltyfilter.click()
        search_btn = wait.until(EC.visibility_of_element_located(self.SEARCH_BTN))
        search_btn.click()
