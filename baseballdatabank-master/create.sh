#!/bin/bash
echo -ne '#!/bin/bash
declare -a array=(' > running.txt
echo -ne 'declare -a rawDataArray=(' >> runningd.txt
echo -ne 'declare -a questionArray=(' >> runningq.txt
echo -ne 'declare -a suggestedArray=(' >> runnings.txt
echo -ne 'declare -a statArray=(' >> runningt.txt
echo ')' >> endname.txt
for ii in 9 14 17 23
do
	for i in 1900 1920 1940 1960 1980 2000
	do
		python outputwinnersjs.py $ii season $i p
		cat running.txt namedata.txt > runningn.txt
		cat runningn.txt > running.txt 
		cat runningd.txt datadata.txt > runningn.txt
		cat runningn.txt > runningd.txt 
		cat runningq.txt questiondata.txt > runningn.txt
		cat runningn.txt > runningq.txt 
		cat runnings.txt suggesteddata.txt > runningn.txt
		cat runningn.txt > runnings.txt

	done
	for (( iii=0; iii<21; iii++ ));
	do
		echo -ne '"'"pitcher-${ii}"'" ' > tempstat.txt
		cat runningt.txt tempstat.txt > statdata.txt
		cat statdata.txt > runningt.txt
		rm tempstat.txt
		rm statdata.txt
	done
	python outputtopnames.py $ii season p
	cat namedata.txt ../../gaultsports-site/mlb/base/quiz-base.js > ../../gaultsports-site/mlb/quiz-names/quiz-pitcher-${ii}.js
done
for ii in 10 16 17 20 21 22
do
	for i in 1900 1920 1940 1960 1980 2000
	do
		python outputwinnersjs.py $ii season $i b
		cat running.txt namedata.txt > runningn.txt
		cat runningn.txt > running.txt 
		cat runningd.txt datadata.txt > runningn.txt
		cat runningn.txt > runningd.txt 
		cat runningq.txt questiondata.txt > runningn.txt
		cat runningn.txt > runningq.txt 
		cat runnings.txt suggesteddata.txt > runningn.txt
		cat runningn.txt > runnings.txt

	done
	for (( iii=0; iii<21; iii++ ));
	do
		echo -ne '"'"batter-${ii}"'" ' > tempstat.txt
		cat runningt.txt tempstat.txt > statdata.txt
		cat statdata.txt > runningt.txt
		rm tempstat.txt
		rm statdata.txt
	done
	python outputtopnames.py $ii season b
	cat namedata.txt ../../gaultsports-site/mlb/base/quiz-base.js > ../../gaultsports-site/mlb/quiz-names/quiz-batter-${ii}.js
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
cat allarray.txt makequizzes-base.sh > ../../gaultsports-site/makequizzes.sh
rm allarray.txt