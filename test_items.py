from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_button_is_present_on_the_page(browser):
    browser.get(link)
    add_button = browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert len(add_button) > 0, 'Элемент не найден на странице!'
