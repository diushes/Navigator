from selenium import webdriver
from tests.check_filters_test import test_check_filters
from tests.view_edit_client_test import test_view_client


driver = webdriver.Chrome()

# 1) This testcase performs login, adding new client, viewing and checking newly added client and editing client info
# uncomment to run

test_view_client(
    driver,
    "Salvatore",
    "Damon",
    "hotterbrothers@gmail.com",
    "22000611300",
    "2/16/1820",
    "Stefan",
)

# 2) This is a custom testcase, that checks "Loyalty level" filter
# test_check_filters(driver)
