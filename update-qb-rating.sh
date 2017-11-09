#!/bin/bash
cd nfl_scrape
python genstr.py
cat helloworld.txt ../../gaultsports-site/nfl/custom-QB-rating-base.js > ../../gaultsports-site/nfl/custom-QB-rating.js
cd ..
cd ..
cd gaultsports-site
echo "update website"
rsync -e "ssh -i /home/rwilcox/.ssh/cdn77_rsa" -va . user_ebh79y2z@push-24.cdn77.com:/www/
