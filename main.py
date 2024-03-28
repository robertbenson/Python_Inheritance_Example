from Stack import SumStack


def main():
    sum_stack = SumStack()
    # print(help(adding_stack))

    for i in range(5):
        try:
            sum_stack.push(i)
            print(f"push: {i}{sum_stack.__dict__}")
        except TypeError:
            print(f"TypeError: value is not int or float: {i}")

    print(f"Total: {sum_stack.get_sum()}")

    for i in range(5):
        print(f"pop: {sum_stack.pop()}{sum_stack.__dict__}")


if __name__ == '__main__':
    main()
