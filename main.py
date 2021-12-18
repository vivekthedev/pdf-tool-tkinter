import tkinter as tk
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename
from pdffunc import *


def info():
    path = askopenfilename(title="Select File", filetypes=[
                           ("PDF Document", "*pdf")])
    extract_information(path)


def rotate():
    path = askopenfilename(title="Select File", filetypes=[
                           ("PDF Document", "*pdf")])
    rotate_pages(path)


def merge():
    path_A = askopenfilename(title="Select First File", filetypes=[
        ("PDF Document", "*pdf")])
    path_B = askopenfilename(title="Select Second File", filetypes=[
        ("PDF Document", "*pdf")])

    merge_pdfs(path_A, path_B)


def split():
    path = askopenfilename(title="Select File", filetypes=[
                           ("PDF Document", "*pdf")])

    def assign():
        ranges = Range.get()
        pdf_split(path, ranges)
        newWindow.destroy()

    newWindow = tk.Toplevel(root)
    newWindow.title('Enter Split Ranges')
    newWindow.geometry('400x200')
    newWindow.rowconfigure([0, 1, 2], minsize=50)
    newWindow.columnconfigure([0], minsize=400)
    labelh = tk.Label(newWindow, text="Enter Split Ranges and Press GO")
    labelE = tk.Label(
        newWindow, text="Eg: 1-23 and 24-36 can be written as 23")
    labelh.grid(row=0, column=0)
    labelE.grid(row=1, column=0)
    container = tk.Frame(newWindow)
    container.columnconfigure([0, 1], minsize=200)
    container.rowconfigure([0], minsize=50)
    Range = tk.Entry(container)
    submit = tk.Button(container, text="GO", command=assign)
    Range.grid(row=0, column=0)
    submit.grid(row=0, column=1, padx=10, pady=10)
    container.grid(row=2, column=0)


def watermark():
    path = askopenfilename(title="Select File", filetypes=[
                           ("PDF Document", "*pdf")])
    pathW = askopenfilename(title="Select Watermark File", filetypes=[
                           ("PDF Document", "*pdf")])
    create_watermark(path, pathW)


def encrypt():
    path = askopenfilename(title="Select File", filetypes=[
                           ("PDF Document", "*pdf")])

    def assign():
        passwordText = password.get()
        add_encryption(path, passwordText)
        newWindow.destroy()

    newWindow = tk.Toplevel(root)
    newWindow.title('Create Password')
    newWindow.geometry('400x200')

    newWindow.rowconfigure([0, 1], minsize=100)
    newWindow.columnconfigure([0], minsize=400)
    label1 = tk.Label(
        newWindow, text="Create a Strong password to encrypt PDF")
    label1.grid(row=0, column=0)

    container = tk.Frame(newWindow)
    container.rowconfigure([0], minsize=100)
    container.columnconfigure([0, 1], minsize=200)
    password = tk.Entry(container)
    submit = tk.Button(container, text="Encrypt", command=assign)
    password.grid(row=0, column=0)
    submit.grid(row=0, column=1)
    container.grid(row=1, column=0)


root = tk.Tk()
root.geometry('800x600')
root.wm_title('PDF Utility Tool')

fontStyle = tkFont.Font(size=42)
btnText = tkFont.Font(size=12)


root.columnconfigure(0, minsize=800)
root.rowconfigure(0, minsize=200)
root.rowconfigure(1, minsize=400)

label1 = tk.Label(text='PDF Utility Tool', font=fontStyle,
                  borderwidth=2, relief="groove")
label1.grid(row=0, column=0)

container = tk.Frame(root)

container.columnconfigure([0, 1], minsize=300)
container.rowconfigure([0, 1, 2], minsize=100)

btn_merge = tk.Button(container, text='Merge', bg='#FFE882',
                      padx=15, pady=15, width=9, height=2, command=merge)
btn_rotate = tk.Button(container, text='Rotate',
                       bg='#FFE882', padx=15, pady=15, width=9, height=2, command=rotate)
btn_split = tk.Button(container, text='Split', bg='#FFE882',
                      padx=15, pady=15, width=9, height=2, command=split)
btn_watermark = tk.Button(container, text='Watermark',
                          bg='#FFE882', padx=15, pady=15, width=9, height=2, command=watermark)
btn_encrypt = tk.Button(container, text='Encrypt',
                        bg='#FFE882', padx=15, pady=15, width=9, height=2, command=encrypt)
btn_extract = tk.Button(container, text='Extract Info',
                        bg='#FFE882', padx=15, pady=15, width=9, height=2, command=info)

btn_merge.grid(row=0, column=0)
btn_rotate.grid(row=0, column=1)
btn_split.grid(row=1, column=0)
btn_watermark.grid(row=1, column=1)
btn_encrypt.grid(row=2, column=0)
btn_extract.grid(row=2, column=1)

container.grid(row=1, column=0)

root.mainloop()
