import time

left = '\U0001F448'
right = '\U0001F449'
up = '\U0001F446'
down = '\U0001F447'
middle = '\U0001F595'

mango = '\U0001F96D'

win = '\U0001F44D'
lose = '\U0001F44E'

person = '\U0001F606'
person = '\U0001F914'
person = '\U0001F385'

pensive = '\U0001F614'

unamused = '\U0001F612'

grimace = '\U0001F62C'

relieved = '\U0001F60C'

nausea = '\U0001F922'

bandage = '\U0001F915'

upside = '\U0001F643'

skull = '\U0001F480'

size = (5, 5)

cur = [0, 0]

states = ['b', 'p', 's', 'w', 'g']

world = [[0, 0, 's', 'w', 'sb'],
         ['b', 0, 0, 'sb', 'p'],
         ['p', 'b', 0, 0, 'b'],
         ['b', 'sp', 'b', 'g', 'b'],
         ['s', 'w', 's', 'b', 'p']]

visited = list()

def display_world():
    global visited
    for i in range(size[0]):
        for j in range(size[1]):
            if [i, j] in visited:
                if [i, j] == cur:
                    if world[i][j] == 0:
                        print(f"\033[1;32;40m{person}\033[0m", end = " | ") 
                    else:
                        print("\033[1;32;40m" + person + " " + " ".join(world[i][j].upper()) + "\033[0m", end = " | ")
                else:
                    if world[i][j] == 0:
                        print('-', end = " | ") 
                    else:
                        print(world[i][j].upper(), end = " | ")
            else:
                print('X', end = ' | ')
        print('\n_____________________')

def wumpus_world():
    global visited
    while True:
        visited.append(cur.copy())
        print(f'Current location:  {cur} \n')
        display_world()
        square = str(world[cur[0]][cur[1]])
        if 'g' in square:
            print(f'\nGold reached!!! {mango}\n\n')
            return True
        if 'p' in square:
            print(f'\nPit encountered!!! {bandage}\n\n')
            return False
        if 'w' in square:
            print(f'\nWumpus detected!!! {skull}\n\n')
            return False
        if 'b' in square:
            print(f'\nBreeze detected! {grimace}\n\n')
        if 's' in square:
            print(f'\nStench detected! {nausea}\n\n')
        if len(set(states).intersection(set(square))) == 0:
            print(f'\nNothing detected! {relieved}\n\n') 
            
        while True:
            print(f'w: Move up   s: Move down   a: Move left   d: Move right')
            choice = input('Enter choice: ').lower().strip()
            if choice not in ['w', 'a', 's', 'd']:
                print('\nInvalid input, Are u blind?\n')
            elif cur[0] == 0 and choice == 'w':
                print('Invalid choice, Cannot move up!') 
            elif cur[0] == size[0] - 1 and choice == 's':
                print('Invalid choice, Cannot move down!') 
            elif cur[1] == 0 and choice == 'a':
                print('Invalid choice, Cannot move left!')
            elif cur[1] == size[1] - 1 and choice == 'd':
                print(f'Invalid choice, Cannot move right!') 
            else:
                if choice == 'w':
                    print(f'Moving up... {up}')
                    cur[0] -= 1
                elif choice == 'a':
                    print(f'Moving left... {left}')
                    cur[1] -= 1
                elif choice == 's':
                    print(f'Moving down... {down}')
                    cur[0] += 1
                elif choice == 'd':
                    print(f'Moving right... {right}\n')
                    cur[1] += 1
                break
                

def main():
    result = wumpus_world()
    
    if result:
        print(f'\n\nYOU WIN, KAMI SAMA!!! {win}\n\n')
    else:
        print(f'\n\nYOU LOSE, U BOZO!!! {lose}\n\n')
        
    time.sleep(5)
    
    print(f'Still Here???')
    
    time.sleep(3)
    
    print(f'Here you go, {middle}')
    
if __name__ == "__main__":
    main()