# to do list:
# add in checker to make sure that the input name is valid
# make this program postable for r/raspberrypi
# find better note taking program
# put notes in cloud
# sync notes and pictures together in same program
# setup GUI for notes program
# setup email packager for files
# text and email notifier
# setup scheduler
# Main menu (c = camera), (e = email) (t = text)
#         s = scheduler, w = word typer
# save all these to a notes folder and allow notes to be emailed
# combine all this into a desktop icon that I can click and go with
# -----------------------

def pic_capture():

    # All-Purpose camera taking function

    from picamera import PiCamera
    from time import sleep
    import random
    # Import the needed modules for the functions to run

    camera = PiCamera()
    # Create instance of Camera

    camera.rotation = 90 # Change this variable if orientation is bad

    picname = (str(input('Pick a photo name:\n ')))
    if picname == '':
        picname = ('pic' + str(random.randint(0, 10000)))

    # If too lazy to type a name, auto assign one named pic
    # plus some number between 0 and 10,000
    # Add in a thing that will remove spaces
    # Ask user input for how many photos

    while True:
        picture_numerator = (int(input('How many photos?:\n ')))
        if picture_numerator == '':
            picture_numerator = 3
        elif picture_numerator <= 0:
            continue
        break
    # If lazy, default is 3
    # Make sure to add a thing that checks if the input is an integer

    # Sleep allows for better camera positioning
    picture_numerator_counter = 0
    # Variable for determining number of pics taken
    camera.start_preview()
    sleep(2)
    # Start camera preview
    while picture_numerator_counter < picture_numerator:  # @UndefinedVariable
        sleep(2)
        camera.capture(picname + str(picture_numerator_counter) + '.jpg')
        picture_numerator_counter += 1
    # Sleep, take a pic, save, increase the number counter of pics taken
    camera.stop_preview()
    # Stop cam preview

pic_capture()
