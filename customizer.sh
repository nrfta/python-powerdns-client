#!/bin/bash

dir=$1

file=$dir/powerdns_client/models/rr_set.py 
sed -i 's/self.changetype = changetype/self.changetype = changetype if changetype is not None else changetype/' $file 
