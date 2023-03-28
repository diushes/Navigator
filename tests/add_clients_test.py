from pages.addclientspage import ClientsPage
from tests.logintest import test_login

# this code adds new client
def test_add_client(driver, surname, name, email, number, birth):
    test_login(driver)
    client_page = ClientsPage(driver)

    # Click on "Add client" button
    client_page.go_to_add_client_page()

    # Fill client information
    client_page.fill_client_info(surname, name, email, number, birth)

    # Save client
    client_page.save_client()
