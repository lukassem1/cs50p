import json
import sys
import requests

try:
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    r = requests.get(url).json()
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    x = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    raise SystemExit


rr = r['bpi']['USD'].values()
rrr = float(list(rr)[4])
result = x * rrr
print(f"${result:,.4f}")
