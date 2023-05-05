import argparse

parser = argparse.ArgumentParser(prog='powcat', usage='[Implement usage]', description='[Implement description]')

parser.add_argument('-p', '--protocol', action='store', choices=['http', 'socks4', 'socks5'], required=True)
parser.add_argument('-c', '--country', action='store', default='all', required=False)
parser.add_argument('-t', '--timeout', action='store', type=int, default=250, required=False)
parser.add_argument('-s', '--ssl', action='store', choices=['yes', 'no', 'all'], default='all', required=False)
parser.add_argument('-a', '--anonymity', action='store', choices=['transparent', 'anonymous', 'elite', 'all'], default='all', required=False)
parser.add_argument('--test', action='store_true', required=False)

args = parser.parse_args()
