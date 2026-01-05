from playwright.sync_api import Page

def test_first(page:Page):
    print("hello")
    page.wait_for_timeout(5000)


def test_seconf(page:Page):
    print("hello2")
    page.wait_for_timeout(5000)