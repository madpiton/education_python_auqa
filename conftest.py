from selene import browser
import pytest

# Фикстура для настройки и завершения работы браузера
@pytest.fixture(scope="function")
def setup_browser():
    # Настройка браузера (например, Chrome)
    browser.config.driver_name = 'chrome'
    browser.config.window_width = 1024
    browser.config.window_height = 786
    browser.config.timeout = 20  # Установка таймаута для ожиданий

    yield browser  # Возвращаем объект браузера для использования в тестах

    # Завершение работы браузера после выполнения теста
    browser.quit()
    print("Закрываем браузер")