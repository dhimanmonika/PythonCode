


def Game(*args):
    if 'scissor' and 'rock' in args:
        print("player",args.index('rock')+1," wins")
    elif 'scissor' and 'paper' in args:
        print("player",args.index('scissor')+1," wins")
    elif 'paper' and 'rock' in args:
        print("player",args.index('paper')+1," wins")






if __name__ =='__main__':
    flag=True
    while(flag):
        ch1 = input('Player 1: ')
        ch2 = input('Player 2: ')

        Game(ch1,ch2)
        ch=input("do you want to play more ?? y/n")
        if ch=='n':
            flag=False











