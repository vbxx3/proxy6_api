import requests
from proxy6_api.exceptions import *


class Proxy6:
    def __init__(self, api_key):
        self._api_key = api_key
        self._check_auth()

    def _send(self, method, params=None):
        response = requests.get(f'https://proxy6.net/api/{self._api_key}/{method}/?{params}').json()
        if response['status'] == 'no':
            raise MethodError(response.get('error', None))
        else:
            return response

    def _check_auth(self):
        if requests.get(f'https://proxy6.net/api/{self._api_key}').json()['status'] == 'no':
            raise WrongKey('Wrong api key')

    def balance(self):
        return requests.get(f'https://proxy6.net/api/{self._api_key}').json()['balance']

    def get_price(self, count, period, version=None):
        return self._send('getprice', params=f'count={count}&'
                                             f'period={period}&'
                                             f'version={version}')['price']

    def get_count(self, country, version=None):
        return self._send('getcount', params=f'country={country}&'
                                             f'version={version}')['count']

    def get_country(self, version=None):
        return self._send('getcountry', params=f'version={version}')['list']

    def get_proxy(self, state='all', descr='', nokey=False):
        params = f'state={state}'\
                 f'&descr={descr}'

        if nokey:
            params += '&nokey'

        return self._send('getproxy', params=params)['list']

    def set_type(self, ids, types):
        return self._send('settype', params=f'ids={ids}&'
                                            f'type={types}')

    def set_descr(self, new, ids=None, olds=None):
        params = f'new={new}'

        if ids:
            params += f'&ids={ids}'
        if olds:
            params += f'&olds={olds}'

        return self._send('setdescr', params=params)['count']

    def buy(self, count, period, country, version=None, types=None, descr='', auto_prolong=False, nokey=False):
        params = f'count={count}'\
                 f'&period={period}'\
                 f'&country={country}'\
                 f'&version={version}'\
                 f'&types={types}'\
                 f'&descr={descr}'

        if auto_prolong:
            params += '&auto_prolong'
        if nokey:
            params += '&nokey'

        return self._send('buy', params=params)['list']

    def prolong(self, period, ids, nokey=False):
        params = f'period={period}'\
                 f'ids={ids}'
        if nokey:
            params += 'nokey'
        return self._send('prolong', params=params)['list']

    def delete(self, ids=None, descr=None):
        params = ''
        if ids:
            params += f'ids={ids}'
        elif descr:
            params += f'descr={descr}'
        return self._send('delete', params=params)['count']

    def check(self, ids):
        return self._send('check', params=f'ids={ids}')['proxy_status']
