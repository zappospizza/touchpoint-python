import os
from touchpoint import Touchpoint

TEST_STORE_ID=os.environ['TP_STORE_ID']
TEST_API_KEY="notneeded"

def test_employee_info():
    """Tests an API call to get an employee's info"""
    t = Touchpoint(api_key=TEST_API_KEY)

    employee = t.Employee(employee_id=1396, first_name="Zappo", last_name="Z")
    resp = employee.info()

    assert isinstance(resp, dict)
    assert resp['employee_id'] == 1396, "The ID should be in the response"
    assert resp['first_name'] == "Zappo", "The first name should be in the response"
    assert resp['last_name'] == "Z", "The first name should be in the response"
