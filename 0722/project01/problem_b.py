import json
from pprint import pprint


def movie_info(movie, genres):
    pass
    # 여기에 코드를 작성합니다.  
    
    
    new_1 = {
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'poster_path' : movie.get('porster_path'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_ids' : movie.get('genre_ids')
    }

    new_1['genre_name'] = new_1.pop('genre_ids')   #genre_ids를 바꾸는 과정

    new_a = []


    for i in new_1['genre_name']:                  #genre_name 밸류를 바꾸는 과정
        for j in range(len('genre_name')):
            if i == genres[j]['id']:
                new_a.append(genres[j]['name'])

    new_1['genre_name'] = new_a



    return new_1
    
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))