#import statements
import csv, os, random

#Input Parameters==========
file_name = "car_data.csv"
generate_records  = 10000
unique_records    = 100
#==========================

#Templates for generating data=======================================================================
headings    =   ['license_plates', 'states', 'colors']
color_names =   ['Red','Green','Blue','Purple','Orange','White','Black']
state_codes =   {'AP':'Andhra Pradesh','AR':'Arunachal Pradesh','AS':'Assam',
                'BR':'Bihar','CG':'Chhattisgarh','GA':'Goa','GJ':'Gujarat','HR':'Haryana',
                'HP':'Himachal Pradesh','JK':'Jammu and Kashmir','JH':'Jharkhand',
                'KA':'Karnataka','KL':'Kerala','MP':'Madhya Pradesh','MH':'Maharashtra',
                'MN':'Manipur','ML':'Meghalaya','MZ':'Mizoram','NL':'Nagaland','OR':'Orissa',
                'PB':'Punjab','RJ':'Rajasthan','SK':'Sikkim','TN':'Tamil Nadu','TR':'Tripura',
                'UK':'Uttarakhand','UP':'Uttar Pradesh','WB':'West Bengal','TR':'Tripura',
                'AN':'Andaman and Nicobar Islands','CH':'Chandigarh','DH':'Dadra and Nagar Haveli',
                'DD':'Daman and Diu','DL':'Delhi','LD':'Lakshadweep','PY':'Pondicherry'}
#=====================================================================================================


#Data generator function==============================================================================
def append_new_rows(writer, total_rows, unique_rows):
    temp_row = []
    idx = 0
    for i in range(0, unique_rows):
        color       = random.choice(color_names)
        state_code  = random.choice(list(state_codes.keys()))
        state_name  = state_codes[state_code]
        num1        = str(random.randint(10,31))
        char1       = random.choice(['A','B','C','D'])
        num2        = str(random.randint(0,9))+str(random.randint(100,201))
        plate_num   = state_code+num1+char1+num2 #example = MH32C1289

        row_data = [plate_num, state_name, color]
        print(f'>> Generated Numbers {idx}: {row_data[0]}')
        writer.writerow(row_data)
        temp_row.append(row_data)
        idx+=1

    while unique_rows <= total_rows:
        row_data = random.choice(temp_row)
        writer.writerow(row_data)
        print(f'>> Repeating Numbers {idx}: {row_data[0]}')
        unique_rows +=1
        idx+=1
#=======================================================================================================


#File handling and data generator controller============================================================
def main():
    #if file exists we will append new data
    if os.path.isfile(file_name):
        print('>> File Already Exists, Appending New Rows')
        csvFile = open(file_name, 'r', newline='')
        data = csv.reader(csvFile)
        try:
            fhead = list(data)[0][0]
            #if heading not present clear file and write from beginning
            if not fhead == 'license_plates':
                print('>> Heading not Available, Writing from Beginning')
                csvFile.close()
                csvFile = open(file_name, 'w', newline='')
                writer = csv.writer(csvFile)
                writer.writerow(headings)
                csvFile.close()
        except IndexError:
            #if file is blank, create headings
            print('>> Blank CSV File, Writing from Beginning')
            csvFile = open(file_name, 'w', newline='')
            writer = csv.writer(csvFile)
            writer.writerow(headings)
            csvFile.close()

        with open(file_name, 'a', newline='') as csvFile:
            writer = csv.writer(csvFile)
            append_new_rows(writer, generate_records, unique_records)
            csvFile.close()

    else:
        print('>> Creating New File And Appending New Rows')
        with open(file_name, 'a', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(headings)
            append_new_rows(writer, generate_records, unique_records)
            csvFile.close()
#=======================================================================================================

#Running the actual application
if __name__ == '__main__':
    main()
#=============================
