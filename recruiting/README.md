getplayerlist.py downloads links to all verbal/signed recruits.
First parameter is number of stars .
Second parameter is year to download.
Third parameter is file to create-auto adds year and number of stars so 'allrecs' becomes 'allrecs20173.csv'.

combineallstars.py combines all different stars into one csv.
first parameter is the year.
second parameter is the basefile-auto adds year and 1-5 stars to combine into base+year.csv.

getrecruitdata.py downloads data on all recruits in list.
first parameter is year.
second parameter is basefile.
creates basefile+year+done+threadindex.csv with recruit data.
checks for players that have been done and adds to files.

combinerecruitdata.py combines all different recruits from threads into one csv.
first parameter is the year.
second parameter is the basefile-auto adds year to combine into base+year+done.csv.

analyzerecruits.py generates rankings
first parameter is the year.
second parameter is the basefile-auto adds year to get base+year+done.csv.
outputs to helloworld.txt

Combined into updat-recruiting.sh in gaultsports



