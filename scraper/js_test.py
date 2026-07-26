from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://quotes.toscrape.com/js/")

    page.wait_for_timeout(3000)

    print(page.locator(".quote").first.inner_text())

    browser.close()