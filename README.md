# website-status-check

Check status of specified URLs and email notifications if any URLs are unreachable


## Run

You can run the file manually: `python3 check.py`

You can also add this to an automated service, like cron. Here's an example cron line to have the script automatically run every 15 minutes if cloning this repository to your user directory: `0,15,30,45 * * * * python3 ~/website-status-check/check.py`


## Maintain

check.py contains all of the code you'll need to maintain. E.g. you can:

- edit the URLs to be scanned by adding/removing strings to the urls_to_check array
- change the email notifications (sender address, subject text, message text, etc)

check.py is well commented, so please refer to the file for more instructions on how to maintain it.


## Testing

To test that the script is running as desired (i.e. it's identifying erroneous URLs and notifying you of them) then try temporarily setting some URLs that you know to be invalid within the urls_to_check array and then run check.py. Once you're happy it's working, remove these intentionally erroneous URLs. 
