old=$(cat sha_log_info.txt)
file="log_info.txt"
cat $file | while read line
do
    result=$(echo $(echo $line | cut -d " " -f 1) $(echo $line | cut -d " " -f 2 | sha256sum | cut -d " " -f 1))
    if [[ $old != *"$result"* ]]; then
    echo $result >> sha_log_info.txt
    fi
done