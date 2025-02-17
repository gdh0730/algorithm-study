'''
Sudo 코드
1. N 입력 (사진틀 수)
2. total 입력 (추천 횟수)
3. 추천 리스트 입력
4. 사진틀 = []
5. 추천 리스트를 순서대로 탐색:
    학생이 사진틀에 있으면:
        - 추천 수 +1
    학생이 사진틀에 없으면:
        - 사진틀이 꽉 찼으면:
            - 추천 수가 가장 작은 학생 중, 가장 먼저 들어온 학생 제거
        - 새 학생을 사진틀에 추가 (추천 수 1, 게시 시점 기록)
6. 사진틀에 남아있는 학생 번호를 오름차순으로 출력
'''
# 입력 처리
N = int(input())  # 사진틀 수
total = int(input())  # 추천 횟수
recommendations = list(map(int, input().split()))  # 추천받은 학생 번호 리스트

frames = []  # 사진틀 (학생 정보: [학생 번호, 추천 수, 게시 시점])

for time, student in enumerate(recommendations):
    # 1) 이미 게시된 학생이면 추천 수 증가
    found = False
    for frame in frames:
        if frame[0] == student:
            frame[1] += 1
            found = True
            break

    # 2) 게시되어 있지 않으면 새로 게시
    if not found:
        # 사진틀이 꽉 찬 경우
        if len(frames) == N:
            # 추천 수 오름차순 -> 게시 시점 오름차순으로 정렬 후 제거
            frames.sort(key=lambda x: (x[1], x[2]))
            frames.pop(0)  # 가장 추천 수 적고 오래된 학생 제거
        # 새 후보 추가
        frames.append([student, 1, time])

# 3) 최종 후보 출력 (번호 오름차순)
frames.sort(key=lambda x: x[0])  # 학생 번호로 정렬
for frame in frames:
    print(frame[0], end=' ')
