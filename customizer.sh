#!/bin/bash

dir=$1

file=$dir/powerdns_client/models/rr_set.py 
sed -i 's/self.changetype = changetype/self.changetype = changetype if changetype is not None else "NOT_SET"/' $file 

file=$dir/setup.py
perl -i -p0e 's/long_description=""".*"""/"long_description=long_description,"/se' $file
read -r -d '' text << EOM
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    long_description_content_type='text/markdown',
EOM
perl -i -p0e "s/setup\(/'$text'/se" $file 
