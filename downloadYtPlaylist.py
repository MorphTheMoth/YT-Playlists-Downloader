from pyyoutube import Api
import os, threading, subprocess, re

api = Api(api_key="             YOUR GOOGLE API KEY               ")  # https://developers.google.com/youtube/v3/getting-started

folders = {
    # "PlaylistId" : "Folder Name",
    "PLvjIcEZWPuf_OIVwg5f-uYpz4AsozpSW7" : "Girls Band Cry",
    "PLPqVb_3u9vSPmC_LA5IbAxVsxcJ2YZWwg" : "KAF - Solo",
    "PLmOldskd2VbL7_t-NE9p6rEboq_v0AHko" : "hollow knight ost",
    "" : "",
    "" : "",
    "" : "",
}

sinfo = subprocess.STARTUPINFO()
sinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

blacklist = None
with open("blacklist.txt", "r", encoding="utf-8") as txt_file:
    blacklist = "--".join(txt_file.readlines())

for id, folderName in folders.items():
    if id == "": break
    print(f"\n\n--{folderName}--\n\n")
    path = os.path.join(os.getcwd(), folderName)

    if not os.path.isdir(path): os.mkdir(path)

    for file in os.listdir(path):
        if blacklist.find(os.path.splitext(file)[0])!=-1 or os.path.splitext(file)[0].find('.')!=-1:
            print(f"Deleting: {file}")
            os.remove(f"{path}\\{file}")

    songsInFolder = "".join(os.listdir(path))

    for song in api.get_playlist_items(playlist_id=id, count=None).items:

        if song.snippet.title == "Private video": continue
        title = re.sub(r'([\/:*?"><|.#])', '', song.snippet.title)  #cant use these chars for files in widows
        if blacklist.find(title) != -1:
            print(f"{title} is in blacklist")
            continue

        if songsInFolder.find(title) == -1:
            print(f"\n -NOT FOUND: {title}\n")
            try:
                result = subprocess.run(['yt-dlp.exe', f'https://www.youtube.com/watch?v={song.contentDetails.videoId}', '-x', '--embed-thumbnail', '--embed-metadata', '-P', path, '-o', f'{song.snippet.channelTitle.replace('.', '')} - {title}'], check=True, capture_output=True, text=True, startupinfo=sinfo)
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                print(f"Error: {e.stderr}")
