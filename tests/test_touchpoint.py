import os
from touchpoint import Touchpoint

API_KEY=os.environ['TP_API_KEY']
TEST_STORE_ID=os.environ['TP_STORE_ID']

def test_ping():
    """Tests an API call to API's endpoint"""
    t = Touchpoint(api_key=API_KEY)
    resp = t.ping()
    assert isinstance(resp, int)

def test_ping_full():
    """Tests an API call to API's endpoint"""
    t = Touchpoint(api_key=API_KEY)
    resp = t.ping_full()
    assert isinstance(resp, str)
    assert "status" in resp, "The response should include status."
    assert "error" in resp, "The response should incude error."
    assert "data" in resp, "The response should include data."

def test_get_employees():
    """Tests an API call to get a store's employees"""

    t = Touchpoint(api_key=API_KEY)
    resp = t.get_employees(store_id=TEST_STORE_ID)

    assert isinstance(resp, list)
    assert isinstance(resp[0], Touchpoint.Employee), "The type of employees should be Employee."

def test_get_employee():
    """Tests an API call to get a store's employees"""

    t = Touchpoint(api_key=API_KEY)
    resp = t.get_employee(store_id=TEST_STORE_ID, employee_id="zp001~342a1b43388b8d0238839e04596c49361")

    assert isinstance(resp, Touchpoint.Employee)

def test_get_location():
    """Tests an API call to get a location"""

    t = Touchpoint(api_key=API_KEY)
    resp = t.get_location(store_id=TEST_STORE_ID)

    assert isinstance(resp, Touchpoint.Location)