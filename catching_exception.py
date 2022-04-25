dividend = input("Enter dividend: ")
divisor = input("Enter divisor: ")

try:
    dividend = int(dividend)
    divisor = int(divisor)
    total = dividend / divisor
except ValueError:
    total = "Invalid number/s"
except ZeroDivisionError:
    total = "Cannot divide by zero"
except Exception:
    total = "Unknown"

print(f"Total: {total}")