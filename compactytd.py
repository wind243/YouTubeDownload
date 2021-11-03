from pytube import YouTube
YouTube(input("Enter the YouTube URL: ")).streams.filter(file_extension='mp4').get_by_itag(18).download(filename = input("What do you want to name your file? ") + ".mp4", output_path = "downloads")
print("Done!")