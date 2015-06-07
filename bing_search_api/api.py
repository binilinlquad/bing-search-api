import requests
from requests.auth import HTTPBasicAuth

def quote(query):
    '''Quote query with sign(')'''
    if query.startswith('\'') is not True:
        query = '\'' + query 

    if query.endswith('\'') is not True:
        query = query + '\''         
    
    return query


class BingSearchAPI:
    ''' 
    Microsoft Bing Search (Azure) Wrapper 
    '''
    def __init__(self, key):
        self.key = key
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
        self.auth = HTTPBasicAuth(self.key, self.key) 
        self.url = 'https://api.datamarket.azure.com/Bing/Search/'
    
    def search(self, query, search_type, payload=None):
        '''Search implementation'''
        url = self.url + search_type
        headers = {'User-Agent': self.user_agent}
        
        if payload is not None:
           payload['Query'] = quote(query)
        else:
            payload = {'Query': quote(query)}

        request = requests.get(url, auth=self.auth, params=payload, headers=headers)
        return request

    def search_image(self, query, payload=None):
        '''Shortcut search image'''
        return self.search(query, 'Image', payload)

    def search_web(self, query, payload=None):
        '''Shortcut search web'''
        return self.search(query, 'Web', payload)

    def search_news(self, query, payload=None):
        '''Shortcut search News'''
        return self.search(query, 'News', payload)

    def search_video(self, query, payload=None):
        '''Shortcut search video'''
        return self.search(query, 'Video', payload)

    def search_spelling_suggestions(self, query, payload=None):
        '''Shortcut search spelling suggestions'''
        return self.search(query, 'SpellingSuggestions', payload)

    def search_related_search(self, query, payload=None):
        '''Shortcut search related'''
        return self.search(query, 'RelatedSearch', payload)

    def search_composite(self, query, source, payload=None):
        '''Shortcut search with composite source'''
        source = '+'.join(source)

        if payload is None:
            payload = dict(Sources=quote(source))
        else:
            payload['Sources'] = quote(source)
            
        return self.search(query, 'Composite', payload)

