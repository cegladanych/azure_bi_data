import csv

converted_list = []
cnt = 0
# file = "C:\\Users\\admin\\Downloads\\names.csv"
with open("C:\\Users\\admin\\Downloads\\namesFixed.csv","w",encoding="utf-8",newline='') as outfile:
    csvwriter = csv.writer(outfile)

    with open("C:\\Users\\admin\\Downloads\\names.csv","r",encoding="utf-8") as file:
        reader = csv.reader(file,quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
        for row in reader:
            a = len(row[4])
            b = len(row[5])
            c = len(row[6])
            if a != 0 and b != 0 and c != 0:
                # cnt = cnt + 1
                # csvwriter.writerow(row)
                for element in row:
                    item = '"' + element + '"' 
                    converted_list.append(item)

                csvwriter.writerow(converted_list)
                converted_list.clear()
    # print(cnt)

