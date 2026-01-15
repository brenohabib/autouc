import time
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://192.168.101.1/#/login")
    page.locator("input[type=\"text\"]").fill("adminisp")
    page.locator("input[type=\"text\"]").press("Tab")
    page.locator("input[name=\"user\"]").fill("adminisp")
    page.get_by_role("button", name=" Login").click()
    page.get_by_text("Management", exact=True).click()
    page.get_by_role("menuitem", name="Firmware Update").click()
    page.locator('.el-upload__input').set_input_files("./V3.2.8_sinal.img")
    page.get_by_role("button", name=" Upgrade").click()
    page.get_by_role("button", name="Confirm").click()
    time.sleep(50)
    # page.get_by_text("3%Uploading fileTo avoid").click() --> usar para talvez checkar chegar em 100%

    # ---------------------
    context.close()
    browser.close()

def run_standalone() -> None:
    with sync_playwright() as playwright:
        run(playwright)


if __name__ == "__main__":
    run_standalone()
