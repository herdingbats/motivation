from flask import Flask
from random import choice
import datetime
app = Flask(__name__)
global logtime
logtime = datetime.datetime.now()

positive_messages = ["If it works it is good enough.",
"If it doesn't work I can try it again.",
"There is space in between junk and perfection. My work doesn't fall into just one of those categories.",
"It's still possible people will like the work even if there are some flaws.",
"I've got a lot to do today but if I put one foot ahead of the other I'll move ahead.",
"If I don't get this job, it's probably not something I did, just that there are a lot of good applicants out there.",
"If I don't get this job, there are other opportunities."
]

def timemessage(elapsedtime):
  elapsedtime = elapsedtime.total_seconds()
  hours = elapsedtime // 3600
  minutes = (elapsedtime // 60) - (hours * 60)
  seconds = elapsedtime - (minutes * 60)

  if elapsedtime < 60:
    return "It has been " + ("%.0f" % seconds) + " seconds since your last new tab."
  elif elapsedtime < 1800:
    return str(minutes) + " minutes and " + ("%.0f" % seconds) + " seconds since your last new tab."
  elif elapsedtime < 3600:
    return "Good work! It has been " + str(minutes) + " since your last new tab."
  elif elapsedtime < 7200:
    return "You're doing great! It has been an hour and " + str(minutes) + " since your last new tab."
  else:
    return "Great focus! It has been more than " + str(hours) + " hours since your last new tab."


@app.route('/')
def fancypage():
  imageurl = ''
  bgimageline = "background-image: url('/static/images/image"+ str(choice(range(0,12))) + ".jpg');" 
  global logtime
  timeinterval = datetime.datetime.now() - logtime
  logtime = datetime.datetime.now()
  return """
<!DOCTYPE html>
<html>
<style>
body, html {
    height: 100%;
    margin: 0;
}

.bgimg {

    """ + bgimageline + """
    height: 100%;
    background-position: center;
    background-size: cover;
    position: relative;
    color: white;
    font-family: "Courier New", Courier, monospace;
    font-size: 25px;
}

.topleft {
    position: absolute;
    top: 0;
    left: 16px;
}

.bottomleft {
    position: absolute;
    bottom: 0;
    left: 16px;
}

.middle {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
}

hr {
    margin: auto;
    width: 40%;
}
a:link {
    color: white;
}
</style>
<body>

<div class="bgimg">
  <div class="topleft">
    <p><a href="chrome://apps">Chrome apps</a></p>
  </div>
  <div class="middle">
    <h1>""" + choice(positive_messages) + """</h1>
    <hr>
    <p>Do you <em>really</em> need another tab?</p>
  </div>
  <div class="bottomleft">
    <p>""" + timemessage(timeinterval) + """</p>
  </div>
</div>
  """


if __name__ == '__main__':
	app.run(use_reloader=True, debug=True) #debug=True because I want verbose errors IN THE BROWSER