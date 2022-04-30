from ctypes import sizeof
from datetime import datetime


def main():
    start_time = datetime.now() 
    for i in range(10000):
        print(i)
    end_time = datetime.now()
    execution_time  = end_time-start_time
    print(execution_time.total_seconds())
    print()

if __name__ == "__main__":
    main()