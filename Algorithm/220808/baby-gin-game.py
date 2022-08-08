# 0~9까지의 카드 중 6개의 카드를 임의로 뽑는다
# 3장의 카드가 연속이면 run
# 3장의 카드가 동일하면 triplet
# 6장의 카드가 run 과 triplet으로만 이루어져 있으면 baby-gin이라고 한다.
# => run2개 / triplet2개 / run1개 + triplet1개로 구성되어야 한다

# 6자리의 숫자를 입력받으면 baby-gin여부를 판단하는 프로그램을 작성하여라

# ex) 667767 => 두개의 triplet이므로 baby-gin
# ex) 054060 => 한개의 triplet과 한개의 run으로 이루어졌으므로 baby-gin

'''
i = 0
tri = run = 0
while i < 10 :
    if c[i] >= 3 : # triplet 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1 : # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2 : print("Baby Gin")
else : print("Lose")
'''