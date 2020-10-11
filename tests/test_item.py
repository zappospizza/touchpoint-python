from touchpoint import Touchpoint

TEST_API_KEY="notneeded"

def test_item_info():
    """Tests an API call to get an location's info"""
    t = Touchpoint(api_key=TEST_API_KEY)

    item = t.Item(item_id='test~1001')
    resp = item.info()

    assert isinstance(resp, dict)
    assert resp['item_id'] is 'test~1001', "The ID should be in the response"
