import datetime

def time_delta(t1, t2):
    # months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # len_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # temp1 = t1.split()
    # temp2 = t2.split()
    
    # time1 = [ int(x) for x in temp1[-2].split(':') ]
    # time2 = [ int(x) for x in temp2[-2].split(':') ]

    # date1 = temp1[1:4]
    # date2 = temp2[1:4]

    # date1[1] = months.index(date1[1]) + 1
    # date2[1] = months.index(date2[1]) + 1

    # date1 = date1 + time1
    # date2 = date2 + time2

    # diff1 = int(temp1[-1])
    # diff2 = int(temp2[-1])

    # date1[-3] -= diff1 // 100
    # date2[-3] -= diff2 // 100

    # date1[-2] -= diff1 % 100
    # date2[-2] -= diff2 % 100

    # date1 = list(map(int, date1))
    # date2 = list(map(int, date2))
    
    # print(date1)
    # print(date2)
    
    # date1 = date1[0] * 24 * 3600 \
    #     + date1[1] * len_months[date1[1]-1] * 24 * 3600 \
    #     + date1[2] * 365 * 24 * 3600 \
    #     + date1[3] * 3600 \
    #     + date1[4] * 60 + date1[5]
    
    # date2 = date2[0] * 24 * 3600 \
    #     + date2[1] * len_months[date2[1]-1] * 24 * 3600 \
    #     + date2[2] * 365 * 24 * 3600 \
    #     + date2[3] * 3600 \
    #     + date2[4] * 60 + date2[5]
    
    # print(date1)
    # print(date2)

    # return abs(date2 - date1)

    dt1 = datetime.datetime.strptime(t1.rstrip(), '%a %d %b %Y %H:%M:%S %z')
    dt2 = datetime.datetime.strptime(t2.rstrip(), '%a %d %b %Y %H:%M:%S %z')
    return abs(int(((dt2-dt1).total_seconds())))


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)
