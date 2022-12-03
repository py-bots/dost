from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://portal.iitdh.ac.in/asc/index.jsp")
    page.frame_locator("#right2").locator("input[name=\"UserName\"]").click()
    page.frame_locator("#right2").locator("input[name=\"UserName\"]").fill("200030017")
    page.frame_locator("#right2").locator("input[name=\"UserPassword\"]").click()
    page.frame_locator("#right2").locator("input[name=\"UserPassword\"]").fill("aps")
    page.frame_locator("#right2").locator("input[name=\"UserPassword\"]").press("CapsLock")
    page.frame_locator("#right2").locator("input[name=\"UserPassword\"]").fill("apsVW")
    page.frame_locator("#right2").locator("input[name=\"UserPassword\"]").press("CapsLock")
    page.frame_locator("#right2").locator("input[name=\"UserPassword\"]").fill("apsVWxjm")
    page.frame_locator("#right2").locator("input[name=\"UserPassword\"]").press("CapsLock")
    page.frame_locator("#right2").locator("input[name=\"UserPassword\"]").fill("apsVWxjmN")
    page.frame_locator("#right2").locator("input[name=\"UserPassword\"]").press("CapsLock")
    page.frame_locator("#right2").locator("input[name=\"UserPassword\"]").fill("apsVWxjmNz")
    page.frame_locator("#right2").get_by_role("button", name="Submit").click()
    time.sleep(2)
    page.frame_locator("#leftname").locator("#ygtvt1").click()
    page.frame_locator("#leftname").locator("#ygtvt8").click()
    page.frame_locator("#leftname").get_by_role("link", name="View").click()

    # ---------------------
    time.sleep(15)
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     run(playwright)


def start_codegen(website_url:str="pybots.ai"):
    import os

    os.system("playwright codegen "+website_url)

def activate_browser():
    with sync_playwright() as playwright:    
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
start_codegen()