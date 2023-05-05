from requests import get

def scrape(protocol: str = 'all', timeout: int = 10000, country: str = 'all', ssl: str = 'all', anonymity: str = 'all') -> list[str]:
    '''
    Scrapes proxies from the proxyscrapeAPI and returns them as an array.
    Returned array-format: ['ip:port', ...]

    Parameters:
    :param str protocol: Can be 'http', 'socks4', 'socks5' or 'all'.
    :param int timeout: Proxy-latency in milliseconds.
    :param str country: Can be single Alpha-2-ISO country code, multiple codes separated by a comma or 'all'.
    :param str ssl: Can be 'yes', 'no' or 'all'. Only respected when protocol is 'http' or 'all'.
    :param str anonymity: Can be 'transparent', 'anonymous', 'elite' or 'all'.

    Return:
    :return: ['ip:port', ...]
    :rtype: list[str]

    Errors:
    :raises ValueError: If no proxies where returned by the API.
    :raises ConnectionError: If process could not reach API.
    '''

    try:
        proxies = get(f'https://api.proxyscrape.com/v2/?request=displayproxies&protocol={protocol}&timeout={timeout}&country={country}&ssl={ssl}&anonymity={anonymity}')
        proxies = proxies.text.split('\r\n')[0:-1]

    except:
        raise ConnectionError('Could not reach API!')
    
    if len(proxies) == 0:
        raise ValueError('No proxies where returned by the API!')
    
    return proxies
