# Formula:
# CI = P × (1 + R/100)^T − P



principle = float(input("Enter the principle:"))
rate  = float(input("Enter the rate:"))
time = float(input("Enter the time:"))

compound = principle * rate

print("compound =",compound)