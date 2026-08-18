email_text= input("enter the email text:\n")

symbols=['@','.','!']

print("\nSpecial Symbol Count:")
for symbol in symbols:
    count=email_text.count(symbol)
    print(f"{symbol}:{count}")
