import csv
import pandas as pd

with open('Users.csv','r') as users:
    reader=csv.reader(users)
    header = next(users) #On ne veut pas iterer sur la premiere ligne qui correspond au nom des clonens, on le skip donc
    for line in reader:
        print(line[0])