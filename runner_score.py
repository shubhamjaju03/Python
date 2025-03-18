if __name__ == '__main__':
   
    n = 5 
    arr = [2, 3, 6, 6, 5]

    unique_sorted_arr = sorted(set(arr))

    if len(unique_sorted_arr) > 1:
        print(unique_sorted_arr[-2])
    else:
        print("No second largest number")
