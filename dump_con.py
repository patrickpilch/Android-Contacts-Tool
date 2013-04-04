import sqlite3
import argparse
import csv
from os.path import splitext

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='Filename of the contacts database file.')
parser.add_argument('-csv', help='Enable csv file output. (Outputs <filename>.csv)',
					action='store_true')
args = parser.parse_args()

query = "SELECT raw_contacts._id, raw_contacts.display_name, data.data1 FROM raw_contacts, data \
		WHERE raw_contacts._id = data.raw_contact_id AND data.mimetype_id = 5 \
		ORDER BY raw_contacts._id"

with sqlite3.connect(args.filename) as connection:
	cursor = connection.cursor()
	if args.csv:
		with open(splitext(args.filename)[0] + '.csv', 'w') as csvfile:
			csv_writer = csv.writer(csvfile)
			for row in cursor.execute(query):
				csv_writer.writerow([row[1], row[2]])
	else:
		for row in cursor.execute(query):
			print(row[1], row[2])