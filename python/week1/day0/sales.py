import csv

with open("sales.csv", 'r') as messyfile:
    messydata = csv.DictReader(messyfile)
    with open("cleaned_sales.csv", 'w') as cleanfile:
        with open("placeholder_sales.csv", 'w') as placeholderfile:
            fields = ["OrderID", "Product", "Price", "Customer", "City", "PostalCode"]
            cleandata = csv.DictWriter(cleanfile, fieldnames = fields)
            placeholderdata = csv.DictWriter(placeholderfile, fieldnames = fields)
            cleandata.writeheader()
            placeholderdata.writeheader()

            for row in messydata:
                if all(row[field] != "" for field in fields):
                    cleandata.writerow(row)
                for field in fields:
                    if row[field] == "":
                        row[field] = "unknown"
                placeholderdata.writerow(row)