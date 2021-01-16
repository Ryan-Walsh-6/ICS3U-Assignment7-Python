#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: January 2021
# this program concatenates two lists


def concatenating_the_list(list_input, list_input_2):
    # concatenating two lists

    mergedlist = []
    mergedlist = list_input
    for counter in list_input_2:
        mergedlist.append(counter)

    return mergedlist


def main():
    # this program concatenates two lists

    list_input = []
    list_input_2 = []
    element_from_user = None

    # input
    print("Please enter 1 element at a time. Enter STOP at the end.")
    print("\n", end="")
    print("Enter the elements for your first list.")
    element_from_user = input("Enter an element:")
    list_input.append(element_from_user)
    while element_from_user.upper() != "STOP":
        element_from_user = input("Enter an element:")
        list_input.append(element_from_user)

    list_input.pop()
    print("\n", end="")

    print("Enter the elements for your second list.")
    element_from_user = input("Enter an element:")
    list_input_2.append(element_from_user)
    while element_from_user.upper() != "STOP":
        element_from_user = input("Enter an element:")
        list_input_2.append(element_from_user)

    list_input_2.pop()
    print("\n", end="")

    concatenated_list = concatenating_the_list(list_input, list_input_2)

    print("The concatenated list is:")
    print("\n", end="")
    fmt = "[%s"
    for counter in concatenated_list:
        print(fmt % counter, end="")
        fmt = ", %s"
    print("]")
    print("\n", end="")


if __name__ == "__main__":
    main()
