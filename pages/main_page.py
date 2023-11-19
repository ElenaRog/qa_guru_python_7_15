import allure

from selene import browser, have, be


class MainPage:
    @allure.step('Open main page')
    def open(self):
        browser.open('')

    @allure.step('Click language button')
    def click_language_button(self):
        language_button = browser.element('.language_top')
        language_button.click()

    @allure.step('Change language button')
    def change_language_button(self):
        browser.all('.language__select').first.click()

    @allure.step('Confirm English language')
    def confirm_en_language(self):
        browser.all('.language__curent').first.should(have.text('ENG'))

    @allure.step('Go to Contact page')
    def go_to_contacts(self):
        browser.element('[href="/ru/contact-us"]').click()

    @allure.step('Confirm Contact page')
    def confirm_contacts_page(self):
        browser.element('.page-title').should(have.text('Контакты'))

    @allure.step('Open other page')
    def open_other_page(self, url=''):
        browser.open(f'{url}')

    @allure.step('Open other page')
    def go_to_home_page(self):
        browser.element('.header__logo').click()

    @allure.step('Confirm Home page')
    def confirm_home_page(self):
        browser.element('.welcome-banner__content-title').should(have.text('Расширяем'))

    @allure.step('Trying to find articles')
    def find_article(self, article_theme):
        browser.element('.header__search').click()
        browser.element('#edit-search-api-fulltext').send_keys(article_theme).press_enter()

    @allure.step('Confirm finding articles')
    def confirm_finding_articles(self):
        assert len(browser.all('.line-group-search')) > 0

    @allure.step('Confirm menu content has Store')
    def confirm_menu_content_has_store(self):
        browser.element('.menu-item.store :first-child').should(have.text('Store'))
