from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.jungle                        # 'jungle'라는 이름의 db를 만듭니다.

# # MongoDB에 insert 하기

# # 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.users.insert_one({'name':'bobby','age':21})
# db.users.insert_one({'name':'kay','age':27})
# db.users.insert_one({'name':'john','age':30})
# MongoDB에서 데이터 모두 보기

# db.games.insert_one({'name':'League of legends','id' : '손가든'})
# db.games.insert_one({'name':'MapleStory','id' : '죽창으로찔러'})
# all_users = list(db.users.find({}))
all_games = list(db.games.find({}))
# # 참고) MongoDB에서 특정 조건의 데이터 모두 보기
# same_ages = list(db.users.find({'age':21}))
same_ids = list(db.games.find({'id':'죽창으로찔러'}))
print(all_games[0])
print(all_games[0]['name'])

for game in all_games:
    print(game)
# print(all_users[0])         # 0번째 결과값을 보기
# print(all_users[0]['name']) # 0번째 결과값의 'name'을 보기

# for user in all_users:      # 반복문을 돌며 모든 결과값을 보기
#     print(user)

game = db.games.find_one({'name':'League of legends'} , {'_id':False})
print(game)

db.games.update_one({'name':'MapleStory'},{'$set':{'id':'죽창으로 찔러'}})
game = db.games.find_one({'name':'MapleStory'},{'_id':False})
print(game)
# user = db.users.find_one({'name':'bobby'})
# print(user)

# # 그 중 특정 키 값을 빼고 보기
# user = db.users.find_one({'name':'bobby'},{'_id':False})
# print(user)

# db.users.delete_one({'name':'bobby'}) # 중복된 데이터가 여러개 일 경우 하나씩 사라짐

# user = db.users.find_one({'name':'bobby'})
# print(user)
# db.games.delete_many({})

