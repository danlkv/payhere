# Welcome! These are some backend tools for PayHere.

# This file explains how to try it / set it up. 


# STEP ONE: SET UP THE VIRTUAL ENVIRONMENT

# Launch the virtual environment by typing in:
# source clarifai/bin/activate

# STEP TWO: USE EITHER THE FACE FINDER OR THE ULTRASOUND EMITTER #


###### FACE FINDER ########


# In order to use the Face recognition library (currently only trained on the Celebrity dataset), we need to import face_find and then generate the predictions
# A sample working script could be:

#from face_find import Face
#predictions = Face("https://cryptobeat.co/pay/musk.png").predict()
#print(predictions)



###### ULTRASOUND EMITTER ########


# You have to run (of course, replacing the user id):
# python3 quietnet/send_file.py ENCRYPTED_USER_USERID_TO_TRANSMIT