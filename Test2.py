# covert csv to txt   for  undirected
import csv

txt_file = "/Users/dukechan/Downloads/sms_sna_oct18_undirected.txt"
csv_file = "/Users/dukechan/Downloads/sms_sna_oct18_undirected.csv"
in_txt = csv.reader(open(csv_file, "rb"), delimiter = ',')
out_csv = csv.writer(open(txt_file, 'wb'),delimiter = '\t')
out_csv.writerows(in_txt)