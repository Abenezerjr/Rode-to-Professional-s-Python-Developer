print('Wellcome to the tip Calculator.')

totalBill = float(input("what was the total bill? $"))
# print(totalBill)
tipPercentage = int(input(f"What percentage tip would you like to give? 10,12 or 15? "))
# print(tipPercentage)
splitBill = int(input("how many people to split the bill? "))
# print(splitBill)

percentage = tipPercentage / 100 # change the tipPercentage to percentage
totalTip = totalBill * percentage # find the totalbBill of the percentage
totalBillWithTip = totalBill + totalTip # add total Bill and tip to find the totalBillwith tip
totalEachTip = round(totalBillWithTip / splitBill,2) # divide the totalBill with spiltBill to each person and round in 2 decimal place

print(f"Each person should pay:${totalEachTip}") # final result store
