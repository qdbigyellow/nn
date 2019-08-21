import requests

class DataServer:
    def __init__(self, address, key):
        self.address=address
        self.key=key

    def request(self, what,function, symbol, interval, **kwargs):
        api=f'{self.address}function={function}&symbol={symbol}&interval={interval}&apikey={self.key}'
        print(f"{what} from {api}")
        return requests.get(api)