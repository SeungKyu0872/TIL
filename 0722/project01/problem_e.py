import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    new_d1= []
    new_r1= []
    new_m1= []
    for i in range(len(movies)):                         # 제목을 리스트를 추출
        new_d1.append(movies[i]['id'])
        son_ = open(f'data/movies/{new_d1[i]}.json', encoding='UTF8')
        son_list = json.load(son_)    
        new_r1.append(son_list['release_date'][5:7])     # 날짜에서 월만 추출
    
    for j in range(len(movies)):                         # 12월을 추출
        if  new_r1[j] == '12' :
            new_m1.append(movies_list[j]['title'])
    

    return new_m1
    
    
    






# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))