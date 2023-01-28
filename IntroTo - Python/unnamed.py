import pytube

try:
    link = input("Enter video link: ")
    yt = pytube.YouTube(link)
    stream_list = yt.streams.filter(progressive=True)
    for i, stream in enumerate(stream_list):
        print(i+1, ". ", stream)
    user_choice = int(input("Enter the number of the quality you want to download: "))
    chosen_stream = stream_list[user_choice-1]
    chosen_stream.download()
    print("Downloaded Successfully")
    print("Thanks for using our video downloader")
except Exception as e:
    print(e)
