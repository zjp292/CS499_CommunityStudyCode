import pandas as pd
import time

seconds_since_epoch = str(time.time())
url = "https://mastodon.social/api/v1/timelines/tag/books?"
data = pd.read_csv(url)
df = pd.DataFrame(data)
first = df.iloc[:,0]

df.to_csv('D:/499_data/' + seconds_since_epoch + ".csv", index=False)

def data_col():
    seconds_since_epoch = str(time.time())
    url = "https://mastodon.social/api/v1/timelines/tag/books?"
    data = pd.read_csv(url)
    df = pd.DataFrame(data)

    df.to_csv('D:/499_data/' + seconds_since_epoch + ".csv", index=False)

if __name__ == "__main__":
    while True:
        data_col()
        time.sleep(15*60)
