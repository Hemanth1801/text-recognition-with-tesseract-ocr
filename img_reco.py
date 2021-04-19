import cv2
import pytesseract
from PIL import ImageGrab
import tkinter as tk
from tkinter.filedialog import  asksaveasfilename

def scan_clipboard():
    imge = ImageGrab.grabclipboard()
    imge.save('image.png', 'PNG')
    img = cv2.imread('image.png')
    return img
def i2tconvert(img):
    img = scan_clipboard()
    #img = get_grayscale(img)
    # img=tresholding(img)
    # img=remove_noise(img)

    my_file = open("test_file.txt", "w")
    my_file.write(ocr_core(img))

    print(ocr_core(img))
    cv2.imshow('img', img)
    cv2.waitKey(800)
    cv2.destroyAllWindows()

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text
def open_file():
    """Open a file for editing."""
    filepath = 'R:/text_recognition/test_file.txt'
    i2tconvert(scan_clipboard())
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"text recognition - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"text recognition - {filepath}")



def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image,5)
def tresholding(image):
    return cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
window = tk.Tk()
window.title("text recognition")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="scan", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
#--------------------------------------------------------------

window.mainloop()