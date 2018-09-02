#!/usr/bin/python
# -*- coding: UTF-8 -*-
import psycopg2
import os
import sys

try:
    pg_conn = psycopg2.connect(database="test",
                               user="gangjun",
                               password="123456",
                               host="localhost",
                               port="5432")  # there is to change your db info
except Exception as e:
    print e
    pg_conn = None
if pg_conn:
    print "Connected successful"
    db_cur = pg_conn.cursor()
else:
    db_cur = None
if pg_conn:
    begin_btn = input("To start？[Y/N]: ")
else:
    print "Failed to connect,please checked your code...Is closing！"
    sys.exit(0)
if begin_btn == 'N':
    sys.exit(0)
else:
    pass
file_path = "H:\\Work\\test\\image"   # in windows，need to two '\'
file_count = os.listdir(file_path)
file_current = os.getcwd()
print "get father file path: ", file_current
print "file list:", file_count
print "folder name: ", os.path.basename(file_path)
file_array = []
for line in file_count:
    if line:
        print "find file：", line
        all_file_name = line.decode('gbk').encode('utf-8')
        if len(all_file_name) >= 10:
            hs_code = all_file_name[0:10]
            file_name = all_file_name[:-4]
            print "file hs_code", hs_code
            print "file name：", file_name
            if db_cur:
                db_cur.execute("SELECT * FROM custom_register WHERE register_code='" + hs_code + "'")
                rows = db_cur.fetchall()
                print "database rows：", rows
                if rows:
                    for rows_name in rows:
                        if rows_name[1]:
                            print "old file name ==> ", file_name
                            print "new file name ==> ", rows_name[1]
                            old_img_name = rows_name[1].decode('utf-8')
                            os.chdir(file_path)
                            os.rename(line, old_img_name + '.png')

if pg_conn:
    db_cur.close()
    pg_conn.close()
