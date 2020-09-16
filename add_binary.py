def binary_sum(bin1, bin2):
    if len(bin2) > len(bin1) : bin1, bin2 = bin2, bin1
    sum = ""
    remainder = 0
    
    for i in range(len(bin1) - len(bin2)):
        bin2 = "0" + bin2
    
    for i in range(len(bin1) - 1, -1, -1):
        temp_sum = int(bin1[i]) + int(bin2[i])
        
        if remainder > 0:
            temp_sum += remainder
            remainder = 0
        
        if temp_sum > 1:
            sum = "0" + sum
            remainder = 1
        else:
            sum = str(temp_sum) + sum
            
        if i == 0 and remainder > 0:
            sum = str(remainder) + sum
    
    return sum


if __name__ == "__main__":
    print binary_sum("100", "1") # 101
    print binary_sum("11", "1") # 100
    print binary_sum("1", "0") # 1
    print binary_sum("101101", "11001") # 1000110 
    print binary_sum("1001", "110110") # 111111

