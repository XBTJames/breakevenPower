# breakevenPower
This takes publicly avaliable CoinMetrics Bitcoin Mining revenue data and calculates breakeven historical power prices according to the Bitcoin miner model efficiency

This project relies on data from coinmetrics.io. charts.coinmetrics.io/network-data. Asset = BTC ; Metrics = Mining --> Miner Revenue per Hash per Sec (USD). Time is "All", then download CSV. I call this data "Hashprice Data.csv", you can call it what you want but you will need to change the filename on line 13 in the code if you use a different file name.

example functions:
breakevenPower(95) --> Will show the breakeven MWH price over time for a 95J/TH miner since May 31, 2016
breakevenPower(34.5, pd.to_datetime('2020-02-27')) --> Will show the breakeven MWH price over time for a 34.5J/TH miner since February 27th, 2020
