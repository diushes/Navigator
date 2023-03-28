import time
from pages.filterspage import FilterPage
from tests.logintest import test_login

# this code checks filter
def test_check_filters(driver):
    test_login(driver)
    filterpage = FilterPage(driver)
    filterpage.check_filters()
