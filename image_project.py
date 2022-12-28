import threading

import requests
import time
start=time.perf_counter()
print(start)
image_sunny = [
        'https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.deccanherald.com%2Fsites%2Fdh%2Ffiles%2Farticle_images%2F2020%2F05%2F19%2Fsunny-leone-crop-1583632072-1558673375.jpg&imgrefurl=https%3A%2F%2Fwww.deccanherald.com%2Flok-sabha-election-2019%2Fits-always-sunny-in-gurdaspur-735513.html&tbnid=LIVVsu-_V5PAGM&vet=12ahUKEwi52bG-lNP7AhVNj9gFHVUNBq0QMygFegUIARDcAQ..i&docid=8Xm__ypgfjcb0M&w=1221&h=957&q=sunny%20photos&ved=2ahUKEwi52bG-lNP7AhVNj9gFHVUNBq0QMygFegxxxUIARDcAQ',
        'https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F2662116%2Fpexels-photo-2662116.jpeg%3Fcs%3Dsrgb%26dl%3Dpexels-jaime-reimer-2662116.jpg%26fm%3Djpg&imgrefurl=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fnature%2F&tbnid=wQieVlIpCtgGrM&vet=12ahUKEwic_ImLldP7AhX02HMBHavIDHEQMygAegUIARDhAQ..i&docid=ShwNVOdFBcmkxM&w=5407&h=3605&q=nature%20photos&ved=2ahUKEwic_ImLldP7AhVNX02HMBHavIDHEQMygAexxxgUIARDhAQ'
    ]

def complete(image_sunny):
    print("sleeping the image")
    img=requests.get(image_sunny).content
    img_name=image_sunny.split('AhVN')[1]
    img_name=f'{img_name}.jpg'
    with open(img_name,'wb') as img_file:
        img_file.write(img)
        print(f'{img_name} was downloaded.......')
Rockys=[]
for i in image_sunny:
    Rocky=threading.Thread(target=complete,args=[i])
    Rocky.start()
    Rockys.append(Rocky)

for i in Rockys:
    i.join()

finish=time.perf_counter()
print(finish)




