import csv

converted_list = []

with open("names.csv","w",encoding="utf-8",newline='') as outfile:
    csvwriter = csv.writer(outfile)

    with open("names.csv","r",encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                converted_list.append(element.replace('\n',''))

            csvwriter.writerow(converted_list)
            converted_list.clear()