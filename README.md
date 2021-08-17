# Last song parameter - Streamlabs Twitch bot script

This package contains a script for the Streamlabs chatbot that adds the ability
to request the last requested song.

## Installation

In order to download the latest version of this script, go to the 
(releases of this package)[https://github.com/mfrankruijter/LastSongParameter/releases/latest] 
and click on the `Source code (zip)` button. This will download the codebase 
of the script. Unpack this ZIP. Go into the unpacked folder, there should be a 
`README.md` file. In that same folder there should be a `LastSongParameter` 
folder. This folder should be zipped again. On Windows 10 the following steps
can be done: 
- Right click on the folder.
- Open the menu, copy to.
- Click on the Zipped folder option.

The resulting ZIP is the package that needs to be imported in the following 
step.

In order to use this script, Python (2.7) must be installed on the same system
that the bot is running on. For the exact documentation please see
[the original documentation](https://cdn.streamlabs.com/chatbot/Documentation_Twitch.pdf)
Import the ZIP file from this repository under the `Scripts` section of your
chatbot. If the scripts section is not available, try to reconnect
`Twitch Streamer` and `Twitch Bot` under the connection tab, under the profile
icon in the bottom left corner.

## Usage

When the script is installed, click on the entry in the scripts tab and add the
path where the three new text files should be stored (so without the file names). 
The most logical path can be found when clicking on the `?` on the top right of StreamLabs 
ChatBot click on Open Install Directory and then navigate from there to 
`Services > Twitch > Files`. Because this is where other related files are stored aswell.
These can be imported to display additional information on stream. The files 
that will become available after the first song in SongRequest has been played 
will be:
- lastSong.txt - Contains just the song name.
- lastSongRequested.txt - Contains the song name + the requester name.
- lastSongRequester.txt - Contains just the requester name.

In a command, the following variables will become available:
- $lastsong - Contains just the song name.
- $lastsongrequested - Contains the song name + the requester name.
- $lastsongrequester - Contains just the requester name.

The script will replace these variables with `N/A` when they are empty.

## Feedback

Feedback for this package can be provided through issues, or by creating a pull
request with a fix or improvement.

## References

- [StreamLabs Chatbot](https://streamlabs.com/chatbot)

## MIT License

Copyright (c) Marcel Frankruijter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.