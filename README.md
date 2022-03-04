# instagram-video-and-photos-downloader

**A. Description:**

This is a Python application that download images and videos from Instagram (file named: *instagramAutomation.py*).
Python Selenium library and chrome driver were used to perform various operations on the Web browser without user inputs.

The interface is built using Flask web framework (File named: instagramApp.py and rendered html template: *index.html* )

**B. instagramAutomation.py File:**

This contains functions that perform the following automatically using Selenium and webdriver:

    1. Launch Instagram in chrome browser.
    2. Permit the user to log into his or her Instragam account.
    3. Turns off Instagram notifications
    4. Serch Instagram account
    5. Click on first search result.
    6. Find and print images urls
    7. Create a local directory in the current project directory
    8. Download Images.

**C. instagramApp.py File:**

This is develeloped using Flask web framework. Below is the logic:

    1. Once you access the page on http://127.0.0.1:5000/, the page loads then it calls functions in instagramAutomation.py module.
    2. You are prompted your instagram username and password.
    3. Then the download begins.
    4. Once the download completes a message from the rendered index.html is displayed showing that download is complete.
    
**4. index.html template File**

This is the rendered html template. It displays a message when download is complete.

Note: Feel free to check it out, later on I will try to Improve it to be much better!



