def hangman():
    list_of_word=["apple"]
    word=random.choice(list_of_word)
    turn=3
    guessmade=''
    valid_entry=set("abcdefghijklmnopqrstuvwxyz")
    
    while len(word)>0:
        main_word=''
        missed=0
        
        print("guess the word",main_word)
        guess=input()
        
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_"
        if main_word==word:
            print("main word") 
            print("you won !!!") 
            break
        
        print("guess the word",main_word) 
        guess=input()     
                    
        
        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("enter the valid character")
            guess=input()    
            
        if guess not in word:
            turn=turn-1  
            if turn==9:
                print(" 9 turns left !!!")
                print("_ _ _ _ _ _ _")
            if turn==8:
                print(" 8 turns left !!!")
                print("_ _ _ _ _ _ _ _ ")
                print("       o        ")
            if turn==7:
                print(" 7 turns left !!!")
                print("_ _ _ _ _ _ _ _ ")
                print("       o        ")
                print("       |        ")
            if turn==6:
                print(" 6 turns left !!!")
                print("_ _ _ _ _ _ _ _ ")
                print("       o        ")
                print("       |        ")
                print("      /        ")
            if turn==5:
                print(" 5 turns left !!!")
                print("_ _ _ _ _ _ _ _ ")
                print("       o        ")
                print("       |        ")
                print("      / \        ")
            if turn==4:
                print(" 4 turns left !!!")
                print("_ _ _ _ _ _ _ _ ")
                print("      \o        ")
                print("       |        ")
                print("      / \        ")
            if turn==3:
                print(" 3 turns left !!!")
                print("_ _ _ _ _ _ _ _ ")
                print("      \o/        ")
                print("       |        ")
                print("      / \        ")
            if turn==2:
                print(" 2 turns left !!!")
                print("_ _ _ _ _ _ _ _ ")
                print("      \o/  |      ")
                print("       |        ")
                print("      / \        ")   
            if turn==1:
                print(" 1 turns left !!!")
                print("_ _ _ _ _ _ _ _ ")
                print("      \o/_|      ")
                print("       |        ")
                print("      / \        ")           
            if turn==0:
                print("you loose") 
                print("you let a good man die")
                
name=input("enter the name")
print("welcome",name,"!") 
print("try to do guess the word 10 attemps")  
hangman()                   
                        
        
        
        