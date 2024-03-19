import random
import time

def get_me_choice():
    me_choice = input("청개구리 가위,바위,보를 시작합니다. 가위, 바위, 보를 입력해주세요 : ")
    if me_choice in ['가위', '바위', '보']:
        return me_choice
    else:
        get_me_choice()

def get_computer_choice():
    choices = ['가위', '바위', '보']
    return random.choice(choices)

def input_countdown(seconds):
    timer_start = time.time()
    my_choice = input("개굴, 이겼다, 졌다를 입력해주세요 : ")
    timer_end = time.time()
    if timer_end - timer_start <= seconds:
        return my_choice
    else:
        print("시간초과!")
        return 'timeout'    
    


def determine_winner(me_choice, computer_choice, my_choice):
    if me_choice == computer_choice:
        if my_choice == '개굴':
            return '게임에 승리하셨습니다!'
        else:
            return '게임에 패배하셨습니다!'
    elif (me_choice == '가위' and computer_choice == '보') or \
         (me_choice == '바위' and computer_choice == '가위') or \
         (me_choice == '보' and computer_choice == '바위'):
        if my_choice == '졌다':
            return '게임에 승리하셨습니다!' 
        else:
            return '게임에 패배하셨습니다!'
    else:
        if my_choice == '이겼다':
            return '게임에 승리하셨습니다!'
        else:
            return '게임에 패배하셨습니다!'

def play_game():
    me_choice = get_me_choice()
    computer_choice = get_computer_choice()
    print(f"나: {me_choice}")
    print(f"상대는 [{computer_choice}]를 냈습니다.")
    my_choice = input_countdown(3)
    print(determine_winner(me_choice, computer_choice, my_choice))

while True:
    play_game()
    choice = input("게임을 다시 하려면 1, 그만하려면 2를 누르세요: ")
    if choice == '2':
        break

