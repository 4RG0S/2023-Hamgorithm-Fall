def main():
    l, c = map(int, input().split())
    li = sorted(input().split())
    
    # 문자열이 모음 1개, 자음 2개 이상 가졌는지 확인하는 함수
    def check(str):
        mo = 0
        for s in str:
            if s in ['a', 'e', 'i', 'o', 'u']:
                mo += 1
        
        if len(str) - mo > 1 and mo > 0:
            return True
        return False
    
    # 오름차순으로 문자열을 생성하는 함수
    def fun(str, num):
        if len(str) == l and check(str):
            print(str)
        
        for i in range(num, c):
            fun(str+li[i], i+1)
    
    fun("", 0)    
    
if __name__ == "__main__":
    main()