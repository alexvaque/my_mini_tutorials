#/bin/bash

#set connection data accordingly
source_host=aa
source_port=aa
source_db=0
password=aa

#remove all keys - elegant FLUSH all without blocks
redis-cli -h $source_host -p $source_port -n $source_db -a $password --scan --pattern "*" |  while read key; do redis-cli -a $password -h $source_host -p $source_port -n $source_db DEL "$key"; done
