#Complete the funtion to compute how many seconds passed between the two timestamp.
def two_timestamp(hr1,min1,sec1,hr2,min2,sec2):
    fisrt_hour = hr1 * 3600
    first_min = min1 * 60
    final_first = fisrt_hour + first_min + sec1
    second_hour = hr2 * 3600
    second_min = min2 * 60
    final_second = second_hour + second_min + sec2
    
    return final_second - final_first


#Invoke the fuction and pass two timestamps(6 intergers) as its argument.
print(two_timestamp(1,1,1,2,2,2))