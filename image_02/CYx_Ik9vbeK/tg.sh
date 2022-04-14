TOKEN=5162521329:AAGw7_ZrcqCiIlf3CJMRl4WW7-sYJPO_drM
chat_ID=873388096
for i in ./*
do   
curl -F chat_id=$chat_ID -F photot=@"$i" https://api.telegram.org/bot$TOKEN/sendphoto
done
