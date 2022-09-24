from socket import *
from struct import *

ListenIp = "192.168.2.100"
ListenPort = 11111

SendIp = "localhost"
SendPort = 49983

propertyNames = [
    "EyeBlinkLeft",
    "EyeLookDownLeft",
    "EyeLookInLeft",
    "EyeLookOutLeft",
    "EyeLookUpLeft",
    "EyeSquintLeft",
    "EyeWideLeft",
    "EyeBlinkRight",
    "EyeLookDownRight",
    "EyeLookInRight",
    "EyeLookOutRight",
    "EyeLookUpRight",
    "EyeSquintRight",
    "EyeWideRight",
    "JawForward",
    "JawLeft",
    "JawRight",
    "JawOpen",
    "MouthClose",
    "MouthFunnel",
    "MouthPucker",
    "MouthLeft",
    "MouthRight",
    "MouthSmileLeft",
    "MouthSmileRight",
    "MouthFrownLeft",
    "MouthFrownRight",
    "MouthDimpleLeft",
    "MouthDimpleRight",
    "MouthStretchLeft",
    "MouthStretchRight",
    "MouthRollLower",
    "MouthRollUpper",
    "MouthShrugLower",
    "MouthShrugUpper",
    "MouthPressLeft",
    "MouthPressRight",
    "MouthLowerDownLeft",
    "MouthLowerDownRight",
    "MouthUpperUpLeft",
    "MouthUpperUpRight",
    "BrowDownLeft",
    "BrowDownRight",
    "BrowInnerUp",
    "BrowOuterUpLeft",
    "BrowOuterUpRight",
    "CheekPuff",
    "CheekSquintLeft",
    "CheekSquintRight",
    "NoseSneerLeft",
    "NoseSneerRight",
    "TongueOut",
    "HeadYaw",
    "HeadPitch",
    "HeadRoll",
    "LeftEyeYaw",
    "LeftEyePitch",
    "LeftEyeRoll",
    "RightEyeYaw",
    "RightEyePitch",
    "RightEyeRoll"
]

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((ListenIp, ListenPort))
DstAddr = (SendIp,SendPort)
udpClntSock = socket(AF_INET, SOCK_DGRAM)

data_template = "mouthSmile_R-{:d}|"\
            "eyeLookOut_L-{:d}|"\
            "mouthUpperUp_L-{:d}|"\
            "eyeWide_R-{:d}|"\
            "mouthClose-{:d}|"\
            "mouthPucker-{:d}|"\
            "mouthRollLower-{:d}|"\
            "eyeBlink_R-{:d}|"\
            "eyeLookDown_L-{:d}|"\
            "cheekSquint_R-{:d}|"\
            "eyeBlink_L-{:d}|"\
            "tongueOut-{:d}|"\
            "jawRight-{:d}|"\
            "eyeLookIn_R-{:d}|"\
            "cheekSquint_L-{:d}|"\
            "mouthDimple_L-{:d}|"\
            "mouthPress_L-{:d}|"\
            "eyeSquint_L-{:d}|"\
            "mouthRight-{:d}|"\
            "mouthShrugLower-{:d}|"\
            "eyeLookUp_R-{:d}|"\
            "eyeLookOut_R-{:d}|"\
            "mouthPress_R-{:d}|"\
            "cheekPuff-{:d}|"\
            "jawForward-{:d}|"\
            "mouthLowerDown_L-{:d}|"\
            "mouthFrown_L-{:d}|"\
            "mouthShrugUpper-{:d}|"\
            "browOuterUp_L-{:d}|"\
            "browInnerUp-{:d}|"\
            "mouthDimple_R-{:d}|"\
            "browDown_R-{:d}|"\
            "mouthUpperUp_R-{:d}|"\
            "mouthRollUpper-{:d}|"\
            "mouthFunnel-{:d}|"\
            "mouthStretch_R-{:d}|"\
            "mouthFrown_R-{:d}|"\
            "eyeLookDown_R-{:d}|"\
            "jawOpen-{:d}|"\
            "jawLeft-{:d}|"\
            "browDown_L-{:d}|"\
            "mouthSmile_L-{:d}|"\
            "noseSneer_R-{:d}|"\
            "mouthLowerDown_R-{:d}|"\
            "noseSneer_L-{:d}|"\
            "eyeWide_L-{:d}|"\
            "mouthStretch_L-{:d}|"\
            "browOuterUp_R-{:d}|"\
            "eyeLookIn_L-{:d}|"\
            "eyeSquint_R-{:d}|"\
            "eyeLookUp_L-{:d}|"\
            "mouthLeft-{:d}|"\
            "=head#{:3.6f},{:3.6f},{:3.6f},{:3.6f},{:3.6f},{:3.6f}|"\
            "rightEye#{:3.6f},{:3.6f},{:3.6f}|"\
            "leftEye#{:3.6f},{:3.6f},{:3.6f}|"
    
