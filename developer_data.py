import os

import pandas as pd
from datetime import datetime

save_path = '..//CGFTCoin/developer'
def code_freq_to_excel(list):
    j = 0

    for i in list:
        print("Developer Data " + i + " starts at ", datetime.now())

        url = "https://api.github.com/repos/" + i + "/stats/code_frequency"
        df = pd.read_json(url)
        df.set_axis(["Date", "Additions", "Deletions"], axis=1, inplace=True)

        df["Date"] = pd.to_datetime(df["Date"].astype(int), unit='s')

        file_name = list[j].split('/')[0] + ".xlsx"
        completeName = os.path.join(save_path, file_name)

        df.to_excel(completeName, index=False)
        j += 1

        print("Developer Data " + i + " ends at ", datetime.now())
