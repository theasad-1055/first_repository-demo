"""
Image Loader and Viewer using OpenCV.
This script loads an image from any PC location, displays it in a fixed-size window,
and allows the user to view, save, or convert it to grayscale.
"""

import cv2
import os

# Step 1: Choose source
path = input("Enter the image name or full path: ").strip('"').strip("'")  # remove extra quotes if pasted
path = os.path.normpath(path)  # normalize slashes for your OS
image = cv2.imread(path)

# Step 2: Process image if loaded
if image is not None:
    choose = input("Show 'original' or 'gray_color'? Enter 'first' or 'second': ")

    if choose == 'second':
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print("Options: 'show', 'save', or 'both'")
        task = input("Enter task: ")

        if task == 'show':
            cv2.namedWindow("Gray Image", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Gray Image", 800, 600)
            cv2.imshow("Gray Image", gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif task == 'save':
            file_name = input("Enter filename (e.g., output.png): ")
            cv2.imwrite(file_name, gray)
            print(f"Image '{file_name}' saved.")

        elif task == 'both':
            cv2.namedWindow("Gray Image", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Gray Image", 800, 600)
            cv2.imshow("Gray Image", gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            file_name = input("Enter filename (e.g., output.png): ")
            cv2.imwrite(file_name, gray)
            print(f"Image '{file_name}' saved.")
        else:
            print("Invalid choice.")

    elif choose == 'first':
        print("Options: 'show', 'save', or 'both'")
        task = input("Enter task: ")

        if task == 'show':
            cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Original Image", 800, 600)
            cv2.imshow("Original Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif task == 'save':
            file_name = input("Enter filename (e.g., output.png): ")
            cv2.imwrite(file_name, image)
            print(f"Image '{file_name}' saved.")

        elif task == 'both':
            cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Original Image", 800, 600)
            cv2.imshow("Original Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            file_name = input("Enter filename (e.g., output.png): ")
            cv2.imwrite(file_name, image)
            print(f"Image '{file_name}' saved.")
        else:
            print("Invalid choice.")

    else:
        print("Please enter 'first' or 'second'.")
else:
    print("Could not load the image. Check your path or file exists.")
