#Recieving face tracking osc messages from Kyle McDonald's FaceOSC https://github.com/kylemcdonaldofxFaceTracker

#OSC messages are formatted in a URL style, so the code you see in the example on the project page with /filter, /volume, etc, would have a value associated with each “address” to control the filter and volume of a synthesiser, for example. The addresses FaceOSC sends values to are listed on the github page. As an example, you can get the x and y location of the face within the window, you can access the value at the address /pose/position. This is what I’ve done in the edited example attached below. If you run this program and have faceOSC open at the same time you will see a stream of X and Y values printed out to the console. The /found address is a Boolean for whether a face is found or not, and so on.


