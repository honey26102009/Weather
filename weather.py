import requests, json
apiKey="b6907d289e10d714a6e88b30761fae22"
baseUrl="https://samples.openweathermap.org/data/2.5/forecast/hourly?q="
cityName=input("enter your city:")
completeURL=baseUrl+cityName+"&appid="+apiKey
response=requests.get(completeURL)
data=response.json()
li=data['list']
length=len(li)


while True:
    choice=int(input("enter the choice"))
    if choice==1:
        date = input("enter the date")
        for i in range(length):
            if li[i]['dt_txt']==date:
                print("Temperature: ",li[i]['main']['temp'])
        continue
    elif choice==2:
         date = input("enter the date")
         for i in range(length):
                 if li[i]['dt_txt']==date:
                     print("Speed: ",li[i]['wind']['speed'])
         continue
    elif choice==3:
         date = input("enter the date")
         for i in range(length):
                 if li[i]['dt_txt']==date:
                     print("Pressure: ",li[i]['main']['pressure'])
         continue
    elif choice==0:
        break
