

from datetime import datetime


def happy_new_year():
    current_date = datetime.now()
    assert current_date > datetime(year=2024, month=1, day=1, hour=0, minute=0, second=0), '2024 год еще не наступил'
    

if __name__ == '__main__':
    #print(square_root(-10))
    print(happy_new_year())