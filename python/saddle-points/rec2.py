def sum_recursive(current_number, accumulated_sum):
    # Base case
    # Return the final state
    if current_number == 20:
        return accumulated_sum

    # Recursive case
    # Thread the state through the recursive call
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)

print(sum_recursive(1,0))