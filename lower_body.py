import random

deck = []

# nums과 shapes 정의
shapes = ['♥ 스쿼트', '♣ 스쿼트', '♠ 오른발런지', '◆ 왼발런지']
nums = []
for i in range(2,11):
    nums.append(str(i))

JQKA = ['J 10', 'Q 10', 'K 10', 'A 11']
for c in JQKA:
    nums.append(c)

#조커 넣어주기
deck.append(('Joker', 'black 아무거나 10회'))
deck.append(('Joker', 'colored 아무거나 10회'))

# 덱 만들기
for shape in shapes:
    for num in nums:
        deck.append((shape, num))

# 카드섞기
random.shuffle(deck)

# 플레이어에게 카드 주기
player = []

last_card = deck.pop()
player.append(last_card)
print('하체 운동 시작!!!')
print("현재 패 >>", player[-1])


while True:

    # 플레이어가 운동을 한다.
    if len(deck) == 0:
        print("하체운동이 끝났습니다!")
        break
    else:
        a = input()
        last_card = deck.pop()
        player.append(last_card)
        print("현재 패 >>", player[-1])


