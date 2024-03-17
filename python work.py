import random

def get_me_choice():
    me_choice = input("청개구리 가위,바위,보를 시작합니다. 가위, 바위, 보를 입력해주세요 : ")
    return me_choice.lower()

def get_computer_choice():
    choices = ['가위', '바위', '보']
    return random.choice(choices)

def determine_winner(me_choice, computer_choice):
    if me_choice == computer_choice:
        return "개굴"
    elif (me_choice == '가위' and computer_choice == '보') or \
         (me_choice == '바위' and computer_choice == '가위') or \
         (me_choice == '보' and computer_choice == '바위'):
        return "게임에 패배하셨습니다!"
    else:
        return "게임에 승리하셨습니다!"

def play_game():
    me_choice = get_me_choice()
    computer_choice = get_computer_choice()
    print(f"나: {me_choice}")
    print(f"상대는 [{computer_choice}]를 냈습니다.")
    print(determine_winner(me_choice, computer_choice))

while True:
    play_game()
    choice = input("게임을 다시 하려면 1, 그만하려면 2를 누르세요: ")
    if choice == '2':
        break
