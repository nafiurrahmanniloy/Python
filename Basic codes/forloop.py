for num in range(1, 11):
    print(num)


marks = {99, 98, 97, 99, 95, 99}  # set ignores multiple values
print(marks)  # no index values, so need to use loop to access the values
for score in marks:  # set is unordered structure
    print(score)
