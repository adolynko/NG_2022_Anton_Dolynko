seconds = int(input())
days = seconds//86400 
hours = (seconds-(days*86400))//3600
minutes = (seconds-(days*86400)-(3600*hours))//60
seconds = (seconds-(days*86400)-(3600*hours)-(60*minutes))
print("days :",days,"hours :",hours,"minutes :",minutes,"seconds :",seconds)
#1 day is 24h is 1440 minutes is 86400 seconds
#1 hour is 60 minutes is 3600 sec
#1 minute is 60 second
