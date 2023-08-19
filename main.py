import unittest    
import random




#맞는 로또번호 저장
# 컴퓨터가 임의의 수를 정해서 저장해둠
def correct_rad():
    return random.sample(range(1,46),6)

# 로또 번호 확인
# 랜덤6개수와 저장된 수를 정렬후 비교
def compare(my_random,correct_random):

    bonus=random.randint(1,45)
    
    print(f"보너스 번호: {bonus}")
    
   #bonus와 correct_random을 비교해 True가 나온경우->5등
    a=bonus in my_random
    cnt=0
    num=1

    while True:
        try:
            for i, j in zip(correct_random,my_random):
                print(f"{num}번째:{i},{j},{i==j}")
                num+=1
                if (i==j)==True:
                    cnt+=1
                print(f"맞은 개수:{cnt}")

            if cnt>=6:
                print("1등입니다.")
            elif cnt==5 and a       :#위의 #경우
                print("2등입니다.")
            elif cnt==5:
                print("3등입니다.")
            elif cnt==4:
                print("4등입니다.")
            elif cnt==3:
                print("5등입니다.")
            elif cnt==2:
                print("등수가없습니다.")            
            elif cnt==1:
                print("등수가 없습니다.")
            elif cnt==0:          
                print("등수가 없습니다.")    

        finally:
            btn=input("그만하려면 'a'를 입력하세요:").lower()
            if btn=='a':
                break

# 자동으로 로또 번호 생성
def auto():
    return sorted(random.sample(range(1,46),6))

# 반자동으로 로또 번호 생성   
#왜 try 되는 구간이 아예 번호고르기부터 되는지 모르겠음
#제대로 해도 안돼

def half_auto():
    print("로또번호를 반자동으로 생성합니다.")
    global my_random
    try:
        my_random=[]

        choice_num=input("몇개의 수를 입력하시겠습니까?:")
        choice_num=int(choice_num)

        print(f"{choice_num}개의 수를 입력해주세요:")
 
        num=list(map(int,input().split()))
        my_random.append(num)
        my_random=my_random[0]+my_random[1:]

        for i in range(6-choice_num):
            my_random=random.sample(range(1,45),(6-choice_num))
    finally:
        print("")
    print(f"내 로또 번호: {sorted(my_random)}")

    return my_random

# 수동으로 로또 번호 생성
def manu():
    print("로또번호를 수동으로 생성합니다.")
    global my_random
    my_random=[]
    print("6개의 수를 입력해주세요:")

    num=list(map(int,input().split()))
    my_random.append(num)
    my_random=sum(my_random,[])

    print(f"내 로또 번호: {sorted(my_random)}")

    return my_random

# 게임을 여러판 할수있게 선택권 두기
def game_count():
    if game_value==auto:
        #try:
            count=int(input())
        #except:
            #print("잘못된 입력입니다\n다시 입력해주세요:")
    elif game_value==half_auto:
        #try:
            while True:
                if count==0:
                    break
                else:
                    count=int(input())
                    #전체적인 if문 어떻게 넣지
        #except:
            #print("잘못된 입력입니다.\n다시 입력해주세요")



if __name__=="__main__":
    # 로또 시뮬레이션
    print("lotto simulator")
    print("로또 프로그램을 시작합니다.")
    print("1:자동")
    print("2:반자동")
    print("3:수동")
    print("4:프로그램 종료")

    while True:
        try:
            n=input("번호를 선택해주세요:")
            n=int(n)
            #함수 count여기다가 넣어야하나
            
            if n==1: 
                 #game_value=auto_n      #자동
#                 game_count() 
                # 자동으로 생성된 6개 번호 리스트가 lotto_numbers에 대입 e.g) [a,b,c,d,e,f]

                print("로또번호를 자동으로 생성합니다.")
                user_numbers = auto() 
                print(f"내 로또 번호: {lotto_numbers}")

                answer_numbers = correct_rad()

                compare(user_numbers, answer_numbers)
            elif n==2:      #반자동
                #game_value=half_auto_n
                #game_count()
                half_auto()
                correct_rad()
                compare(my_random,correct_random)
            elif n==3:      #수동
                #game_value=manu
#                 game_count()
                manu()
                correct_rad()
                compare(my_random,correct_random)
            elif n==4:
                print("프로그램이 종료됩니다.")
            break
        finally:
            print("다시 입력해주세요:")
      
     
        

#피드백 내용
#프로그램 오류 뜨지 않게끔 해야되는거임 (예외처리)

#1. 번호를 다르게입력했을때 프로그램 종료떠버림(O)
#2. 중복되면 안됨 (자동만 함, (반자동, 수동))
#3. 번호 적게 입력하면 다시입력하게끔 해야됨 (이건또 어떻게함)
#4. 게임횟수 지정 




# 의사코드

# inport random
# 로또 유형을 선택해주세요  / if문
# 1. 자동
# 2. 반자동
# 3. 수동
# 4. 프로그래밍 종료
# 번호 선택  / input
# 1. 자동인경우 / random함수 6개 뽑아서 사용자 리스트에 저장
# 2. 반자동인경우 
# 수동으로 몇개 적을건지 확인 /sort사용해서 정렬
# 개수만큼 수동으로 적고 리스트에 저장, 자동으로 돌아갈 수 보여줌
# 6개에서 수동개수를 제외한 수 random 돌리기 , 리스트 저장
# 3. 수동인경우
# random으로 돌린다, 중복나오면 중복이다 하고 다시 돌리게끔
# random.randint(a,b)
# 결과 확인
# 로또 수7개를 random 으로 저장 
# 사용자 리스트 로또 수와 저장된 결과 비교
# 확인된 결과로 1~5등 순위 발표 / if문으로 1~5등 확인가능, 순위에 들지못하면 메시지 표시
# 프로그래밍 종료

# 로또 보여줄때 정렬로 나오는거임

#차라리 예외처리를 생각하면서 짜는게 더 나았을지도..
#수정해서 한번 더 뒤집을 생각하니까 너무 어려움