from pages.viewclientpage import ViewClientsPage
from tests.add_clients_test import test_add_client

# this code is for viewing and editing newly created client
def test_view_client(driver, surname, name, email, number, birth, newname):
    test_add_client(driver, surname, name, email, number, birth)
    viewclientpage = ViewClientsPage(driver)
    viewclientpage.choose_recently_added_client()
    viewclientpage.check_client_info(surname, name, email, number, birth)
    viewclientpage.change_client_name(newname)
