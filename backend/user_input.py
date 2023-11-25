import cv2 
import time
import shutil
import capture
import train
import database_interaction

# demo enters here
def main():
    """
        :type: N/A
        :rtype: N/A
    """
    names = []
    index = 0
    
    while True:
        fname = input("Your First Name: ")
        lname = input("Your Last Name: ")
        name = fname.lower().strip() + "_" + lname.lower().strip()
        if name in names:
            print("Name already exists.")
            continue
        else:
            label = ""
            while True:
                label = input("Your Label (h for Homeowner, v for Visitor): ")
                if label == "h":
                    label = "Homeowner"
                    break
                elif label == "v":
                    label = "Visitor"
                    break
                else:
                    print("Invalid label provided.")
            
            # edit people.json
            database_interaction.add_person(index, name)
            database_interaction.add_label(index, label)
            
            names.append(name)
            index += 1
            
            cam = cv2.VideoCapture(0)
            start = time.time()
            images_count = 0
            print("Taking photos ...")
            while True:
                if images_count == 15:
                    break
                end = time.time()
                diff = end - start
                ret, frame = cam.read()
                if diff >= 3:
                    start = end
                    if not ret:
                        print("Failed read.")
                        continue
                    else:
                        captured = capture.capture(name, frame, images_count)
                        if captured == 1:
                            images_count += 1
            print("Done.")
        
            cam.release()
            cv2.destroyAllWindows()
        
        while True:
            more_people = input("Add More People? (y/n) ")
            if more_people == "y" or more_people == "n":
                break
            else:
                print("Invalid input.")
        
        if more_people == "y":
            continue
        else:
            break
    
    train.train()
    shutil.rmtree("db/imgs")
    
main()
