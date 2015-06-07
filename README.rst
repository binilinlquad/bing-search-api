Thin wrapper for Microsoft Bing Search (Azure). This module use Basic Auth.

Usage
****
Sample simple request ::

    from bing_search_api import BingSearchAPI

    api = BingSearchAPI('YOU_API_KEY')
    result =  api.searchImage('sunshine') 
    print(result.json)

Sample set response as json ::
    from bing_search_api import BingSearchAPI
    
    api = BingSearchAPI('YOU_API_KEY')
    params = {'$format': 'json'}
    result = api.search_image('sunshine', payload=params)
 
Bing Search API
****
Bing Search API parameters could be read in `link <https://onedrive.live.com/view.aspx?resid=9C9479871FBFA822!109&app=Word&authkey=!ACvyZ_MNtngQyCU>`_
