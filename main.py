import random

deck = []

# nums과 shapes 정의
shapes = '♥♣♠◆'
nums = []
for i in range(2,11):
    nums.append(str(i))
for c in 'JQKA':
    nums.append(c)

#조커 넣어주기
deck.append(('Joker', 'black'))
deck.append(('Joker', 'colored'))

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
print("현재 패 >>", player[-1])


while True:

    # 플레이어의 차례
    # 플레이어가 무언가를 한다..
    if len(deck) == 0:
        print("하체운동이 끝났습니다!")
        break
    else:
        a = input()
        last_card = deck.pop()
        player.append(last_card)
        print("현재 패 >>", player[-1])


