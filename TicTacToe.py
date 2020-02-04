# global variables
import random
''' Important Base variables '''
# All 8 (Rows 3,Columns 3,Diagonals 2)
win = ['012','345','678','036','147','258','048','246'] 

# Stores current status of Board
li = [[' ',' ',' ' ],[' ',' ',' '],[' ',' ',' ']] 

# game string work same as 'li'
games = ''

# For keeping tracks of players chance
cnt = 0

#Stores ID of current Player 
ch = ''

#for knowing that game is ended Becomes True when someone wins or board fills 
token  = False

''' For optional features '''

# Stores name of Players
name = ['1','2']

# for force ending game
exit = False

''' For Single player game '''

# stores Game Mode single-player or multi-player
mode  = 1

# Forces Commonsense() to decide next move 
emer = False

# Stores count of filled blocks in every element of 'win' 
c  = [0,0,0,0,0,0,0,0]

# Used to store next move 
move = ()
def commonSense(l,games):
	'''
	Decides next move for Computer
	'''
	global emer
	line = []
	i = 0
	# line contains row or column in which X is about to win
	line.append(chkWin(games,'X1',1,l))
	line.append(chkWin(games,'O2',1,l))
	if line[1] != None:
		i = 1 
	if emer or i==1:
		#print("common sense",line[i],173)
		index = 0
		for c in list(line[i]) :
			if games[int(c)] == ' ':
				index = int(c)
		y = index%3
		x = index//3
		emer = False
		return (x,y)
	else:
		z = randomMove()
		return z

def writeOn(x,y):
	'''
	Writes on input coordinate
	'''
	global li
	# writes data in list
	if li[x][y] == ' ' :
		li[x][y] = 'O'	
	else:
		print('\nBlock is already filled')
def regWrite(m):
	''' 
		Write Info about filled blocks 
		returns list of lines which were 
		changed in last round 
		**value of l given in O's chance
		and it extended in X's chance 
		because commonsense is called in X's chance
	'''
	global win
	global c
	global pos
	global move
	l = set()
	for i in c:
		if i == 3:
			c[c.index(i)] = -1
	if 	m == 2:
		x = 3 * (int(pos[0])-1) +  int(pos[-1])-1
	else:
		x = 3 * move[0] + move[1] 
	for i in win:
		if str(x) in i and c[win.index(i)]!=-1:
			c[win.index(i)] += 1  
			if c[win.index(i)]>1:
				l.add(i)
			
	return l
def randomMove():
	#print("random move",226)
	global li
	set = []
	
	for i in range(len(li)) :
		for j in range(len(li[i])):
			if	li[i][j] == ' ':
				set.append(i*3+j)		
	index = random.sample(set,1)[0]
	x = index//3
	y = index % 3
	return (x,y,1)
# takes player tag(O/X) and current board status(list) as input
def drawBoard(ch,li):                                  
	st = ''
	grid = [[' ---',' ---',' ---'],
			['|','   ','|','   ','|','   ','|'],
			[' ---',' ---',' ---'],
			['|','   ','|','   ','|','   ','|'],
			[' ---',' ---',' ---'],
			['|','   ','|','   ','|','   ','|'],
			[' ---',' ---',' ---']] 
	print('')
	for i in range(len(li)):
		for j in range(len(li[i])):
			grid[2*i+1][2*j+1] = ' ' + li[i][j] + ' ' 
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			st += grid[i][j] 
		st+='\n'	
	# return board string
	return st                                        
#tic tac toe
def chkWin(games,ch,m,l):         
	global token
	global emer
	for i in l :
		wincnt = 0
		ecnt = 0
		for j in range(3) :
			if games[int(i[j])] == ch[0] :
				wincnt+=1
				if wincnt == 3 and m == 2 :
					print( 'Player' ,name[int(ch[1])-1], 'is winner')
					token = True 
					break
			elif games[int(i[j])] == ' ' :
				ecnt+=1
		#print(ecnt,wincnt,m,i)
		if ecnt == 1 and wincnt == 2 and m == 1:
			if ch[0] == 'X'	:
				emer = True
			return i
		
		if token:
			break
