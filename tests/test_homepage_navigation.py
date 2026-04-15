# ============================================================
# AT-004: test_homepage_navigation.py
# Purpose: Verify homepage navigation menu is present after login
# Note: This test requires valid credentials - use environment
# variables in production, not hardcoded values
# ============================================================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MOODLE_URL = "https://moodle.cambriancollege.ca"

def test_homepage_navigation():
    """
    Semi-automated test:
    Opens Moodle, waits for manual Microsoft SSO login,
    then verifies homepage navigation elements are visible.
    """
    with webdriver.Chrome() as driver:
        wait = WebDriverWait(driver, 20)

        driver.get(MOODLE_URL)

        input("Complete Microsoft SSO login in the browser, then press Enter here...")

        # Wait for a homepage-specific element, not just any <nav>
        dashboard_link = wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Dashboard"))
        )
        assert dashboard_link.is_displayed(), "Dashboard link is not visible"

        # Optional extra check
        my_courses_link = wait.until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "My"))
        )
        assert my_courses_link.is_displayed(), "Expected homepage navigation link not visible"

        print("AT-004 PASS: Homepage navigation is visible after login")

if __name__ == "__main__":
    test_homepage_navigation()
    
