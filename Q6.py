def f():
    a=str(input('Input by player1(rock or paper or scissors):'))
    b=str(input('Input by player2(rock or paper or scissors):'))
    if (a=='rock' and b=='scissors')or(a=='scissors' and b=='paper')or(a=='paper' and b=='rock'):
        print('Congratulations Player 1 wins')
    elif (b=='rock' and a=='scissors')or(b=='scissors' and a=='paper')or(b=='paper' and a=='rock'):
        print('Congratulations Player 2 wins')
    else:
        print('Its a tie')
check=0
while check==0:
    f()        
    N=str(input('Do you want to play again?(y/n):'))
    if N=='y':
        check=0
    else:
        print('Thanks for playing')
        check=5
            

        
