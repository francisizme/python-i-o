#!/usr/bin/env python3

def read_file(path):
    with open(path) as file:
        for line in file:
            print(line.strip())


def append_file(data):
    print('Processing Appending file')
    with open('append.txt', 'a') as file:
        file.write(data)
    read_file('append.txt')


def write_file(data):
    print('Processing writing file')
    with open('write.txt', 'w') as file:
        file.write(data)
    read_file('write.txt')


def read_write(data):
    print('Processing read and write file')
    with open('i-o.txt', 'r+') as file:
        file.write(data)
        for line in file:
            print(line.strip())


append_file('Appending...')
write_file('writing....')
read_write('Read and write')
