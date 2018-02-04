cd recruiting
for i in 1 2 3 4 5
do
	python getplayerlist.py $i 2018 "football"
	echo "Got some stars"
done
echo "created list of committed recruits"

python combineallstars.py 2018 "football"
echo "merged all players into football2018.csv"

for i in 0 1 2 3 4
do
	rm football2018done$i.csv
done
echo "removed old data"

python getrecruitdata.py 2018 "football"
echo "got all recruit data into football2018done0-4.csv"

python combinerecruitdata.py 2018 "football"
echo "combined all threads into football2018done.csv"

python analyzerecruits.py 2018 "football"
echo "Recruits Analyzed"
cat helloworld.txt ../../triplelog/ncaaf/base/recruiting-base.js > ../../triplelog/ncaaf/recruiting.js

