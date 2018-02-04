cd ncaab
python getscores.py
echo "got scores"

python getgameinfo.py
echo "got game info (location)"

python combinetogames.py
echo "put all game data into allgames2017.csv"

python genjsfromscores.py
echo "put all js data into helloworld"

python makedab.py
echo "created rankings"

cat helloworld.txt ../../triplelog/ncaab/base/custom-NCAAB-rpi-base.js > ../../triplelog/ncaab/custom-NCAAB-rpi.js
cat hello_dab.txt ../../triplelog/ncaab/base/dab-base.js > ../../triplelog/ncaab/dab.js

