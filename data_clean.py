import pandas as pd

def data_clean():
    with open('链家北京租房.txt') as f:
        df = pd.read_csv(f, sep=',', header=None, encoding='utf-8', names=['area', 'title', 'room_type', 'square', 'position'
            , 'detail_place', 'floor', 'total_floor', 'price', 'house_year'])
        print(df.describe())

def main():
    print('start to clean the datas!')
    data_clean()

if __name__ == '__main__':
    main()