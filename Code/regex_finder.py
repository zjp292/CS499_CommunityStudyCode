import pandas as pd
import matplotlib.pyplot as plt

keywords = [
    'Dune',
    'Frank Herbert',
    'Dune Messiah',
    'Children of Dune',
    'God Emperor of Dune'
]

csv_to_write = 'D:/commStudyTwo/data_set_2.csv'


def find_pattern(keywords, dataset):
    df = pd.read_csv(dataset)

    filtered_posts = df[df['content'].str.contains('|'.join(keywords), case=False, na=False)]
    return filtered_posts

def find_unique_posters(excel_file):
    df = pd.read_csv(excel_file)

    df['poster_url'] = df.iloc[:, 9].str.split('/', n=3).str[:3].str.join('/')

    print(df['poster_url'])

    unique_posters_count = df['poster_url'].nunique()

    return unique_posters_count

# get the posts from the regex pattern finding function
posts = find_pattern(keywords,'D:/commStudyTwo/month_data.csv')
unique_users = find_unique_posters('D:/commStudyTwo/data_set_2.csv')
print(unique_users)

posts.to_csv(csv_to_write, index=False)

posts['created_at'] = pd.to_datetime(posts['created_at'])

posts['date'] = posts['created_at'].dt.date

posts_date = posts.groupby('date').size()
#print(posts_date)

plt.figure(figsize=(10, 6))
posts_date.plot(kind='line', marker='o', color='blue')
plt.title('Posts About Dune From March 1st to April 1st')
plt.xlabel('Date')
plt.ylabel('Number of posts')
plt.grid(True)
plt.tight_layout()
plt.show()