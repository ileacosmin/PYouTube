import os
import tkinter
import customtkinter
from pytube import YouTube
from tkinter import ttk
from tkinter import filedialog

def startDownload():
    try:
        progressBar.set(0)
        pPercentage.configure(text='0%')

        ytlink=link.get()
        ytObj=YouTube(ytlink, on_progress_callback=on_progress)
        video=ytObj.streams.get_highest_resolution()

        title.configure(text=ytObj.title,text_color='white')


        download_path = os.path.expanduser(folder)


        video.download(download_path)

    except Exception as e:
        print(f'Error: {e}')
        finishLabel.configure(text='Youtube link is invalid',text_color="red")
    else:
        finishLabel.configure(text='Downloaded',text_color='green')

def startDownload_mp3():
    try:
        progressBar.set(0)
        pPercentage.configure(text='0%')

        ytlink=link.get()
        ytObj=YouTube(ytlink,  on_progress_callback=on_progress)
        audio_stream = ytObj.streams.get_audio_only()
        print(folder)
        title.configure(text=ytObj.title,text_color='white')


        download_path = os.path.expanduser(folder)

        audio_stream.download(download_path)

    except Exception as e:
        print(f'Error: {e}')
        finishLabel.configure(text='Youtube link is invalid',text_color="red")
    else:
        finishLabel.configure(text='Downloaded',text_color='green')


def on_progress(stream, chunk, bytes_remaining):
    total_size=stream.filesize
    bytes_downloaded=total_size-bytes_remaining
    percentage_of_completion=bytes_downloaded/total_size*100;
    per=str(int(percentage_of_completion))
    pPercentage.configure( text=per+'%')
    pPercentage.update()

    # update progress bar
    progressBar.set(float(percentage_of_completion/100))


# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#our app frame
app = customtkinter.CTk()
app.geometry('720x480')
app.title('PYouTube')

# add ui elements
title=customtkinter.CTkLabel(app, text='Insert the youtube link')
title.pack(padx=10,pady=10)

# link input box
url_var=tkinter.StringVar()
link=customtkinter.CTkEntry(app, 350,30,textvariable=url_var)
link.pack()


# finished downlading
finishLabel=customtkinter.CTkLabel(app, text='')
finishLabel.pack()

#progress percentage
pPercentage=customtkinter.CTkLabel(app, text='0%')
pPercentage.pack()

progressBar=customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10,pady=10)


# add the download buttons
download_mp4 = customtkinter.CTkButton(app, text="Download MP4", command=startDownload)
download_mp4.pack()

download_mp3=customtkinter.CTkButton(app, text="Download MP3",command=startDownload_mp3)
download_mp3.pack(padx=10,pady=10)



folder=''
showFolderPath=customtkinter.CTkLabel(app,text=folder)
showFolderPath.pack()


def getFolderPath():
    global folder
    folder = filedialog.askdirectory()
    showFolderPath.configure(text=folder)
    showFolderPath.update()


# set the path for the download
btnFind = customtkinter.CTkButton(app, text="Open Folder",command=getFolderPath)
btnFind.pack()


# run app
app.mainloop()
