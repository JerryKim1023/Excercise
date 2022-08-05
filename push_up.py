print('상체운동 시~~~작!!!')


print('최고 횟수를 입력하세요')
input_Max = int(input())

print('최소 횟수를 입력하세요')
input_Min = int(input())

while input_Max-input_Min >= 1:

    print(f"이번 운동은 {input_Max}회 입니다.")
    a = input()
    input_Max -= 1

    print(f"이번 운동은 {input_Min}회 입니다.")
    a = input()
    input_Min += 1

print("상체 운동이 끝났습니다!!")