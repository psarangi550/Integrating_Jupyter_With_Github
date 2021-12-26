import argparse

parser=argparse.ArgumentParser(description="This is a Command Line Argument to Perform Operation between the values")

parser.add_argument("num1",help="Provide the First Number", type=int)

parser.add_argument("num2",help="Provide the Second Number", type=int)

parser.add_argument("operation", help="Provide the Operation")

args=parser.parse_args()

print(type(args))

result=None

if args.operation=="+":
    result=args.num1+args.num2
    

print(result)