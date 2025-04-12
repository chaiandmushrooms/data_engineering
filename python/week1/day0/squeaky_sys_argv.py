import sys
import csv

if len(sys.argv) != 3:
    print("usage: play.py inputfile outfile")
    exit()

try:
    with open(sys.argv[1], "r") as inputfile:
        with open(sys.argv[2], "w") as outputfile:
            fields = ["OrderID", "Product", "Price", "Customer", "City", "PostalCode"]
            inputdata = csv.DictReader(inputfile)
            outputdata = csv.DictWriter(outputfile, fieldnames = fields)
            outputdata.writeheader()
            dataexists = set()
            for data in inputdata:
                if all(data[field] != "" for field in fields):
                    datatuple = tuple(data[field] for field in fields)
                    if datatuple not in dataexists:
                        dataexists.add(datatuple)
                        outputdata.writerow(data)
except FileNotFoundError:
    print("enter the correct filename")