# def stall():
#     yield "01. Masala Chai"
#     yield "02. Coffee"
#     yield "03. Green Tea"
#     yield "04. Milk Shake"

# tea = stall()

# print(next(tea))
# print(next(tea))
# print(next(tea))
# print(next(tea))

# #Infine Generator
# def infinite_chai():
#   count =1
#   while True:
#     yield f"Refill #{count}"
#     count+=1
# stall = infinite_chai()

# for _ in range(10):
#     print(next(stall))


# Send Method
def chai():
    print("What flavour you want?")
    while True:
        order = yield
        print(f"You order {order}")
stall = chai()
next(stall)
stall.send("Green Tea")
    