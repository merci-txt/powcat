import argparse
import scraper

description = 'Powcat scrapes proxies from the internet.'
protocol_help = 'Supported protocol.'
country_help = 'Location as Alpha-2 ISO country-code, separate multiple by comma. Defaults to all.'
timeout_help = 'Latency as integer in milliseconds. Defaults to 250.'
ssl_help = 'Support for ssl-encryption. Only respected when protocol is http. Defaults to all.'
anonymity_help = 'Proxy-anonymity. Defaults to all.'
test_help = 'Test proxies after retrieving. Use as flag.'

logo = '''
88""Yb  dP"Yb  Yb        dP  dP""b8    db    888888 
88__dP dP   Yb  Yb  db  dP  dP   `"   dPYb     88   
88"""  Yb   dP   YbdPYbdP   Yb       dP__Yb    88   
88      YbodP     YP  YP     YboodP dP""""Yb   88 

v1 by merci.txt
'''

if __name__ == '__main__':
    print(logo)

    parser = argparse.ArgumentParser(prog='powcat', description=description)
    parser.add_argument('--protocol', help=protocol_help, action='store', choices=['http', 'socks4', 'socks5'], required=True)
    parser.add_argument('--country', help=country_help, action='store', default='all', required=False)
    parser.add_argument('--timeout', help=timeout_help, action='store', type=int, default=250, required=False)
    parser.add_argument('--ssl', help=ssl_help, action='store', choices=['yes', 'no', 'all'], default='all', required=False)
    parser.add_argument('--anonymity', help=anonymity_help, action='store', choices=['transparent', 'anonymous', 'elite', 'all'], default='all', required=False)
    parser.add_argument('--test', help=test_help, action='store_true', required=False)
    args = parser.parse_args()

    print('[Scraping proxies]')
    proxies = scraper.scrape(args.protocol, args.timeout, args.country, args.ssl, args.anonymity)

    for proxy in proxies:
        print(proxy)