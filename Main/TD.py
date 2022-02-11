import ast
import matplotlib.pyplot as plt

# ask for stock name and get the stock information
stock_name = input("Enter the stock code:").upper()
file = open(f"/data/{stock_name}.txt", 'r')
a = file.read()
stock_info = ast.literal_eval(a)
file.close()

# get close, open, high, and low price
close_price = []
open_price = []
day_high = []
day_low = []
time_stamp = []
for i in stock_info:
    close_price.append(i[4])
    open_price.append(i[1])
    day_high.append(i[2])
    day_low.append(i[3])
    time_stamp.append(i[0])

'''To find TD'''
"""
Finalized!!!!!!!!
"""
time_index = 0
i = 0
m = 7  # time_index+5+7 day 8th
fanzhuan = []  # perfect TD
ifanzhuan = []  # normal TD
while True:
    try:
        if close_price[time_index] < close_price[time_index + 4] and close_price[time_index + 1] > close_price[
            time_index + 5]:
            while close_price[time_index + 1 + i] > close_price[time_index + 5 + i]:
                i += 1
                if i == 9:  # TD id formed for day 9: i = 8
                    low_point = [close_price[time_index + 5 + 6], close_price[time_index + 5 + 5],
                                 open_price[time_index + 5 + 6], open_price[time_index + 5 + 5]]
                    try:
                        while min(low_point) < min(close_price[time_index + 5 + m],
                                                   open_price[time_index + 5 + m]):  # to find TD perfect
                            m = m + 1
                            if m == 14:  # fail to find TD perfect
                                break
                        if m < 14:
                            index = time_index + 5 + m  # perfect TD is formed
                            fanzhuan.append(index)
                            break

                        else:
                            index = time_index + 5 + 8  # normal TD is formed
                            ifanzhuan.append(index)
                            m = 0
                            break

                    except:
                        print('TD id formed，rest of data is not enough to find TD perfect')
                        time_index = len(close_price)
                        break

            time_index = time_index + i  # update time——index
            i = 0  # reset i value
            m = 7  # reset m value


        else:
            time_index += 1

    except:
        print('search accomplished, rest of the data is not enough to keep searching')
        break

'''----Finalized!!!!-----'''
time_index = 0
i = 0
m = 9
fanzhuan_mai = []
while True:
    try:
        if close_price[time_index] < close_price[time_index + 4] and close_price[time_index + 1] > close_price[
            time_index + 5]:
            while close_price[time_index + 1 + i] > close_price[time_index + 5 + i]:
                i += 1
                if i == 9:  # TD formed
                    try:
                        while close_price[time_index + 11] < close_price[time_index + 3 + m]:
                            m = m + 1  # index+11 day7 < day8
                            if m == 16:
                                break

                        if m < 16:
                            index = time_index + 5 + m  # adjustable parameter
                            fanzhuan_mai.append(index)
                            m = 9  # 重置
                            break

                        else:  # fail to find TD perfect
                            index = time_index + 12
                            fanzhuan_mai.append(index)
                            m = 9  # 重置
                            break

                    except:
                        print('this is not working')

            time_index = time_index + i
            i = 0

        else:
            time_index += 1

    except:
        print('this is not working')
        break

'''graph'''
for i in fanzhuan:  # perfect
    plt.plot(i, close_price[i], 'ro')
for i in fanzhuan_mai:
    plt.plot(i, close_price[i], 'b^')
for i in ifanzhuan:
    plt.plot(i, close_price[i], 'ks')

plt.plot(range(len(close_price)), close_price)
plt.show()

# 我觉得对于这个我基本满意了，我现在对于这个的设想就是为我寻找买卖点，两个指标不同编程前后相继出现，我以后出现的的指标为准，如果下一日的收盘价高于
# 指标所在的价格，买入。如果低于指标所在的价格，等待价格回到指标所在的价格买入
# 两个指标基本上现在一样了。。。。但是还是有一点点前后的参考意义的
