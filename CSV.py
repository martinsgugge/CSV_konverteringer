import csv
import numpy

def ArrayTocsv(header_array,ArrayToWrite,file):

    with open(file, 'w',newline='') as csvFile:

        writer = csv.writer(csvFile, delimiter=';')
        if header_array != None:
            print('skriver overskrift')
            writer.writerow(header_array)
        print('Skriver verdier')
        """for row in ArrayToWrite:
            print(row)
            writer.writerow(row)"""
        writer.writerows(ArrayToWrite)
    csvFile.close()

def plotarrayTocsv(header, data, filename):
    with open(filename, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter=';')
        print('skal skrive')
        for i in range(len(header)):
            header.insert(i*2,'Tid')
        data = zip(*data)
        writer.writerow(header)
        for row in data:
            writer.writerow(row)

def plotTagsTocsv(header, tags, filename):
    with open(filename, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter=';')
        print('skal skrive')
        for i in range(len(header)):
            header.insert(i*2,'Tid')

        writer.writerow(header)
        data = []
        for i in len(tags):
            data.append(tags[i].timestamp)
            data.append(tags[i].measurement)

        writer.writerows(data)

def csvToArray(file, delimiter):
    with open(file, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=delimiter)
        for row in reader:
            x = list(reader)
            result = numpy.array(x)

        csvFile.close()
    return result

def merge_lists(l1, l2, header = None):

    list = []
    for j in range(len(l1)):
        while True:
            try:
                tup = (l1[j], l2[j])
            except IndexError:
                if len(l1)> len(l2):
                    l2.append('')
                    tup = (l1[j], l2[j])
                elif len(l1)<len(l2):
                    l1.append('')
                    tup = (l1[j],l2[j])
                continue
            list.append(tup)

            break
    return list

def find_longest_subarray(array):
    """
    Finds longest array in a matrix
    :param array: Matrix of any data
    :return: integer number of the longest subarray
    """
    max = 0
    for i in range(len(array)):
        if len(array[i]) > max:
            max = len(array[i])
    print(max)
    return max

def transpose_undefined_matrix(matrix):
    """
    Transposes a matrix
    :param matrix: Matrix to be transposed
    :return: Transposed matrix
    """
    max = find_longest_subarray(matrix)
    data = []
    temp = []
    for i in range(max):
        temp.clear()
        for j in range(len(matrix)):

            try:
                temp.append(matrix[j][i])
                # print(tag_u_tid[j][i])
                # print('matriseplass ', j,',',i)
            except IndexError:
                temp.append('')

        data.append(temp.copy())
    return data