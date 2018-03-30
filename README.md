# motivation

This is a little widget to help stay focused—when you open a new tab in your browser you get not only a little speedbump on your way to whatever distraction you might have been heading to, you also get a motivating message (I customized them for my own perfectionist tendencies). It'll run in the background and also keep track (and give you a motivating little reminder) of how long you've gone without seeking that dopamine hit of checking your email/facebook/twitter. 



## Installation

1. Clone the repo to your computer with `git clone https://github.com/herdingbats/motivation.git` It comes packaged with a small folder of images (my photos, see more on [Flickr](https://www.flickr.com/photos/herdingbats/)! \<\/shamelessplug>).

2. Set the python script to run on startup:
* For Mac users: I've created a shell script that contains the one-line command to run the script and make it run on startup (directions and more information from [here](https://stackoverflow.com/questions/29338066/mac-osx-execute-a-python-script-at-startup). Specifically:  

```#!/bin/bash
python username/Desktop/motivation/motivation.py
```

> Substitute in the path for where you've saved the script.

> Add the .sh file to "System Preference -> Users and Groups -> Login items", the .sh script will call the > python file on login. 

* On Windows: I haven't tried this, but I believe solution #4 [here](https://stackoverflow.com/questions/4438020/how-to-start-a-python-file-while-windows-starts) is the simplest way to go.


3. Change your new-tab page to `localhost:5000`. You'll likely need to install an extension for this; I used the [Replace new tab page](https://chrome.google.com/webstore/detail/replace-new-tab-page/cnkhddihkmmiiclaipbaaelfojkmlkja) for Chrome.

