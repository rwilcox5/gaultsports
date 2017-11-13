#!/bin/bash
cd poll
read -p "Enter The current week (according to the AP): "  week
echo "Let's get week $week data!"
python getpoll.py $week
echo "got the poll"
cp week${week}temp.csv week${week}.csv
python getgames.py $week
echo "got the games"
python outputtop25.py $week
cat helloworld.txt ../../gaultsports-site/ncaaf/base/ap-poll-base.js > ../../gaultsports-site/ncaaf/ap-poll.js 
echo "done!"