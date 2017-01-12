#/bin/bash

#set connection data accordingly
source_host=host
source_port=6379
source_db=0

target_host=host2
target_port=6379
target_db=0
target_auth=password

#copy all keys without preserving ttl!
#redis-cli keys \* | while read key; do echo "Copying $key"; redis-cli --raw -h $source_host -p $source_port -n $source_db DUMP "$key" | head -c -1|redis-cli -x -h $target_host -p $target_port -n $target_db -a $target_auth RESTORE "$key" 0; done
redis-cli -h $source_host -p $source_port -n $source_db --scan --pattern "*" |  while read key; do echo "Copying $key"; redis-cli --raw -h $source_host -p $source_port -n $source_db DUMP "$key" | head -c -1|redis-cli -a 3ts1nll4dr3 -x -h $target_host -p $target_port -n $target_db -a $target_auth RESTORE "$key" 0; done


