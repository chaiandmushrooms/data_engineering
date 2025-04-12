import csv

with open("messy.csv", "r") as messyfile:
    messydata = csv.DictReader(messyfile)
    with open("squeaky.csv", "w") as squeakyfile:
        fields = ["OrderID", "Product", "Price", "Customer", "City", "PostalCode"]
        squeakydata = csv.DictWriter(squeakyfile, fieldnames = fields)
        squeakydata.writeheader()
        seen = set()
        
        for row in messydata:
            if not (any(row[field] == "" for field in fields)):
                row_tuple = tuple(row[field] for field in fields)
                if row_tuple not in seen:
                    seen.add(row_tuple)
                    squeakydata.writerow(row)