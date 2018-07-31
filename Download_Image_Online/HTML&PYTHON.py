import random
import webbrowser
import urllib.request
def Download_Image(url):
    imageName=str(random.randrange(1,1000))+'.jpg'
    urllib.request.urlretrieve(url,imageName)

Download_Image("https://scontent-sin6-1.xx.fbcdn.net/v/t1.0-9/s851x315/16807487_1114617731979918_6386687668299866007_n.jpg?oh=9bd6f375e6a37b8bd8a40cbd467651bf&oe=59340059")
webbrowser.open_new_tab('Frist_Html.html')
