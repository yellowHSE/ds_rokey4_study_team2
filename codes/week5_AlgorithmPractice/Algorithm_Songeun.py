# 홍송은
# 프로그래머스 해시 - 베스트 앨범
# https://school.programmers.co.kr/learn/courses/30/lessons/42579
"""
<해시(Hash)>
- 데이터를 키(key)-값(value) 쌍으로 저장하는 자료구조
- 키를 해시 함수에 넣어 나온 해시값을 배열의 인덱스처럼 사용
- 빠르게 데이터를 검색하거나 삽입 가능

my_dict["name"] →  
1. "name" 키를 해시 함수에 전달  
2. 계산된 해시값을 통해 메모리상의 위치(버킷) 결정  
3. 해당 위치에서 값을 바로 반환

<해시가 빠른 이유>
리스트처럼 처음부터 끝까지 반복하며 찾지 않고,
한 번의 계산으로 바로 원하는 위치에 접근할 수 있어 매우 빠르다.
탐색, 삽입, 삭제 모두 평균 시간 복잡도: O(1)

<파이썬의 해시 자료구조>
- 파이썬의 dict가 해시 기반 자료구조

<문제 요약>
1. 장르별로 총 재생 수가 많은 순서로 베스트 앨범 수록
2. 각 장르 안에서 재생 수가 많은 곡 순으로 정렬 (동점 시 고유번호가 낮은 순)
3. 각 장르에서 최대 2곡까지 수록
"""

def solution(genres, plays):
    answer = []

    # 앨범 구성
    albums = {}
    for i in range(len(genres)):
        if genres[i] in albums.keys():
            albums[genres[i]].append((i, plays[i]))
        else:
            albums[genres[i]] = list(tuple())
            albums[genres[i]].append((i, plays[i]))
    
    print(f"장르별 곡: {albums}")
    
    # 1. 속한 노래가 많이 재생된 장르를 먼저 수록
    # 2. 장르 내에서 많이 재생된 노래를 먼저 수록
    # 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록

    for k in albums:
        albums[k].sort(key=lambda x: (-x[1], x[0])) 
    
    print(f"장르 내 정렬: {albums}")
        
    # 장르별 총 재생수 기준 정렬
    sorted_genres = sorted(albums.keys(), key=lambda g: sum(p for i, p in albums[g]), reverse=True)

    # 각 장르에서 상위 2곡 추가
    for g in sorted_genres:
        top_songs = albums[g][:2]  # 최대 2곡
        for song in top_songs:
            answer.append(song[0])  # 고유번호만 추가

    return answer

test_genres = ["classic", "pop", "classic", "classic", "pop"]
test_plays = [500, 600, 150, 800, 2500]
result = solution(test_genres, test_plays)
print(result)