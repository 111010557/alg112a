def truth_table(expression, variables):
    num_variables = len(variables)
    table = []

    # Generate all possible combinations of truth values for variables
    for i in range(2 ** num_variables):
        row = []
        for j in range(num_variables):
            row.append((i // (2 ** j)) % 2)
        table.append(row)

    # Print the truth table without expression and result columns
    header = variables
    rows = []

    for row in table:
        values = row
        rows.append(values)

    # Print the truth table
    print("|".join(header))
    print("-" * (len("|".join(header))))
    for row in rows:
        row_str = "|".join(map(str, row))
        print(row_str)

# Example usage:
expression = "(A and B) or (not C)"
variables = ["A", "B", "C"]
truth_table(expression, variables)