def solve_stairs_dp():
    try:
        n_input = input("계단의 개수를 입력하시오: ")
        n = int(n_input)
        
        if n < 0:
            print("계단 수는 0 이상의 정수여야 합니다.")
            return
        
    except ValueError:
        print("유효한 정수를 입력해주세요.")
        return
    
    if n == 0:
        result = 1 
    elif n == 1:
        result = 1 
    else:
        
        ways = [0] * (n + 1)
        
        ways[0] = 1 
        ways[1] = 1 
        
    
        for i in range(2, n + 1):
            
            ways[i] = ways[i - 1] + ways[i - 2]
            
        result = ways[n]

    print(f"{n}개의 계단을 오르는 방법의 수는 {result}가지입니다.")
    
solve_stairs_dp()