# ============================================================
# AT-002: test_sso_login_redirect.py
# Purpose: Verify SSO button redirects to Microsoft login
# ============================================================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MOODLE_URL = "https://moodle.cambriancollege.ca"

def test_sso_redirect():
    driver = webdriver.Chrome()
    try:
        driver.get(MOODLE_URL)
        wait = WebDriverWait(driver, 10)

        sso_link = wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                "//a[contains(@href, '/auth/saml2/login.php') and contains(@href, 'idp=')]"
            ))
        )

        href = sso_link.get_attribute("href")
        assert href is not None, "Microsoft SSO anchor href not found"
        assert "/auth/saml2/login.php" in href, f"Expected SAML2 login path, got: {href}"
        assert "idp=" in href, f"Expected idp parameter, got: {href}"

        print("AT-002 PASS: Microsoft SSO link points to Moodle SAML2 login flow")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_sso_redirect()
    
    
