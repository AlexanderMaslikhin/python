def translate(infile, outfile, eng_rus_dict):
    with open(infile, 'r') as in_f:
        with open(outfile, 'w') as out_f:
            for line in in_f:
                eng_number, separator, number = line.split()
                out_f.write(eng_rus_dict[eng_number] + ' ' + separator + ' ' + number + '\n')


def main():
    eng_rus_dict = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре'
    }
    translate('dz4.txt', 'dz4rus.txt', eng_rus_dict)


main()


