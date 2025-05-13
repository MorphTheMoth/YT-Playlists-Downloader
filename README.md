# YT-Playlists-Downloader
Download or syncs youtube playlists as audio files to a folder tree in your pc

You need https://github.com/yt-dlp/yt-dlp .exe file in the same folder, or in your PATH, and a google API key.

The program will create subfolders for each playlist you want to download, you can change the extension to .pyw and run this on startup to keep the playlist synced with youtube, it will not delete already downloaded songs in case they get removed from youtube. You can edit the blacklist.txt file with any word you want, and any video that cointains that word will not be downloaded.

Edit the file with any playlist id you want to download, its the part at the end of the url : `https://www.youtube.com/playlist?list=[PlaylistID]`.
