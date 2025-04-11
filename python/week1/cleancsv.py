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

            for messy in messydata:
                if all(messy[field] != "" for field in fields):
                    cleandata.writerow(messy)
                for field in fields:
                    if messy[field] == "":
                        messy[field] = "unknown"
                placeholderdata.writerow(messy)