import pytest
from selene.support.shared import browser
from selene import be, have


def test_browser_successful(open_browser):
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_browser_failed(open_browser):
    browser.element('[id="search"]').should(have.no.text('абракадабра'))