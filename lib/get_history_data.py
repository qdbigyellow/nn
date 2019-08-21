from contant import CONST
from data_server import DataServer

def get_data():
    srv = DataServer(CONST.DATA_SRV, CONST.APIKEY)
    print(srv.request(f"Get data from {srv.address}", function="TIME_SERIES_INTRADAY", symbol="MSFT", interval="30min").content)

if __name__ == '__main__':
    get_data()