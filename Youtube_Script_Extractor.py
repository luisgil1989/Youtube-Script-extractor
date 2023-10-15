#####If you're using PyCharm and still encountering an error after installing the youtube-transcript-api library,
# it's possible that the PyCharm environment is not using the same Python interpreter as the one where you installed the library with pip.
# Here are some steps you can take to troubleshoot this issue:

####Ensure you're using the correct Python interpreter in PyCharm:

#In PyCharm, go to "File" > "Settings" (or "PyCharm" > "Preferences" on macOS).
#Under "Project" settings, select "Python Interpreter."
#Make sure you've selected the same Python interpreter where you installed youtube-transcript-api with pip.
#If you've selected the correct interpreter and are still facing issues, try restarting PyCharm. Sometimes, PyCharm may not recognize newly installed packages until you restart the IDE.

#Verify that the Python interpreter used in your PyCharm project matches the one you used with pip to install packages. You can check this by running the following code within PyCharm:

##import sys
#print(sys.executable)


################################################
from youtube_transcript_api import YouTubeTranscriptApi as yta

# YouTube video URL (just the video ID is needed)

# lets put an example: https://www.youtube.com/watch?v=@@@@@
# We want to chose "@@@@" for video url
video_url = '@@@@@'  # This should be the video ID, not the full URL

data = yta.get_transcript(video_url)

transcript = ''
for value in data:
    for key, val in value.items():
        if key == 'text':
            transcript += val + ' '  # Add a space between text segments

# No need to split and join again, you can just use transcript directly
final_tra = transcript

with open("text.txt", 'w') as file:
    file.write(final_tra)
