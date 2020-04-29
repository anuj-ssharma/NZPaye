next_num_in_seq = [0, 1]

end_number = int(input("Enter the number to generate the sequence until: "))
for num in range(0, end_number):
    next_num = next_num_in_seq[-1] + next_num_in_seq[-2]
    if next_num <= end_number:
        next_num_in_seq.append(next_num)

print(next_num_in_seq)