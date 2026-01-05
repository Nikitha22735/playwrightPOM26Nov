import pytest
from playwright.sync_api import sync_playwright
from pathlib import Path
import pytest
# from playwright.sync_api import sync_playwright
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from pages.resultsPage import ResultsPage
from pages.shoppingCartPage import ShoppingCart
from pages.checkOutPage import CheckOutPage

AUTH_FILE = Path("testData/auth_state.json")

# @pytest.fixture(scope="session", autouse=True)
# def create_auth_state():
#     if AUTH_FILE.exists():
#         return

#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()

#         # home_Page.launchTheAmazonBrowser()
#         page.goto("https://www.amazon.in/")
#         page.wait_for_timeout(4000)
#         # home_Page.hoverOnAccountsBtn()
#         page.locator("#nav-link-accountList").hover()
#         # home_Page.clickOnSignInBtn()
#         page.locator(".nav-action-inner").click()
#         page.locator("#ap_email_login").fill("trainingplaywright@gmail.com")
#         # login_page.enterEmailID("trainingplaywright@gmail.com")
#         # login_page.clickOnContinueBtn()
#         page.locator("input[type='submit']").click()
#         # login_page.enterPassword("Welcome@02")
#         page.locator("#ap_password").fill("Welcome@02")
#         # login_page.clickOnContinueBtn()
#         page.locator("input[type='submit']").click()
        

#         # 💾 Save session
#         context.storage_state(path=AUTH_FILE)
#         yield
#         context.close()
#         browser.close()

# @pytest.fixture(scope="session", autouse=True)
# def create_auth_state():
#     # If file exists AND is valid (non-empty), reuse it
#     if AUTH_FILE.exists() and AUTH_FILE.stat().st_size > 0:
#         yield
#         return

#     AUTH_FILE.parent.mkdir(parents=True, exist_ok=True)

#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()

#         page.goto("https://www.amazon.in/")
#         # page.wait_for_load_state("networkidle")
#         page.wait_for_timeout(4000)
#         page.locator("#nav-link-accountList").hover()
#         page.locator(".nav-action-inner").click()

#         page.locator("#ap_email_login").fill("trainingplaywright@gmail.com")
#         page.locator("input[type='submit']").click()

#         page.locator("#ap_password").fill("Welcome@02")
#         page.locator("input[type='submit']").click()

#         # ✅ WAIT until login is actually successful
#         page.wait_for_selector("#nav-link-accountList-nav-line-1")

#         # ✅ Save only AFTER successful login
#         context.storage_state(path=AUTH_FILE)

#         yield

#         context.close()
#         browser.close()

@pytest.fixture(scope="session", autouse=True)
def create_auth_state(browser):
    # if AUTH_FILE.exists() and AUTH_FILE.stat().st_size > 0:
    #     yield
    #     return

    AUTH_FILE.parent.mkdir(parents=True, exist_ok=True)

    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.amazon.in/")
    page.wait_for_selector("#nav-link-accountList")

    page.locator("#nav-link-accountList").hover()
    page.locator(".nav-action-inner").click()

    page.locator("#ap_email_login").fill("trainingplaywright@gmail.com")
    page.locator("input[type='submit']").click()

    page.locator("#ap_password").fill("Welcome@02")
    page.locator("input[type='submit']").click()

    page.wait_for_selector("#nav-link-accountList-nav-line-1")

    context.storage_state(path=AUTH_FILE)

    yield

    context.close()

# @pytest.fixture(scope="session", autouse=True)
# def create_auth_state(browser_type):

    # 🔥 Force fresh login every run
    # if AUTH_FILE.exists():
    #     AUTH_FILE.unlink()

    # browser = browser_type.launch(headless=True)
    # context = browser.new_context()
    # page = context.new_page()

    # page.goto("https://www.amazon.in/")
    # page.wait_for_selector("#nav-link-accountList")

    # page.locator("#nav-link-accountList").hover()
    # page.locator(".nav-action-inner").click()

    # page.locator("#ap_email_login").fill("trainingplaywright@gmail.com")
    # page.locator("input[type='submit']").click()

    # page.locator("#ap_password").fill("Welcome@02")
    # page.locator("input[type='submit']").click()

    # page.wait_for_selector("#nav-link-accountList-nav-line-1")

    # # ✅ Always overwrite
    # context.storage_state(path=AUTH_FILE)

    # context.close()
    # browser.close()

    # yield


# @pytest.fixture
# def context(browser):
#     # context = browser.new_context(storage_state="auth_state.json")
#     # browser = browser.chromium.launch(headless=False)
#     context = browser.new_context(storage_state=AUTH_FILE)
#     yield context
#     context.close()

# @pytest.fixture
# def page(context):
#     page = context.new_page()
#     yield page

# @pytest.fixture(scope="session")
# def context(browser):
#     context = browser.new_context(storage_state=AUTH_FILE)
#     yield context
#     context.close()

# @pytest.fixture
# def page(context):
#     page = context.new_page()
#     yield page
    # page.close()

@pytest.fixture
def context(browser):
    context = browser.new_context(storage_state=AUTH_FILE)
    yield context
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="function")
def home_Page(page):
    home_Page = HomePage(page)
    return home_Page

@pytest.fixture()
def login_page(page):
    login_page = LoginPage(page)
    return login_page

@pytest.fixture()
def results_page(page):
    results_page = ResultsPage(page)
    return results_page

@pytest.fixture()
def shoppingCart_page(page):
    shoppingCart_page = ShoppingCart(page)
    return shoppingCart_page

@pytest.fixture()
def CheckOut_page(page):
    CheckOut_page = CheckOutPage(page)
    return CheckOut_page
