# covert csv to txt   for  directed
import csv

txt_file = "/Users/dukechan/Downloads/sms_sna_oct18_directed.txt"
csv_file = "/Users/dukechan/Downloads/sms_sna_oct18_directed.csv"
in_txt = csv.reader(open(csv_file, "rb"), delimiter = ',')
out_csv = csv.writer(open(txt_file, 'wb'),delimiter = '\t')
out_csv.writerows(in_txt)











