import sys
from Bot import Bot
 
if __name__ == "__main__":
    try:
        input("Press Enter to continue...")
        bot = Bot()
        if len(sys.argv) > 1:
            bot.Run(sys.argv[1])
        else:    
            bot.Run('NETWORK')
    except:
        sys.exit(1)
        
    
     