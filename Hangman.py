import random
words = ['plate', 'python', 'jumble', 'easy', 'difficult', 'answer', 'xylophone', 'hangman', 'challenge','programming']

def hangman():
        
    choice = input("Do u want to play HangMan? Yes/No")
    if choice == 'Yes':
        while(True):
            attempts = 6
            word = random.choice(words)
            print('_' * len(word))
            guessed_word = ['_']*len(word)
            won = 0
            
            while(attempts):
                ch = input("Enter your guess!")
                if ch in word:
                    
                    pos = [i for i in range(len(word)) if word[i]==ch]
                
                    for i in pos:
                        guessed_word[i] = ch

                    #if right answer is reached
                    if "".join(guessed_word) == word:
                        print(f"YAY! You Won. The correct word was {"".join(guessed_word)}")
                        won = 1
                        break
                    
                    print(f"Right guess!! the current word is {"".join(guessed_word)}")
                    continue

                attempts -= 1
                print(f"Oops! seems to be wrong guess. U get {attempts} more choices")
            
            if won:
                repeat = input("Congratulations! do u want to play again? Yes/No")
                if repeat == "Yes":
                    continue
                return
            repeat = input(f"SAD! The correct word was {"".join(word)}. do u want to play again? Yes/No")
            if repeat == "Yes":
                continue
            return
    return 


hangman()
