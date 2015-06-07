import unittest
import os
from api import BingSearchAPI

class TestBingSearchAPI(unittest.TestCase):
    api = BingSearchAPI(os.getenv('BING_API_ID', 'YOUR_ID_HERE'))

    def test_search_image(self):
        result = self.api.search_image('sunshine')
        assert result
        assert result.status_code==200

    def test_search_image_json_format(self):
        params = {'$format': 'json'}
        result = self.api.search_image('sunshine', payload=params)
        assert result
        assert result.status_code==200
        assert result.json is not None

    def test_search_image_complex_params(self):
        result = self.api.search_image('sunshine', payload={'$format': 'json', '$top': 5, 'Adult': '\'Strict\'', 'ImageFilters': '\'Size:Large+Aspect:Wide\''})
        self.assertEqual(result.status_code, 200)

    def test_search_web(self):
        result = self.api.search_web('sunshine')
        assert result
        assert result.status_code==200

    def test_search_web_json_format(self):
        params = {'$format': 'json'}
        result = self.api.search_web('sunshine', payload=params)
        assert result
        assert result.status_code==200
        assert result.json is not None

    def test_search_news(self):
        result = self.api.search_news('sunshine')
        assert result
        assert result.status_code==200

    def test_search_news_json_format(self):
        params = {'$format': 'json'}
        result = self.api.search_news('sunshine', payload=params)
        assert result
        assert result.status_code==200
        assert result.json is not None

    def test_search_video(self):
        result = self.api.search_video('sunshine')
        assert result
        assert result.status_code==200

    def test_search_video_json_format(self):
        params = {'$format': 'json'}
        result = self.api.search_video('sunshine', payload=params)
        assert result
        assert result.status_code==200
        assert result.json is not None

    def test_search_spelling_suggestions(self):
        result = self.api.search_spelling_suggestions('sunshine')
        assert result
        assert result.status_code==200

    def test_search_spelling_suggestions_json_format(self):
        params = {'$format': 'json'}
        result = self.api.search_spelling_suggestions('sunshine', payload=params)
        assert result
        assert result.status_code==200
        assert result.json is not None

    def test_search_related_search(self):
        result = self.api.search_related_search('sunshine')
        assert result
        assert result.status_code==200

    def test_search_related_search_json_format(self):
        params = {'$format': 'json'}
        result = self.api.search_related_search('sunshine', payload=params)
        assert result
        assert result.status_code==200
        assert result.json is not None

    def test_search_composite(self):
        src = ['Web', 'News'] # any search type
        result = self.api.search_composite('sunshine', src)
        assert result
        assert result.status_code==200

    def test_search_composite_json_format(self):
        params = {'$format': 'json'}
        src = ['Web', 'News'] # any search type
        result = self.api.search_composite('sunshine', src, payload=params)
        assert result
        assert result.status_code==200
        assert result.json is not None


if __name__=='__main__':
    unittest.main()
