#!/bin/bash  
declare -a slave_is
slave_is=($(/usr/local/mysql/bin/mysql -unagios -pnagiosadmin    -e "show slave status \G"|grep Running |awk '{print $2}'))
if [ "${slave_is[0]}" = "Yes" -a "${slave_is[1]}" = "Yes"  ]
    then
    echo "OK -slave is running " 
    exit 0
    else
    echo "Critical -slave is error" 
    exit 2
fi

