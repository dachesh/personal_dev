import os
import sys
import glob
from boto.s3.connection import S3Connection as s3con
from boto.s3.key import Key


access_key= '<access_key>' 
secret_key = '<secret_key>'

source_path = "<path to files you wish to push out"

lines = glob.glob(source_path + "/*")  #grabs all files within source_path

#print(lines)

conn = s3con(access_key, secret_key, is_secure=False,) #dives into specified s3 connection
bucket =  conn.get_bucket('alarms-controlcharts') #pushes into specific bucket, more research about pushing to folders is needed

k = Key(bucket)

for fname in lines:
	lngth = len(fname)
	cntr = fname.rfind('/')
	pngname = fname[cntr:lngth]
	k.key = pngname
	k.set_contents_from_filename(fname)
	k.make_public()

print "<message that indicates completion>"