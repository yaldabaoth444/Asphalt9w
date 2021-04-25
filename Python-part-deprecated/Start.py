import sys
from Bot import Bot
 
if __name__ == "__main__":
	try:
		input("Press Enter to continue...")
		sys.stdout.flush()
		print('Press «Esc» to pause or «Q» to quit')
		
		if len(sys.argv) == 2:
			bot = Bot(sys.argv[1])
		elif len(sys.argv) == 3:
			bot = Bot(sys.argv[1], sys.argv[2])
		else:
			bot = Bot()
		bot.Run()
	except:
		sys.exit(1)
