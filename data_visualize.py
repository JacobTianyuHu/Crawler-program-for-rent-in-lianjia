#coding:utf-8
import pandas as pd
import matplotlib.pyplot as plt

def data_visualize():
    with open('链家北京租房.txt') as f:
        df = pd.read_csv(f, sep=',', header=None, encoding='utf-8', names=['area', 'title', 'room_type', 'square', 'position'
            , 'detail_place', 'floor', 'total_floor', 'price', 'house_year'])
        print(df.describe())
        detail_place = df.groupby(['detail_place'])
        house_com = detail_place['price'].agg(['mean', 'count'])
        house_com.reset_index(inplace=True)
        detail_place_main = house_com.sort_values('count', ascending=False)[0:20]
        attr = detail_place_main['detail_place']
        v1 = detail_place_main['count']
        v2 = detail_place_main['mean']
        plt.bar(attr, v2)
        plt.show()

        #
        # line = Line("北京主要路段房租均价")
        # line.add("路段", attr, v2, is_stack=True, xaxis_rotate=30, yaxix_min=4.2,
        #          mark_point=['min', 'max'], xaxis_interval=0, line_color='lightblue',
        #          line_width=4, mark_point_textcolor='black', mark_point_color='lightblue',
        #          is_splitline_show=False)
        # bar = Bar("北京主要路段房屋数量")
        # bar.add("路段", attr, v1, is_stack=True, xaxis_rotate=30, yaxix_min=4.2,
        #         xaxis_interval=0, is_splitline_show=False)
        # overlap = Overlap()
        # overlap.add(bar)
        # overlap.add(line, yaxis_index=1, is_add_yaxis=True)
        # overlap.render('北京路段_房屋均价分布图.html')

def main():
    print('start to visualize the datas!')
    data_visualize()

if __name__ == '__main__':
    main()