def Average_waiting_time(customer):
    avg=0
    time=customer[0][0]
    print(time)
    for i in customer:
        arrival=i[0]
        time_taken=i[1]
        if arrival>time:
            time+=arrival-time
        time+=time_taken
        avg+=(time-arrival)
        print(arrival,time_taken,time)
    avg=avg/len(customer)
    print(avg)
Average_waiting_time([[5,2],[5,4],[10,3],[20,1]])