import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture()
def open_browser():
    browser.open('https://www.google.com/').driver.set_window_size(800,600)
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()


