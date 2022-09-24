# VSeeFace-LiveLink-Relay
Send LiveLink IPhone tracking data to VSeeFace using iFacialMocap protocol

I wanted to use my IPhone for facial tracking with the VSeeFace Vtubing app, but all of the apps it connects to require to pay.
This python script will recieve data from the Unreal Engine LiveLink IOS app and reformat it as iFacialMocap data for use in VSeeFace (or other apps that may make use of this protocol)

Of note that this is pretty rough, but the all of the tracking functionality is still there and it's free unlike other options.
One notable feature that is missing, is that LiveLink only tracks head rotation, not position. So head movements side to side or up and down will not be recorded with this solution.

# Usage
Download the python file, edit the `ListenIP` at the top to match your computer's local IP address and start the script. Then LiveLink on your IOS device and enter your computer's local IP address there as well, ensuring that both devices are connected to the same network. And finally, start VSeeFace, check iPhone tracking reciever, set the tracking app to iFacialMocap, and enter your computer's local IP in the field.
