import argparse


parser = argparse.ArgumentParser(
    description="Simple Command-Line Calculator"
)


parser.add_argument("operation", type=str, choices=["add", "sub", "mul", "div"],
                    help="Operation to perform: add, sub, mul, div")
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")


args = parser.parse_args()


if args.operation == "add":
    result = args.num1 + args.num2
elif args.operation == "sub":
    result = args.num1 - args.num2
elif args.operation == "mul":
    result = args.num1 * args.num2
elif args.operation == "div":
    if args.num2 == 0:
        result = "Error: Division by zero!"
    else:
        result = args.num1 / args.num2

print(f"Result: {result}")
