import facebook

app_secret = '57346db13d27470f88c956331bcf76b6'
app_id = '101075550373465'
token = 'EAACEdEose0cBAJ02Y7PfmcIZBRZBLv5pkXIRyyDxnLQIUHqHeECLYzMW2ZBZB5OFlA4kULIqjsl9ycUyJzdgJQVffwT6bk99tHOO8PK0x65xgmz4VpOjw8STBAtEABPZBvmxeSqDHO7h3EljhLWK58x2kwr0TxgJESnQLSQKzngZDZD'

graph = facebook.GraphAPI(access_token=token, version='2.2')
user = graph.request('me')
print(user['id'])
user_id = user['id']
photos = graph.request(user_id + '/photos')
# photo_id = photos['data'][1]['id']
# photo = graph.request(photo_id)
# print(photo)
# print(len(photo['likes']['data']))
for i in range(0, len(photos['data'])):
    print('----')
    photo_id = photos['data'][i]['id']
    photo = graph.request(photo_id)
    for p in photo['images']:
        like=len(photo['likes']['data'])
        print(p)
