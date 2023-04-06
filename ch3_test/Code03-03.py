## 함수 선언 부분 ##
def myFunc() :
    #지역변수인데, 이 부분을 global 키워드를 추가해서 
    # 값의 변경 부분을 체크. 
    global gVar    
    gVar = 30
    print('함수를 호출함.함수 내부의 gVar : %d' % gVar)
    
## 전역 변수 선언 부분 ##
gVar = 100

## 메인 코드 부분 ##
if __name__ == '__main__' :
    print('메인 함수 부분이 실행됩니다.')
    myFunc()
    print('전역 변수 값:', gVar)

    
