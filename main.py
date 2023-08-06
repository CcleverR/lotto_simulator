import random

print("lotto simulator")

#맞는 로또번호 저장
def correct_rad():
    global correct_random
    correct_random=[]
    for i in range(6):
        correct_randoms=random.randint(1,45)
        correct_random.append(correct_randoms)
    
    return correct_random

# 로또 번호 확인
def compare(my_random,correct_random):
    my_random=sorted(my_random)
    correct_random=sorted(correct_random)

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
    print("로또번호를 자동으로 생성합니다.")
    global my_random
    try:
        my_random=[]
        my_random=random.sample(range(1,45),6)
        print(f"내 로또 번호: {sorted(my_random)}")
    finally:
        print("")
    return my_random

# 반자동으로 로또 번호 생성   *************머리아파*************
#왜 try 되는 구간이 아예 번호고르기부터 되는지 모르겠음
#제대로 해도 안돼

def half_auto():
    print("로또번호를 반자동으로 생성합니다.")
    global my_random
    my_random=[]

    choice_num=input("몇개의 수를 입력하시겠습니까?:")
    choice_num=int(choice_num)
    print("수를 다시 입력하세요:",choice_num(input()))

    print(f"{choice_num}개의 수를 입력해주세요:")

    num=list(map(int,input().split()))
    my_random.append(num)
    my_random=my_random[0]+my_random[1:]

    for i in range(6-choice_num):
        my_random=random.sample(range(1,45),(6-choice_num))
    
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

# 로또 시뮬레이션
print("로또 프로그램을 시작합니다.")
print("1:자동")
print("2:반자동")
print("3:수동")
print("4:프로그램 종료")


if __name__=="__main__":
    while True:
        try:
            n=input("번호를 선택해주세요:")
            n=int(n)
        
            if n==1:        #자동
                 auto()
                 correct_rad()
                 compare(my_random,correct_random)
            elif n==2:      #반자동
                 half_auto()
                 correct_rad()
                 compare(my_random,correct_random)
            elif n==3:      #수동
                 manu()
                 correct_rad()
                 compare(my_random,correct_random)
            elif n==4:
                print("프로그램이 종료됩니다.")
            break
        except:
            print("다시 입력해주세요:")
      
     
        

#피드백 내용
#프로그램 오류 뜨지 않게끔 해야되는거임 (예외처리)

#1. 번호를 다르게입력했을때 프로그램 종료떠버림(O)
#2. 중복되면 안됨 (자동만 함, (반자동, 수동))
#3. 번호 적게 입력하면 다시입력하게끔 해야됨 (이건또 어떻게함)
#4. 게임수 지정 (이거는..?)




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