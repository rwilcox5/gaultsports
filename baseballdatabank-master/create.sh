cat startname.txt > running.txt
cat startdata.txt > runningd.txt
cat startquestion.txt > runningq.txt
cat startsuggested.txt > runnings.txt
for ii in 9 14 17 23
do
	for i in 1990 2000 2010 2015
	do
		python outputc.py $ii season $i
		cat running.txt namedata.txt > runningn.txt
		cat runningn.txt > running.txt 
		cat runningd.txt datadata.txt > runningn.txt
		cat runningn.txt > runningd.txt 
		cat runningq.txt questiondata.txt > runningn.txt
		cat runningn.txt > runningq.txt 
		cat runnings.txt suggesteddata.txt > runningn.txt
		cat runningn.txt > runnings.txt 
	done
done
cat running.txt endname.txt > namearray.txt
cat runningd.txt endname.txt > dataarray.txt
cat runningq.txt endname.txt > questionarray.txt
cat runnings.txt endname.txt > suggestedarray.txt
cat namearray.txt dataarray.txt questionarray.txt suggestedarray.txt > allarray.txt
rm running.txt
rm runningd.txt
rm runningn.txt
rm runningq.txt
rm runnings.txt
rm namearray.txt
rm dataarray.txt
rm questionarray.txt
rm suggestedarray.txt
rm namedata.txt
rm datadata.txt
rm questiondata.txt
rm suggesteddata.txt
cat allarray.txt makequizzes-base.sh > ../../gaultsports-site/makequizzes.sh