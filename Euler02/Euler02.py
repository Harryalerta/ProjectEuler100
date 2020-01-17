CurrentFibonacci  = 1
PreviousFibonacci = 1
TempFibonacci = 0
sum = 0

while CurrentFibonacci <= 4000000:
    if CurrentFibonacci % 2 == 0:
        sum += CurrentFibonacci
    TempFibonacci = CurrentFibonacci
    CurrentFibonacci = CurrentFibonacci + PreviousFibonacci
    PreviousFibonacci = TempFibonacci
