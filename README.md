# Unsplash-DigitalFrame
A little project I made who use the unsplash API to retrieve picture of an account and save them locally on a raspberry PI for a custom digital-frame. 

First, save the main script "download_user_unsplash_photos.py" on your desktop and change the line 18 to your account :
> this_user = pu.user('YOUR_USERNAME_ON_UNSPLASH', w=100, h=100)

# Dependencies

I am using 3 external libraries : 

pyunsplash which can be found here : https://github.com/salvoventura/pyunsplash
```sh
$ pip install pyunsplash
```
Request for the request to the unsplash API : https://requests.readthedocs.io/en/master/
```sh
$ pip install request
```

And feh for the slideshow : https://github.com/derf/feh
```sh
$ pip install feh
``` 

# Slideshow

In this project you can found 2 shell script, they will be use via our script to start / restart our slideshow when there is new pictures to load

Create a new folder in : 
> /home/pi/bin/

This is where you will save the 2 scripts 
> kill_slideshow
> script_slideshow

Tips: you can change the number after -D on script_slideshow if you want to slowdown the speed of the slideshow, if you dont touch anything it will change every 3 seconds which can't be rapidly anoying. 

# Crontab

To automate the task of executing the script, you will need to create a Crontab :
For this, open the crontab : 
```sh
$  crontab -e
``` 

And add this line to execute our script it every day at 1am :
```sh
$  0 1 * * * python /home/pi/Desktop/download_user_unsplash_photos.py
``` 
(consedering I save the script on the Desktop of course)

# Setup Auto-start

To start the slideshow when you start the Raspberry you need to : 
  - Go to : cd /etc/xdg/autostart
  - Create the file slideshow_image_changer.desktop : 
    ```sh
    - $ sudo nano slideshow_image_changer.desktop 
    ```
   - (copy / paste the one with the same name on this project)
   - Save & Close
 
# Disabled sleep mode

Finally, we have to disabled the sleep mode, for this :
- Edit the kdb config file : sudo nano /etc/kbd/config
- Inside the file, change the BLANK_TIME to 0 (so it never goes blank)
- Still inside the file, change the POWERDOWN_TIME to 0 (so it never automatically shuts off)
- Save & Close


# License
unsplash-DigitalFrame is released under the [MIT License](<http://www.opensource.org/licenses/MIT>)


<p align="center">
 If you like this project and you are a curious recruiter, come checkout my portfolio : https://www.philippeoursel.com/
</p>
