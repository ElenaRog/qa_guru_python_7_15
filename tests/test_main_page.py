import allure

from allure_commons.types import Severity
from pages.main_page import MainPage

main_page = MainPage()


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Elena Rogozina')
@allure.feature('Main page')
@allure.story('Change language')
@allure.link('https://nexign.com/ru')
def test_change_language():
    main_page.open()
    main_page.click_language_button()
    main_page.change_language_button()
    main_page.confirm_en_language()
    pass


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Elena Rogozina')
@allure.feature('Main page')
@allure.story('Go to page')
@allure.link('https://nexign.com/')
def test_go_to_page():
    main_page.open()
    main_page.go_to_contacts()
    main_page.confirm_contacts_page()


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Elena Rogozina')
@allure.feature('Main page')
@allure.story('Go to home page')
@allure.link('https://nexign.com/')
def test_go_to_home_page():
    main_page.open_other_page(url='about')
    main_page.go_to_home_page()
    main_page.confirm_home_page()


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Elena Rogozina')
@allure.feature('Main page')
@allure.story('Find article')
@allure.link('https://nexign.com/')
def test_find_articles():
    main_page.open()
    main_page.find_article('Тестирование')
    main_page.confirm_finding_articles()


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Elena Rogozina')
@allure.feature('Main page')
@allure.story('Store in menu')
@allure.link('https://nexign.com/')
def test_menu_content():
    main_page.open()
    main_page.confirm_menu_content_has_store()
