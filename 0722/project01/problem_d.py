import json


def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    new_d1= []
    new_r1= []
    for i in range(len(movies)):
        new_d1.append(movies[i]['id'])
        son_ = open(f'data/movies/{new_d1[i]}.json', encoding='UTF8')
        son_list = json.load(son_)
        new_r1.append(son_list['revenue'])
        max_1 = sorted(new_r1,reverse=True)[0]
    for j in range(len(movies)):
        if  new_r1[j] == max_1 :
            moviename = movies_list[j]['title']
            


    return moviename

    



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
