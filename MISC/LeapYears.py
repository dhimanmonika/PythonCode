if __name__=="__main__":
    print("Enter the staring year")
    st_year=int(input())
    print("Leap years :")
    for i in range(21):
        if st_year%400==0 or st_year%4==0 and st_year%100!=0:
            print(st_year)
        st_year=st_year+1

