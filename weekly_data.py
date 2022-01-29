import csv
import os
from datetime import datetime
import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
save_path = '..//CGFTCoin/weekly'

def weekly_data(list):
    key = "45OM2CS6NLPXEJH0"
    for currency in list:
        print("Weekly Data "+ currency + " starts at ", datetime.now())

        url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&symbol='+currency+'&market=USD&apikey='+key
        r = requests.get(url)
        data = r.json()
        week_data = data['Time Series (Digital Currency Weekly)']

        file_name = currency + ".csv"
        completeName = os.path.join(save_path, file_name)

        a_file = open(completeName, "w")
        writer = csv.writer(a_file)
        writer.writerow(["Date", "Market Cap"])

        for key, value in week_data.items():
            #print(key, ":", value['6. market cap (USD)'])
            writer.writerow([key, value['6. market cap (USD)']])

        a_file.close()
        print("Weekly Data " + currency + " ends at " , datetime.now())



