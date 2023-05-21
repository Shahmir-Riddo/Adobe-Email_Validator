from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

@api_view(['POST'])
def index(request):
    email = request.data.get('email')
    url = 'https://auth.services.adobe.com/signin/v2/users/accounts'
    payload = {
        'username': email,
        'hasT2ELinked': False
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'x-ims-clientid': 'CCHomeWeb1',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Mode': 'cors',
        'Origin': 'https://auth.services.adobe.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Mobile/15E148 Safari/604.1',
        'Referer': 'https://auth.services.adobe.com/en_US/index.html',
    }


    if 'proxy_username' in request.data and 'proxy_password' in request.data:
        proxy_username = request.data['proxy_username']
        proxy_password = request.data['proxy_password']
        proxies = {
            'http': f'http://{proxy_username}:{proxy_password}@proxy_address:proxy_port',
            'https': f'https://{proxy_username}:{proxy_password}@proxy_address:proxy_port'
        }
    else:
        proxies = None

    response = requests.post(url, json=payload, headers=headers, proxies=proxies)
    json_data = response.json()

    if isinstance(json_data, list) and len(json_data) > 0:
        has_t2e_linked = json_data[0].get('hasT2ELinked', False)
        if has_t2e_linked:
            result = 'success'
        else:
            result = 'fail'
    else:
        result = 'fail'

    return Response({'result': result})
