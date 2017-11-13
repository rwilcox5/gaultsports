
arraylength=${#array[@]}

for (( i=0; i<${arraylength}; i++ ));
do
	python createquiz.py --title "TripleLog - Sports and Data Analysis" --question "${questionArray[$i]}" --onload "createAnswers()" --style ../assets/css/awesomplete.css --scripts "${dataArray[$i]}" --base mlb/base/quiz-base.html --output quizzes/mlb-${array[$i]}.html
done