dividend = input("Enter dividend: ")
divisor = input("Enter divisor: ")

try:
    dividend = int(dividend)
    divisor = int(divisor)
    quotient = dividend / divisor
except ValueError:
    quotient = "Invalid number/s"
except ZeroDivisionError:
    quotient = "Cannot divide by zero"
except Exception:
    quotient = "Unknown"

print(f"Total: {quotient}")