def command(pos):
	global exit
	global name
	global mode
	if pos == 'exit':
		ch = input('Are you sure(y/n):')
		if ch == 'y':
			exit = True
			return True
		else:
			return False
	if pos[:-1] == 'name':
		chngName(name[int(pos[-1])-1],int(pos[-1])-1)
		return False
	if pos == 'restart':
		ch = input('Are you sure(y/n):')
		if ch == 'y':
			restart()
			return True
		else:
			return False
	if pos =='mode':
		mode = int(input('\n\tEnter the Mode (1/2)'))
		restart()
		print(exit)
		return True
#def undo():

def chngName(c,p):
	global name
	name[p] = input("Enter name for Player %s " % c)
def restart():
	global games
	games  = ''
	global li
	li =  [[' ',' ',' ' ],[' ',' ',' '],[' ',' ', ' ']] 
	global cnt
	cnt = 0
	global exit
	exit = True
	global pos
	pos = ''
	global c
	c = [0,0,0,0,0,0,0,0]
	print('Restarted')
def uInput(ch):
	global pos
	global cnt
	global exit 
	global games
	tmp = cnt
	p = int(ch[1])-1
	while tmp == cnt :
		pos = input('\nPlayer %s\'s (%s) chance enter coordinates "x,y" '%(name[p],ch[0]))
		# makes user input operable
		pos = pos.strip()
		if pos == 'name':
			pos+=ch[1]
			command(pos)
			continue
		if command(pos):
			break
		if pos == 'exit' or pos == 'restart' :
			continue
		if mode == 2 or ch[0] == 'X':
			if  pos != '' and pos[0] in ['1','2','3'] and pos[-1] in ['1','2','3'] :
				x = int(pos[0])-1
				y = int(pos[-1])-1
				# writes input from user in list
				if li[x][y] == ' ' :
					li[x][y] = ch[0]
					cnt+=1
				else:
					print('\nBlock is already filled ')
			else:
				print('\n\tPlease Give a valid Input ')	
				
	
def main():
	global games
	global li 
	global cnt
	global token
	global pos
	global mode 
	global ch
	global exit
	global c
	global move
	
	print('Instructions:-\n 1.you can type your move these format x,y\n 2.for changing into 2P mode type "mode" command\n 3.for changing name type "name" command\n 4.for Exit or Restart type respective commands "exit" and "restart"')
	while not token and cnt < 9 :

		#stores game state in string format
		games = ''
		if cnt == 0:
			print(drawBoard(' ',li),'\n','Input Format "x,y"')
		# Decides which players chance 
		if cnt%2 == 0 :
			ch = 'X1'
			uInput(ch)
			if not exit:
				if cnt>1:
					l.extend(regWrite(2)) 
				else:
					l = list(regWrite(2))
		else :
			ch = 'O2'
			if	mode == 2:
				uInput(ch)
				if not exit:
					if cnt>1:
						l = list(regWrite(2))
					else:
						l = list(regWrite(2))
					
			else:
				print('Computer writes at (%d,%d)'%(move[0],move[1]))
				if len(move) == 2: 
					writeOn(move[0],move[1])
					l = list(regWrite(1))
				
				else:
					writeOn(move[0],move[1])
					l = list(regWrite(1))
				cnt+=1
				
		if exit == True :
			if pos == '':
				exit = False
				continue
			else :	
				return
	
		# writes data from user to string 
		for i in range(3):
				for j in range(3):
					games += li[i][j]
		# Computer on work
		if ch[0] == 'X' and mode == 1 and cnt < 8 :
			move = commonSense(l,games);
			
		#Draws Board creates new string each time called
		print(drawBoard(ch[0],li))
		#checks Win
		for i in c:
			if i == 3:
				if not token:
					chkWin(games,ch,2,l)
		
		if not token and cnt == 9:
			print('Draw')
while True:
	main()
	ch = input('Wanna Play again(y/n):')
	if ch != 'y':
		break
	