import pyunsplash
import requests
import os
import re
import json
import shutil

pu = pyunsplash.PyUnsplash(api_key='YOUR API KEY')


def main():
    pageNumber = 10
    print (" ---> Requesting photos...")
    count = 0
    update = False
    retrievePic = 0;
    while retrievePic < pageNumber:
        this_user = pu.user('ourselp', w=100, h=100)
        photos = this_user.photos(page=retrievePic, per_page=20)    # photos is an instance of class Photos
        retrievePic += 1
        if photos.entries:
            pageNumber += 1
            for photo in photos.entries:
                count += 1
                filename = photo.id + '.jpeg'
                print (photo.link_download_location)
                linkSourceImg = requests.get(photo.link_download_location + '/?client_id=UVtouHS8slGsncRIUtSKsI5BZdiI2dzCQ0hav80KQ4Y')
                print (linkSourceImg)
                data = linkSourceImg.json()
                url = data['url']
                path = '/home/pi/Desktop/photoframe/unsplash-pictures/%s' % filename
                folder = '/home/pi/Desktop/photoframe/unsplash-pictures'
                try:
                    image_file = open(path)
                    print (" ---> Already have %s" % url)
                except IOError:
                    print (" ---> Downloading %s" % url)
                    r = requests.get(url, stream=True)
                    if r.status_code == 200:
                        with open(path, 'wb') as f:
                            f.write(r.content)
                            update = True

    #if it added or removed a photo, update slideshow
    if update == True:
        print (" ---> Restarting slideshow")
        os.system("kill $(ps aux | grep '[f]eh' | awk '{print $2}')")
        os.system("/home/pi/bin/script_slideshow")

if __name__ == '__main__':
    main()

