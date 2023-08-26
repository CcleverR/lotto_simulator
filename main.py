import unittest    
import random

#중복값 제거
def dedupe(my_random):
    #중복 제거후 새로만들 리스트
    my_random_new=[]

    if list(my_random)==list(set(my_random)):
        for i in my_random:
            if i not in my_random:
                my_random.append(i)
    else:
        if i not in my_random_new:
            my_random_new.append(i)

    return my_random_new


#맞는 로또번호 저장
# 컴퓨터가 임의의 수를 정해서 저장해둠
def correct_rad():
    return random.sample(range(1,46),6)

# 로또 번호 확인
# 랜덤6개수와 저장된 수를 정렬후 비교
def compare(my_random,correct_random):

    # 보너스 번호는 컴퓨터가 뽑는 것.
    # 보너스번호랑 correct_random이랑 겹치면 안되는데 어떡하지

    bonus = 0
    while True:
        bonus=random.randint(1,46)
        if bonus not in correct_random:
            break

    print(f"보너스 번호: {bonus}")
    
   #bonus와 correct_random을 비교해 True가 나온경우->5등
    a=bonus in my_random
    cnt=0
    num=1

    for i, j in zip(correct_random,my_random):
        print(f"{num}번째:{i},{j},{i==j}")
      
        if (i==j)==True:
            cnt+=1
        print(f"맞은 개수:{cnt}")

    # 2등인 경우, cnt ==5 and bonus in my_random
    # 1등인 경우, cnt == 6
    # 3등인 경우, cnt == 5
    # 4등인 경우, cnt == 4
    # 5등인 경우, cnt == 3

    if cnt == 5 and bonus in my_random:
        print('2등입니다.')
    elif cnt == 6:
        print('1등입니다.')
    elif cnt <= 5 and cnt >= 3:
        print(f'{8-cnt}등입니다.')
    else:
        print("낙첨입니다.")

# 자동으로 로또 번호 생성
def auto():
    return sorted(random.sample(range(1,46),6))

    #random.sample: 지정된 수에서 랜덤으로 뽑아 리스트로 반환해주는 함수
    #거기다가 정렬함

# 반자동으로 로또 번호 생성   
#왜 try 되는 구간이 아예 번호고르기부터 되는지 모르겠음
#제대로 해도 안돼


def half_auto():
    #뽑은수 따로 저장
        #이거 안쓰면 뭐하라그랬더라
        # FIXME: n개 입력 받았는데, n개보다 많은 수를 입력한 경우
        # -> N개의 입력 범위를 벗어나면 N개 다시 입력하게하기
        # FIXME: 1부터 45까지 이외의 범위 벗어나는 수 입력되는 문제
        # -> 입력을 받았을때 범위를 IF문으로 정해서 에러 해결 
    
        while True:
            choice_num=int(input("몇개의 수를 입력하시겠습니까?:"))#입력하고 싶은 수
            print(f"{choice_num}개의 수를 입력해주세요:")
            if choice_num >= 6:
                print("1~5 사이 수를 입력해주세요.")
            break


        my_random=[]
            
        while len(my_random)<choice_num:
            userInput=list(map(int,input().split()))
            for i in userInput:
                if len(my_random)==choice_num:
                    print("기존리스트와 수가 같은경우 뒤에는 다 나가리임")
                    break
                if int(i)<1 or int(i)>45:
                    print("범위가 벗어나는경우 다시입력해야됨")
                    continue
                my_random.append(int(i))

       
        print(my_random)



        
        #my_random=my_random[0]+my_random[1:]
        #print(my_random)
        #if 1>my_random or my_random>45:
            #print("다시입력하셈")
        
        lotto_numbers=list(range(1,46))
        
        for i in my_random: #[3,4,10]
            # lotto_numbers = [1~45]
            # my_random = [3,4,10]
            lotto_numbers.remove(i)

        for i in random.sample(lotto_numbers,6-choice_num):
            my_random.append(i)

        #6개에서 나머지 랜덤수로 채우기

        return sorted(my_random)

# 수동으로 로또 번호 생성
def manu(): 
    print("6개의 수를 입력해주세요:")

    my_random=list(map(int,input().split()))

    return sorted(my_random)

# 게임을 여러판 할수있게 선택권 두기
#def game_count():
#    print("게임 몇판 하실거에요(0~):")
#    game_count=int(input())
#    while True:
#        if game_count>0 and game_count<10000000:
#            next_count=game_count-1
#            return next_count
#        elif game_count==0: 
#            break 
#        else:
#            print("다시입력하시오.")
            
                   
#전체적인 if문 어떻게 넣지
#예외처리 함수 만들어서 처리할수있는가


if __name__=="__main__":
    # 로또 시뮬레이션
    print("lotto simulator")
    print("로또 프로그램을 시작합니다.")
    print("1:자동")
    print("2:반자동")
    print("3:수동")
    print("4:프로그램 종료")

    #예외처리 가능?

    while True:
            n=input("번호를 선택해주세요:")
            n=int(n)
            #게임 횟수 입력 여기다가 할거임
            game_count=int(input("게임 몇번하시겠사요:"))
            for i in range(0,game_count):
            #함수 count여기다가 넣어야하나
                print("------------------------------------------")
                print(f"게임 횟수:{i+1}")
                if n==1: 
                 #game_value=auto_n      #자동
#                 game_count() 
                # 자동으로 생성된 6개 번호 리스트가 lotto_numbers에 대입 e.g) [a,b,c,d,e,f]
                    print("로또번호를 자동으로 생성합니다.")
                    user_numbers = auto() 
                    print(f"내 로또 번호: {user_numbers}")

                    answer_numbers = correct_rad()

                    compare(user_numbers, answer_numbers)
                elif n==2:      #반자동
                #game_value=half_auto_n
                #game_count()
                    print("로또번호를 반자동으로 생성합니다")
                    user_numbers=half_auto()
                    print(f"내 로또번호:{user_numbers}")
                    answer_numbers=correct_rad()
                    compare(user_numbers,answer_numbers)
                elif n==3:      #수동
                #game_value=man호호
#                 game_count()
                    print("로또 번호를 수동으로 입력합니다.")
                    user_numbers=manu()
                    print(f"내 로또번호:{user_numbers}")
                    answer_numbers=correct_rad()
                    compare(user_numbers,answer_numbers)
                elif n==4:
                    print("프로그램이 종료됩니다.")
                    break
                else:
                    print("다시 입력하시오.")
      
            i-=1
        

#다 잘 돌아가긴 하는데
# 예외처리
# 중복 ->함수 만들었는디,,어떻게 합치냐
# 이거만 신경쓰면될듯        


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