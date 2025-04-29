from playwright.sync_api import sync_playwright

def test_example_website():
    with sync_playwright() as p:
        # Запуск браузера (по умолчанию Chromium)
        browser = p.chromium.launch(headless=False)  # headless=False для визуального отображения
        page = browser.new_page()

        #Открытие веб-страницы
        page.goto("https://example.com")

        #Проверка заголовка страницы
        assert "Example" in page.title(), "Заголовок страницы не содержит 'Example'"

        #Поиск и клик по элементу с текстом "More information"
        # Если элемент не найден, скрипт выдаст ошибку
        more_info_selector = "text='More information'"
        page.click(more_info_selector)

        #Проверка URL после клика
        expected_url = "https://www.iana.org/domains/example"
        assert page.url == expected_url, f"Ожидался URL {expected_url}, получен {page.url}"

        print("✅ Все проверки пройдены успешно!")
        browser.close()

if __name__ == "__main__":
    test_example_website()
