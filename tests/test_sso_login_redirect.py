# ============================================================
# AT-002: test_sso_login_redirect.py
# Purpose: Verify SSO button redirects to Microsoft login
# ============================================================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MOODLE_URL = "https://cambrian.mrooms.net"
MICROSOFT_LOGIN_DOMAIN = "login.microsoftonline.com"

def test_sso_redirect():
    driver = webdriver.Chrome()
    try:
        driver.get(MOODLE_URL)
        wait = WebDriverWait(driver, 10)

        # Find and click the Microsoft SSO login button
        sso_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'oauth2') or contains(text(),'Microsoft')]"))
        )
        sso_btn.click()

        # Wait for redirect and verify we are on Microsoft login
        wait.until(EC.url_contains(MICROSOFT_LOGIN_DOMAIN))
        assert MICROSOFT_LOGIN_DOMAIN in driver.current_url, \
            f"Expected Microsoft login page, got: {driver.current_url}"
        print("AT-002 PASS: SSO button redirected to Microsoft login page")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_sso_redirect()
    