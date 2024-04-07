import json
import requests
import pandas as pd
import time

hashtag = 'books'
URL = f'https://mastodon.social/api/v1/timelines/tag/{hashtag}'
params = {
    'limit': 40
}

start = pd.Timestamp("2024-03-01", tz='utc')
is_end = False

results = []

while True:
    r = requests.get(URL, params=params)
    toots = json.loads(r.text)

    if len(toots) == 0:
        break

    for t in toots:
        if 'created_at' in t:
            timestamp = pd.Timestamp(t['created_at'], tz='utc')
            if timestamp <= start:
                #is_end = True
                break
            print(t)
            results.append(t)

    if len(toots) < params['limit']:
        break

    max_id = toots[-1]['id']
    params['max_id'] = max_id



df = pd.DataFrame(results)
print(df.head)
seconds_since_epoch = str(time.time())
df.to_csv('D:/commStudyTwo/' + seconds_since_epoch + ".csv", index=False)