import pandas as pd
import sys

# file to check if pandas can be imported within the docker file

def process_data(day=sys.argv[1]):
    print(f'job finished successfully for day={day}')
    return None

if __name__=='__main__':
    process_data()
