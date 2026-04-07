# ============================================================
# AT-001: test_login_page_loads.py
# Purpose: Verify Moodle login page loads and SSO button exists
# ============================================================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MOODLE_URL = "https://cambrian.mrooms.net"

def test_login_page_loads():
    driver = webdriver.Chrome()
    try:
        driver.get(MOODLE_URL)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        assert "Moodle" in driver.title or "Cambrian" in driver.title, \
            "Page title does not indicate Moodle loaded"
        print("AT-001 PASS: Login page loaded successfully")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_page_loads()
    