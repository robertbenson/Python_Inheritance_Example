from Stack import SumStack


def main():
    sum_stack = SumStack()
    # print(help(adding_stack))

    for i in range(5):
        sum_stack.push(i)
        print(f"push: {i}{sum_stack.__dict__}")

    print(f"Total: {sum_stack.get_sum()}")

    for i in range(5):
        print(f"pop: {sum_stack.pop()}{sum_stack.__dict__}")


if __name__ == '__main__':
    main()
