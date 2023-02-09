#Name: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 02/07/2023
#This code is designed to read a json file of NYC SAT scores and tester data, then write it
#into a csv file with the tester's DBN's, school, and average scores.


import json
class SatData:
    def __init__(self):
        """
        Class designed to open json file and convert student's id numbers, scores, and schools in csv file
        this class uses an __init__ method and a save_as_csv method
         """
        with open('sat.json', 'r') as infile: #opens and reads json file
            self._sat_list = json.load(infile)

            self._sat_data = self._sat_list["data"]
            self._header = [] #creates empty list for header

            for i in range(8,14): #iterates through attributes 8-13 in json
                self._header.append(self._sat_list['meta']['view']['columns'][i]['name']) #adds 8 header names from the json list


    def save_as_csv(self, dbn_list):
        """
        save_as_csv method will be used to sort through the DBN's, scores, and schools, then write them into
        a csv file with by the dbn's the user inputs
        """
        outfile = open("output.csv", "w") #opens csv file for writing
        outfile.write(','.join(self._header)) #joins headers for the csv file
        outfile.write("\n") #new line break

        dbn_list.sort() #sorts list of dbn's

        for dbn in dbn_list: #iterates through dbn's
            for row in self._sat_data:
                if dbn == row[8]: #checks if dbn is in list from json file
                    outfile.write(",".join(row[8:14])) #adds info from attributes 8-14 to csv
                    outfile.write('\n') #adds line breaks to csv

        outfile.close() #closes outfile writing















       # with open('output.csv', 'w') as outfile:






           # outfile.write("DBN, School Name, Number of Test Takers, Critical Reading Mean, Mathematics Mean, Writing Mean\n") #Creates headers
           # self._sat_list.sort
          #  for row in self._sat_list:
               # if row["DBN"] in self._sat_list:
                  #  if "," in row["School Name"]:
                     #   row["School Name"] = '"' + row["School Name"] + '"'
                   # outfile.write(row["DBN"] + "," + row["School Name"] + "," + str(row["Number of Test Takers"]) + "," + str(row["Critical Reading Mean"]) + "," + str(row["Mathematics Mean"]) + "," + str(row["Writing Mean"]) + "\n")

sd = SatData()
dbn_list = ["02M303", "02M294", "01M450", "02M418"]
sd.save_as_csv(dbn_list)


