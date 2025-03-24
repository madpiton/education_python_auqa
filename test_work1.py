from selene import browser, be, have

# Тест для поиска на ya.ru
def test_ya_search(setup_browser):
    # Открыть страницу Яндекса
    browser.open('https://ya.ru')

    # Найти поле поиска и ввести текст
    browser.element('#text').should(be.blank).type('eefofoasfoeeoeoeoeoeofjajggg').press_enter()

    # Проверить наличие текста на странице
    browser.element('html').should(have.text("Ничего не нашли"))  # Или другой текст, который ожидается в результатах
