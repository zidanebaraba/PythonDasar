import _thread
import time

def CounterDown(ThreadName):
    count=10
    while(count>=0):
        print("{}, count: {}".format(ThreadName,count))
        count-=1
        time.sleep(1)
        
def main():
    try:
        _thread.start_new_thread(CounterDown,("Thread1",))
        _thread.start_new_thread(CounterDown,("Thread2",))
        print("Thread is running")
    except:
        print("error: Unable to start thread")
    while 1:
        pass
    
if __name__ == "__main__":
    main()