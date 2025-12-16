def knapsack_solver():
    items = [
        {"name": "노트북", "wt": 3, "val": 12},
        {"name": "카메라", "wt": 1, "val": 10},
        {"name": "책", "wt": 2, "val": 6},
        {"name": "옷", "wt": 2, "val": 7},
        {"name": "휴대용 충전기", "wt": 1, "val": 4}
    ]
    
    n = len(items)

    try:
        w_input = input("배낭 용량을 입력 하세요 : ")
        W = int(w_input)
    except ValueError:
        print("유효한 정수(배낭 용량)를 입력해주세요.")
        return

    A = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_wt = items[i - 1]["wt"]
        item_val = items[i - 1]["val"]

        for w in range(1, W + 1):
            if item_wt > w:
                A[i][w] = A[i - 1][w]
            else:
                val_with = item_val + A[i - 1][w - item_wt]
                val_without = A[i - 1][w]
                
                A[i][w] = max(val_with, val_without)

    max_satisfaction = A[n][W]
    print(f"최대 만족도: {max_satisfaction}")