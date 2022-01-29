from developer_data import *
from weekly_data import *

## TOP 5 (Tether does not have a source code in marketcap)
## Cardano does not have a GitHub repo (cardanoupdates.com)
## CentreHQ -> USD Coin ("centrehq/centre-tokens",)

coin = ["bitcoin/bitcoin","ethereum/go-ethereum","binance-exchange/binance-official-api-docs",
        "solana-labs/solana", "ripple/rippled"]

## Get Weekly MarketCap Data (www.alphavantage.co)
coin_list = ["BTC","ETH","BNB","SOL","XRP"]


code_freq_to_excel(coin)
weekly_data(coin_list)
