# 입력받기
arr = list(map(int, input().split()))

# 정렬 과정
while arr != [1, 2, 3, 4, 5]:  # 정렬이 완료될 때까지 반복
    for i in range(4):  # 나무 조각은 5개이므로 인접한 4쌍을 비교
        if arr[i] > arr[i + 1]:  # 현재 조각이 다음 조각보다 크면 교환
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            print(" ".join(map(str, arr)))  # 교환 후 현재 상태를 출력
