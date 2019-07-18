      
def main():
    varx = int(input("Enter your camera IP address:"))
    if int (varx) >= 0 :
         from object_detection_camera_1 import my_class
         my_class()
    else:
        print ("Invalid number")
   
main()