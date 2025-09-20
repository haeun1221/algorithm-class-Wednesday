#############################################################################
#  시스템 스택 호출과 재귀함수를 이용한 팩토리얼 계산 콘솔 인터렉티브 프로그램 
#  작성자: 조하은
#  작성일: 2025-09-20
#  순환(recursion)과 반복(iteration)의 차이점 이해
#  - 반복문 기반과 재귀 기반의 팩토리얼 계산 함수 구현
#  - 유효성 검사 포함 (0 이상 정수 확인)
#  - 문자열 입력 → 정수 변환 → 유효성 검사 → 팩토리얼 계산까지 포함된 콘솔 프로그램 형태
#  - q 또는 quit 입력 시 종료
#############################################################################

def factorial_iter(n):
    # 반복문 기반 n!
    result = 1
    for k in range(2, n+1):
        result *= k
    return result 

def factorial_rec(n):
    # 재귀적으로 문제 해결 n!

    # 1. base case (재귀호출 종료 조건)
    if n == 0 or n == 1: 
        return 1
    
    # 2. 재귀 분할
    return n * factorial_rec(n-1) # 함수 자기 자신 호출

def main():
    while True:
        user_input = input("\n정수를 입력하세요 (종료하려면 'q' 또는 'quit'): ").strip().lower()

        # 종료 명령 확인
        if user_input in ('q', 'quit'):
            print("프로그램을 종료합니다.")
            break

        try:
            n = int(user_input)
            
            # 유효성 검사: 0 이상의 정수만 허용
            if n < 0:
                print("오류: 0 이상의 정수를 입력해주세요.")
                continue

            # 팩토리얼 계산 및 결과 출력
            print(f"반복문 기반: {factorial_iter(n)}")
            try:
                print(f"재귀 기반: {factorial_rec(n)}")
            except RecursionError:
                print("재귀 기반 계산: 입력값이 너무 커서 계산할 수 없습니다. 재귀 깊이 한계를 초과했습니다.")
        
        except ValueError:
            print("오류: 올바른 정수 또는 종료 명령어를 입력해주세요.")


if __name__ == "__main__":
    main()