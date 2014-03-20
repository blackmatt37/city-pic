import pyimgur
import urllib

city = raw_input("Enter city name");

client_id = '5af83233f671fc4'

client_secret = '9dc5c91cef8192c72fcde94af4868427ffdf4792'


request = "http://maps.googleapis.com/maps/api/staticmap?center=" + city + "&size=600x300&sensor=false&maptype=hybrid"

urllib.urlretrieve(request, "0.png")
im = pyimgur.Imgur(client_id)
image = im.upload_image("0.png", title=city)
print(image.link)
