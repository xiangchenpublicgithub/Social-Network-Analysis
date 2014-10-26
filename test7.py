# remove first line for undirected
import csv

txt_file = "/Users/dukechan/Downloads/sms_sna_oct18_undirected-1.txt"
csv_file = "/Users/dukechan/Downloads/sms_sna_oct18_undirected.csv"
csv_file_new = "/Users/dukechan/Downloads/sms_sna_oct18_undirected-1.csv"
with open(csv_file,'r') as f:
    with open(csv_file_new ,'w') as f1:
        f.next() # skip header line
        for line in f:
            f1.write(line)
in_txt = csv.reader(open(csv_file_new, "rb"), delimiter = ',')
out_csv = csv.writer(open(txt_file, 'wb'),delimiter = '\t')
out_csv.writerows(in_txt)
