import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    new_c1= []
    for k in movies:
   
        new_1 = {
            'id' : k.get('id'),
            'title' : k.get('title'),
            'poster_path' : k.get('porster_path'),
            'vote_average' : k.get('vote_average'),
            'overview' : k.get('overview'),
            'genre_ids' : k.get('genre_ids')
        }

        new_1['genre_name'] = new_1.pop('genre_ids')   #genre_ids를 바꾸는 과정

        new_a = []


        for i in new_1['genre_name']:                  #genre_name 밸류를 바꾸는 과정
            for j in range(len('genre_name')):
                if i == genres[j]['id']:
                    new_a.append(genres[j]['name'])

        new_1['genre_name'] = new_a
        new_c1.append(new_1)


    return new_c1
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))