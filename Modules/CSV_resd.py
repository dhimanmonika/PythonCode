import csv


with open('csvfile.csv','r') as csvfile:
    csv_reader=csv.reader(csvfile)

    with open('new_csv.csv','w') as newfile:
        csv_writer=csv.writer(newfile, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)

            