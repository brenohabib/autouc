import time
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://192.168.0.1/")
    page.get_by_role("textbox", name="Senha").fill("dominet123")
    page.get_by_role("textbox", name="Senha").press("Enter")
    page.get_by_text("Avançado", exact=True).click()
    page.get_by_role("link", name="Ferramentas de Sistema").click()
    page.get_by_role("link", name="- Backup e Recuperação").click()
    file_input = page.locator('#filename')
    file_input.set_input_files("./preset.bin")
    page.locator("#t_restore").click()

    time.sleep(4)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
