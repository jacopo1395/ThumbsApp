import facebook

app_secret = ''
app_id = ''
token = ''

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
