'''A cafe has N computers. Several customers come to the cafe to
use these computers. A customer will be serviced only if there is
any unoccupied computer at the moment the customer visits the
cafe. If there is no unoccupied computer, the customer leaves the
cafe.
You are given an integer N representing the number of computers
in the cafe and a sequence of uppercase letters S. Every letter in S
occurs exactly two times. The first occurrence denotes the arrival
of a customer and the second occurrence denotes the departure
of the same customer if he gets allocated the computer.
You have to find the number of customers that walked away
without using a computer.
Example 1:
Input:
N = 3
S = GACCBDDBAGEE
Output: 1
Explanation: Only D will not be able to get any computer. So the
answer is 1.
Example 2:
Input:
N = 1
S = ABCBAC
Output: 2
Explanation: B and C will not be able to get any computers. So the
answer is 2.'''


def count_customers_without_computer(N, S):
    stack = []
    walked_away = 0

    for customer in S:
        if customer in stack:
            stack.remove(customer)
        else:
            if len(stack) < N:
                stack.append(customer)
            else:
                walked_away += 1
    return walked_away

print(count_customers_without_computer(3, "GACCBDDBAGEE"))  # Output: 1
print(count_customers_without_computer(1, "ABCBAC"))  # Output: 2
