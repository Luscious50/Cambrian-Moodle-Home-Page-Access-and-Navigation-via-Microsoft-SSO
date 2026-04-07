const { test, expect } = require('@playwright/test');

test.describe('Cambrian Moodle homepage access and navigation', () => {
  test('Moodle login page is reachable', async ({ page }) => {
    await page.goto('https://moodle.cambriancollege.ca/', {
      waitUntil: 'domcontentloaded',
    });

    await expect(page).toHaveURL(/moodle/i);
  });

  test('login page shows Microsoft sign-in option or login-related controls', async ({ page }) => {
    await page.goto('https://moodle.cambriancollege.ca/', {
      waitUntil: 'domcontentloaded',
    });

    const pageText = await page.locator('body').innerText();

    await expect(pageText.toLowerCase()).toMatch(/microsoft|login|sign in|sso/);
  });

  test('homepage contains visible navigation-related content after landing', async ({ page }) => {
    await page.goto('https://moodle.cambriancollege.ca/', {
      waitUntil: 'domcontentloaded',
    });

    const body = await page.locator('body').innerText();

    expect(body.length).toBeGreaterThan(50);
  });
});
