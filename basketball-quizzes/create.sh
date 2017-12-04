#!/bin/bash
echo -ne '#!/bin/bash
declare -a array=(' > running.txt
echo -ne 'declare -a rawDataArray=(' >> runningd.txt
echo -ne 'declare -a questionArray=(' >> runningq.txt
echo -ne 'declare -a suggestedArray=(' >> runnings.txt
echo -ne 'declare -a statArray=(' >> runningt.txt
echo ')' >> endname.txt
for ii in 9
do
	for i in 1950 1970 1990 2010
	do
		python outputwinnersjs.py $ii season $i
		cat running.txt namedata.txt > runningn.txt
		cat runningn.txt > running.txt 
		cat runningd.txt datadata.txt > runningn.txt
		cat runningn.txt > runningd.txt 
		cat runningq.txt questiondata.txt > runningn.txt
		cat runningn.txt > runningq.txt 
		cat runnings.txt suggesteddata.txt > runningn.txt
		cat runningn.txt > runnings.txt

	done
	for (( iii=0; iii<10; iii++ ));
	do
		echo -ne '"'"bball-${ii}"'" ' > tempstat.txt
		cat runningt.txt tempstat.txt > statdata.txt
		cat statdata.txt > runningt.txt
		rm tempstat.txt
		rm statdata.txt
	done
	python outputtopnames.py $ii season
	cat namedata.txt ../../triplelog/nba/base/quiz-base.js > ../../triplelog/nba/quiz-names/quiz-bball-${ii}.js
done

cat running.txt endname.txt > namearray.txt
cat runningd.txt endname.txt > dataarray.txt
cat runningq.txt endname.txt > questionarray.txt
cat runnings.txt endname.txt > suggestedarray.txt
cat runningt.txt endname.txt > statarray.txt
cat namearray.txt dataarray.txt questionarray.txt suggestedarray.txt statarray.txt> allarray.txt
rm running.txt
rm runningd.txt
rm runningn.txt
rm runningq.txt
rm runnings.txt
rm runningt.txt
rm namearray.txt
rm dataarray.txt
rm questionarray.txt
rm suggestedarray.txt
rm statarray.txt
rm namedata.txt
rm datadata.txt
rm questiondata.txt
rm suggesteddata.txt
rm endname.txt
cat allarray.txt makequizzes-nba-base.sh > ../../triplelog/makequizzes-nba.sh
rm allarray.txt