import time
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://192.168.0.1/")
    page.wait_for_load_state("load")
    page.get_by_text("Nova Senha").click()
    page.get_by_role("textbox", name="Nova Senha").fill("dominet123")
    page.get_by_text("Confirmar Senha").click()
    page.get_by_role("textbox", name="Confirmar Senha").fill("dominet123")
    page.get_by_role("button", name="Salvar").click()
    time.sleep(1)
    page.get_by_role("textbox", name="Senha").click()
    page.get_by_role("textbox", name="Senha").fill("dominet123")
    page.get_by_role("textbox", name="Senha").press("Enter")
    page.get_by_role("button", name="Próximo").click()
    page.get_by_text("Avançado").click()
    page.get_by_role("link", name="Ferramentas de Sistema").click()
    page.get_by_role("link", name="- Atualização de Firmware").click()
    page.locator('a', has_text="EX141").click()
    file_input = page.locator('#filename')
    file_input.set_input_files("./firmware.bin")
    page.get_by_role("button", name="Atualização").click()
    time.sleep(4)
    context.close()
    browser.close()


def run_standalone() -> None:
    with sync_playwright() as playwright:
        run(playwright)


if __name__ == "__main__":
    run_standalone()
