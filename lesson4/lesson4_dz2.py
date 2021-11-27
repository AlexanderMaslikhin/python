def main():
    source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    new_list = [element for i, element in enumerate(source_list) if i != 0 and source_list[i] > source_list[i-1]]
    print(new_list)


main()
