# 11.3
import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_cards(cards):
    card=random.choice(cards)
    return card
def calc_scores(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21 :
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_sum, ai_sum):
    if user_sum == ai_sum:
        return "Draw"
    elif ai_sum == 0:
        return "you lose , opponent has blackjack"
    elif user_sum ==0:
        return "you win with a blackjack"
    elif user_sum >21:
        return "you went over ,you lose"
    elif ai_sum >21:
        return "oppponent went over you win"
    elif user_sum >ai_sum:
        return "you win"
    else:
        return "you lose"
def play_game():
    user=[]
    ai=[]
    is_game_over=False

    for i in range(2):
        user.append(deal_cards(cards))
        ai.append(deal_cards(cards))
    # print(user,ai)

    while not is_game_over:
        user_sum=calc_scores(user)
        ai_sum=calc_scores(ai)
        print(f"your cards : {user} , your scores : {user_sum}")
        print(f"ai first cards : {ai[0]}")

        if user_sum == 0 or ai_sum == 0 or user_sum >21:
            is_game_over = True
        else:
            user_should_deal=input("type 'y' to get another card ,type 'n' to pass :")
            if user_should_deal == 'y':
                user.append(deal_cards(cards))
            else:
                is_game_over = True
    while ai_sum!=0 and ai_sum <17:
        ai.append(deal_cards(cards))
        ai_sum=calc_scores(ai)


    print(f"your final hand :{user},final score :{user_sum}")
    print(f"ai final hand :{ai},final score :{ai_sum}")
    print(compare(user_sum, ai_sum))
    ans=input("are you want to play again? (y/n):")
    if ans=="y":
        play_game()
    else:
        print("comeback buddy!!!")


play_game()