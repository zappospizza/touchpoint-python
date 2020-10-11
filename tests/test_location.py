from touchpoint import Touchpoint

TEST_API_KEY="notneeded"

def test_location_info():
    """Tests an API call to get an location's info"""
    t = Touchpoint(api_key=TEST_API_KEY)

    location = t.Location(location_id='test-1001', wss_url='', default_order_notes=None, name=None, address=None, phone=None)
    resp = location.info()

    assert isinstance(resp, dict)
    assert resp['location_id'] is 'test-1001', "The ID should be in the response"
