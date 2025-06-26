import random
word_list=['apple','beautiful','potato','supriya']
lives=6
chosen_word=random.choice(word_list)
print(chosen_word)
display=[]
for i in range(len(chosen_word)):
    # display=display+'_'
    display+='_'
    # display.append="_"
print(display)
game_over=False
while not game_over:
    gussed_letter=input("guess a letter :").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==gussed_letter:
            display[position]=gussed_letter
    print(display)
    if gussed_letter not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("you lose")
    if '_' not in display:
        game_over=True
        print("you win")