running = True
while running:

    data, addr = sock.recvfrom(1024)
    if (data): 
        your_text = data[-244:]
        
        bufferSize = 4
        i = 0
        asdf = 0
        output = {}
        while i + bufferSize <= len(your_text):
            output[propertyNames[asdf]] = unpack("!f", your_text[i:i + bufferSize])[0]
            i += bufferSize
            asdf += 1

        output
        
        if len(output) > 52:
            for key in output:
                if key.endswith("Pitch") or key.endswith("Yaw") or key.endswith("Roll"):
                    continue
                output[key] = int(output[key] * 100)
            
            data_string = data_template
            data_string = data_string.format(output["MouthSmileRight"],
                                             output["EyeLookOutLeft"],
                                             output["MouthUpperUpLeft"],
                                             output["EyeWideRight"],
                                             output["MouthClose"],
                                             output["MouthPucker"],
                                             output["MouthRollLower"],
                                             output["EyeBlinkRight"],
                                             output["EyeLookDownLeft"],
                                             output["CheekSquintRight"],
                                             output["EyeBlinkLeft"],
                                             output["TongueOut"],
                                             output["JawRight"],
                                             output["EyeLookInRight"],
                                             output["CheekSquintLeft"],
                                             output["MouthDimpleLeft"],
                                             output["MouthPressLeft"],
                                             output["EyeSquintLeft"],
                                             output["MouthRight"],
                                             output["MouthShrugLower"],
                                             output["EyeLookUpRight"],
                                             output["EyeLookOutRight"],
                                             output["MouthPressRight"],
                                             output["CheekPuff"],
                                             output["JawForward"],
                                             output["MouthLowerDownLeft"],
                                             output["MouthFrownLeft"],
                                             output["MouthShrugUpper"],
                                             output["BrowOuterUpLeft"],
                                             output["BrowInnerUp"],
                                             output["MouthDimpleRight"],
                                             output["BrowDownRight"],
                                             output["MouthUpperUpRight"],
                                             output["MouthRollUpper"],
                                             output["MouthFunnel"],
                                             output["MouthStretchRight"],
                                             output["MouthFrownRight"],
                                             output["EyeLookDownRight"],
                                             output["JawOpen"],
                                             output["JawLeft"],
                                             output["BrowDownLeft"],
                                             output["MouthSmileLeft"],
                                             output["NoseSneerRight"],
                                             output["MouthLowerDownRight"],
                                             output["NoseSneerLeft"],
                                             output["EyeWideLeft"],
                                             output["MouthStretchLeft"],
                                             output["BrowOuterUpRight"],
                                             output["EyeLookInLeft"],
                                             output["EyeSquintRight"],
                                             output["EyeLookUpLeft"],
                                             output["MouthLeft"],
                                             -output["HeadPitch"] * 45,
                                             output["HeadYaw"] * 45,
                                             output["HeadRoll"] * 40,
                                             0,
                                             0,
                                             0,
                                             -output["RightEyePitch"],
                                             output["RightEyeYaw"],
                                             output["RightEyeRoll"],
                                             -output["LeftEyePitch"],
                                             output["LeftEyeYaw"],
                                             output["LeftEyeRoll"])
            data_utf8 = data_string.encode('utf-8')
            udpClntSock.sendto(data_utf8,DstAddr)



