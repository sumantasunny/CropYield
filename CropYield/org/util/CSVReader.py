import csv

def CSV_File_Read():
    with open('/home/suntron/Documents/LiClipse Workspace2/CropYield/org/util/apy.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            print '* '.join(row)
            
def main():
    CSV_File_Read()
    
    
main()