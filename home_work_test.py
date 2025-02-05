from selene import browser, be, have

NOT_FOUND_TEXT = ',mxngvjklksdfckjnrekwjlrnvejkrnli'


class TestSearchEngineFindSelene:

    def test_duck_duck_go_should_find_selene(self):
        browser.open('/')
        browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
        browser.element('.react-results--main').should(
            have.text('Selene: User-Oriented Web UI Browser Tests in Python - GitHub Pages'))


def test_google_search_abra_cadabra_and_not_find_selene():
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type(NOT_FOUND_TEXT).press_enter()
    browser.element('section[data-testid="mainline"]').should(
        have.text(f'По запросу {NOT_FOUND_TEXT} результаты не найдены.'))
