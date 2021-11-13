
import time
import curses #does the styling of terminal or writting any thing
from curses import wrapper#Wrapper initialize the curses module --> takeover to cmd screen do the operation and return back
import random


def start_screen(stdscr):
	stdscr.clear()#Clear the entire screen
	stdscr.addstr("Welcome to TypingSpeed Test!! Level up your speed..")#prints the text in the terminalon| color_pair selects the color| and at the begining 2---> line no.,8-->characters 
	stdscr.addstr("\nPress any key to begin",curses.color_pair(2))#overrides
	stdscr.refresh()#on adding anything say a text, gotta refresh the screen to actually show
	stdscr.getkey()#acts like the getch() in c

def display_text_over(stdscr,target,current,wpm=0):
	stdscr.addstr(target)#prints the text in the terminalon| color_pair selects the color| and at the begining 2---> line no.,8-->characters 
	stdscr.addstr(1,0,f"WPM={wpm}")
	for i,char in enumerate(current):
		if target[i]==char:
			stdscr.addstr(0,i,char,curses.color_pair(1))
		else:
			stdscr.addstr(0,i,char,curses.color_pair(3))


def load_txt():
	with open("text.txt","r") as f:
		lines=f.readlines()
		return random.choice(lines).strip()


def test_start(stdscr):
	text=load_txt()
	current=[]
	wpm=0
	start_time=time.time()
	stdscr.nodelay(True)#the program dont freze while taking input sp that the time keps counting
	while True:
		time_elapsed=max(time.time()-start_time,1)
		wpm=round((len(current)/(time_elapsed/60))/5)
		stdscr.clear()#Clear the entire screen
		display_text_over(stdscr,text,current,wpm)
		stdscr.refresh()#on adding anything say a text, gotta refresh the screen to actually show
		
		if "".join(current)==text:
			stdscr.nodelay(False)
			break

		try:
			key=stdscr.getkey()
		except:
			continue
		

		if ord(key)==27:
			break

		if key in ("KEY_BACKSPACE",'\b',"\x7f"):
			if len(current) > 0:
				current.pop()
		elif len(current)<len(text):
			current.append(key)

		
def main(stdscr):#stdscr---> Standard Screen( The cmd prompt screen )
	curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)#pair the foreground and the background color. The no. 1 represnets the color pair
	curses.init_pair(2,curses.COLOR_BLUE,curses.COLOR_BLACK)
	curses.init_pair(3,curses.COLOR_RED,curses.COLOR_BLACK)
	
	start_screen(stdscr)
	
	while True:
		test_start(stdscr)

		stdscr.addstr(2,0,"You completed the test.\nThank you so much for playing.\nPress any key to continue....")
		key=stdscr.getkey()
		if ord(key)==27:
			break
wrapper(main)#calling the main function using the wrapper function(to execute the main funtion in terminal)

#you gotta run the code in terminal or cmd