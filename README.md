# BotControlledByHand
## Description
This project proposes a way to control a robot in the simulator V-REP using Hand Gestures. All the gestures were obtained in
the [1 Million Hand Dataset](https://www-i6.informatik.rwth-aachen.de/~koller/1miohands/]) and used the CNN Topology proposed
by the Inception V1, which the implementation were inspired by the repository [TF-Deephand](https://github.com/neccam/TF-DeepHand).
The gestures used in this project are:

 - ![](https://www-i6.informatik.rwth-aachen.de/~koller/1miohands/Handshape_3_1_1.png): The bot moves foward
 - ![](https://www-i6.informatik.rwth-aachen.de/~koller/1miohands/Handshape_5_1_1.png): The bot moves very fast forward
 - ![](https://www-i6.informatik.rwth-aachen.de/~koller/1miohands/Handshape_7_1_1.png): The bot moves backwards
 - ![](https://www-i6.informatik.rwth-aachen.de/~koller/1miohands/Handshape_6_4_1.png): Stop the bot 
 - ![](https://www-i6.informatik.rwth-aachen.de/~koller/1miohands/Handshape_2_1_1.png): The bot starts to rotate anti-clockwise
 - ![](https://www-i6.informatik.rwth-aachen.de/~koller/1miohands/Handshape_1_1_3.png): The bot starts to rotate clockwise
 - ![](https://www-i6.informatik.rwth-aachen.de/~koller/1miohands/Handshape_4_3_1.png): Freezes the command interpreter
    - If freezed, it will only restart interpret the gestures if you unfreeze
 - ![](https://www-i6.informatik.rwth-aachen.de/~koller/1miohands/Handshape_3_2_1.png): Unfreezes the command interpreter
 
It's possible execute the gestures with both hands. The script starts **FREEZED**, so it's necessary unfreeze it!

## Requirements
 - V-REP: 3.6.1
 - Python: 3.7.2
    - Tensorflow: 1.13.1
    - Numpy: 1.16.2
    - OpenCV: 4.0.0
    
## Run
  - Starts the V-REP and open the file scene.ttt
  - Starts the simulation
  - Run the script run.py and enjoy it
  
## Video

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/X_Z0I6pzNpc/0.jpg)](http://www.youtube.com/watch?v=X_Z0I6pzNpc)

## License
BSD 3-Clause License

Copyright (c) 2019, Bruno Georgevich Ferreira
All rights reserved.
