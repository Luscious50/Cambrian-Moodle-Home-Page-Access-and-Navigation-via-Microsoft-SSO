# ============================================================
# AT-003: test_moodle_api_token.py
# Purpose: Verify Moodle REST API responds with valid data
# Note: Replace YOUR_TOKEN_HERE with your Moodle security token
# To get token: Moodle > Profile > Preferences > Security Keys
# ============================================================
import requests

MOODLE_URL = "https://moodle.cambriancollege.ca"
API_TOKEN = "YOUR_TOKEN_HERE"  # Paste only the raw Moodle token value here, not the "Webservice-..." label

def test_moodle_api():
    endpoint = f"{MOODLE_URL}/webservice/rest/server.php"
    params = {
        "wstoken": API_TOKEN,
        "wsfunction": "core_webservice_get_site_info",
        "moodlewsrestformat": "json"
    }
    response = requests.get(endpoint, params=params)

    assert response.status_code == 200, \
        f"Expected 200 status, got {response.status_code}"

    data = response.json()
    assert "sitename" in data, \
        f"Expected 'sitename' in response, got: {data}"
    assert "errorcode" not in data, \
        f"API returned an error: {data}"

    print(f"AT-003 PASS: API responded with site name: {data['sitename']}")

if __name__ == "__main__":
    test_moodle_api()
    
