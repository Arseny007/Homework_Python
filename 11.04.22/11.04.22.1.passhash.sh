count=1
rm sha_log_info.txt
file="log_info.txt"
cat $file | while read line
do 
    if [ $(( $count % 2 )) -eq 1 ] && [ ]
    then
    echo "$line" >> sha_log_info.txt
    elif [ $(( $count % 2 )) -eq 0 ]
    then
    echo "$line" | sha256sum >> sha_log_info.txt
    fi
    count=$(( $count + 1 ))
done