# Below is a dictionary that contains information about real estate space for
# a doctor's office. Using the dictionary, create a csv file that has details
# for each space represented as rows. Name your file 'retail_space.csv.

import csv
import os



  

'''
Your final output should look like:

room-number,use,sq-ft,price
100,reception,50,75
101,waiting,250,75
102,examination,125,150
103,examination,125,150
104,office,150,100

'''



datastore = { "medical":[
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }

      ]
}

FILE = 'retail.space.csv'

outfile = open(FILE, 'w', newline = '')

writer = csv.writer(outfile)

headers = ['room-number', 'use', 'sq-ft', 'price']
writer.writerow(headers)

list1 = datastore['medical'] 

for dict in list1:
  rn = dict['room-number']
  use= dict['use']
  sq = dict ['sq-ft']
  price = dict ['price']

  new_row = [str(rn) + ',' + use + ',' + str(sq) + ',' + str(price)]
  writer.writerow(new_row)

outfile.close()