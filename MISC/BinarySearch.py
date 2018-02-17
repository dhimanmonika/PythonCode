

def BSearch(numbers,number):
    start=1
    end=len(numbers)
    print(len(numbers))
    while True:
        mid = int((end - start )    / 2)
        print("mid number",numbers[mid],mid)
        if mid<start or mid>end or mid <0 :
            return False
        if numbers[mid] == number:
            print("found number ", number, "at position ", mid + 1)
            return True
        elif number > numbers[mid]:
            start=mid
        elif number < numbers[mid]:
            end=mid


numbers=[2,3,6,13,45]
print("list of numbers :",numbers)
if not BSearch(numbers,13):
    print("number not found in the list")
