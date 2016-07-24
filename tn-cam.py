# to do list:
# add in checker to make sure that the input name is valid
# make this program postable for r/raspberrypi
# find better note taking program
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

    from picamera import PiCamera # IF THIS IS NOT RUN ON A RASPBERRY PI CAMERA, IT WILL NOT WORK
    from random import random
    # Import the needed modules for the functions to run

    camera = PiCamera()
    # Create instance of Camera

    camera.rotation = 90  # Change this variable if orientation is bad

    picture_name = (str(input('Pick a photo name:\n ')))
    if picture_name == '':
        picture_name = ('pic' + str(random.randint(0, 10000)))
    # If too lazy to type a name, auto assign one named pic, plus some number between 0 and 10,000

    # # Be sure to add in a thing that will remove spaces

    picture_numerator = 0  # user input variable that asks for how many pictures to be taken.
    while True:
        picture_numerator = (int(input('How many photos?:\n ')))  # Ask user input for how many photos
        if picture_numerator == '':
            picture_numerator = 3  # Default is 3 pictures
        elif picture_numerator <= 0:
            continue
        break

    # # Make sure to add a thing that checks if the input is an integer

    picture_numerator_counter = 0  # Variable for determining number of pics taken
    camera.start_preview()  # Turn the preview window on, note that this takes up the entire screen.
    sleep(2)  # preview for two seconds before taking a picture

    while picture_numerator_counter < picture_numerator:
        sleep(2)
        camera.capture(picture_name + str(picture_numerator_counter) + '.jpg')
        picture_numerator_counter += 1
    # Sleep, take a pic, save, increase the number counter of pics taken

    camera.stop_preview()
    # Stop cam preview

pic_capture()


