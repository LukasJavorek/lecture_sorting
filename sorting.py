import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as csv_file:
        content = csv.DictReader(csv_file)
        data = {}
        for row in content:
            for key in row.keys():
                if key not in data:
                    data[key] = [int(row[key])]
                else:
                    data[key].append(int(row[key]))

        print(data)
    return data


def selection_sort(number_list, direction=0):
    idx0 = 0
    for n in range(len(number_list)):
        smallest = number_list[idx0]
        idx = idx0
        for number in number_list[idx0:]:
            if smallest >= number and direction == 0:
                smallest = number
                idx_smallest = idx
            if smallest <= number and direction == 1:
                smallest = number
                idx_smallest = idx
            idx = idx + 1
        number_list[idx0], number_list[idx_smallest] = number_list[idx_smallest], number_list[idx0]
        idx0 = idx0 + 1

    return number_list


def main():
    direction = 0
    data = read_data("numbers.csv")
    for value in data.values():
        value = selection_sort(value, direction)
    print(data)

if __name__ == '__main__':
    main()
