from PIL import Image
import os

ascii_chars = ["#", "@", "%", "*", "+", "=", "-", ":", ".", " "]

# Resize image
def ResizeImage(image, new_width=200):
    width, height = image.size
    ratio = height // width
    new_height = new_width * ratio
    return image.resize((new_width, new_height))

# Convert to grayscale
def ConvertToGrayscale(image):
    return image.convert("L")

# Read pixels
def PixelsToAscii(image):
    pixels = list(image.getdata())
    ascii_string = "".join([ascii_chars[pixel // 32] for pixel in pixels])
    img_width = image.width
    ascii_image = "\n".join([ascii_string[index:index + img_width] for index in range(0, len(ascii_string), img_width)])
    return ascii_image
    
# Return ASCII Image
def ImgToAscii(path):
    # Tries to open the image
    try:
        image = Image.open(path)
    except:
        print("INVALID PATH!")
        return
    # Tries to convert the image to ascii
    try:
        ascii_image = PixelsToAscii(ConvertToGrayscale(ResizeImage(image)))
        return ascii_image
    except ValueError as ve:
        print(str(ve).upper())

def saveImageText(ascii_image):
    while True:
        option = input("DO YOU WANT TO TURN IT INTO A .TXT FILE? y/n").upper()
        if(option == "Y"):
            try:
                with open("asci_image.txt", "a") as file:
                    file.write(ascii_image)
            except:
                print("CANNOT SAVE THE ASCII IMAGE")
            print("ASCII IMAGE SAVED")
            break
        elif option == "N":
            return
        else:
            pass

if __name__ == "__main__":
    path = input("TYPE THE IMAGE'S PATH:")
    ascii_image = ImgToAscii(path)
    if ascii_image:
        os.system("cls||clear")
        print(ascii_image)
        saveImageText(ascii_image)