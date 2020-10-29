# Smart India Hackathon 2020 

## Problem Statement

- **Organisation: Great Learning**
- **Problem No.: GL32**

[Problem Statement Link](https://www.sih.gov.in/sih2020PS)

The problem statement is to create a mechanism to monitor and measure the attention span of the learners in the instructor led online sessions. Following are a few ideas on the measures that can be used to quantify the level of attention span: 
-  Out of the designated session-time, what proportion of session was one-way dialogue vs two-way dialogue 
-  number of distinct learners who participated in the session 
-  presence of background noise, chatters in the session, etc.. Expected Outcomes 
-  Real time dashboard that quantifies the participation for each participant 
-  Real time triggers in case of sub-optimal participation 
-  Suggestions (along with implementation) of other ideas to quantify level / quality of interactions Great Learning will be sharing sample recording of the online mentored sessions


## Design Flow
![Architechture Design ](https://github.com/anshumyname/SIH2020/blob/master/imgs/design.png) 

## Solution Proposed
We have divided the problems into the following subproblems:

- **Attention Detector in Visual Media** by OpenCV and image processing modules of Python3. The basic idea is to get an input stream of the student's webcam and apply CNN and Scipy-Kit on the same. We have used the pre-trained weight Harcascade-Classifier and also tested for shape_predictor_68_face_landmarks.dat, as of now. The primary features for this are Face Detection, Drowsiness Detection by measuring Eye-Aspect-Ratio and Head Position Estimation through dlib. 

-  **Analysis of Auditory Media** by checking for Noise on the Student’s side and informing them if the noise is unsuitable for Conversation on the Channel. Fourier Transform will be applied through SciKit onto the audio channels. We would use external APIs like Discord for effective Voice Chat options, or the infrastructure might be created by Flask integration, of which the option to mute or be muted will be given. This would reduce chatter and distraction on the channel. The time duration for active interaction will also be tabulated.

-  **Group Text Chat** This would be achieved by Socket Programming and Threading through these chats. These would be made available on the browser through Flask on either side. Along with this, a User-Friendly Dashboard will be integrated for simple UI for both the clients. The response time for all replies will also be noted for gathering their Attention-Data during the session. Real-time triggers would be provided to the student through the dash-board in case of inattentiveness as detected by the “Attention Detection Model”.

-  **Data Analysis** for the data accumulated during the Session for each individual participant through their Attention Reports (the timeline for which they have been detected as having paid attention). This will help us in tabulating and plotting the time period versus the number of students paying attention. Through this, the more engaging part of the session may be gauged and that would suggest parts of the session that may be improved upon.

## Screenshots

![Head Position Detection](https://github.com/anshumyname/SIH2020/blob/master/imgs/look.jpg)

![Final View](https://github.com/anshumyname/SIH2020/blob/master/imgs/main.jpg)


