import sys
import pandas as pd

name = list()
number = list()

try:
    with open('phonebook.txt') as f:
        for line in f:
            contents = line.split(',')
            name.append(contents[0])
            number.append(contents[1].replace('\n',''))
        xy = {'Name':name,
               'Number':number
        }
        df = pd.DataFrame(xy)
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])

# 2. (가) 의 Solution
def number_search(name):
    for i, v in zip(df["Name"].index, df["Name"]):
        if (v == name):
            print(df["Number"][i])

# 2. (나) 의 Solution
def region_book(num):
    for i, v in zip(df["Number"].index, df["Number"]):
        if (v.split('-')[0] == num):
            print(df["Name"][i], df["Number"][i])

