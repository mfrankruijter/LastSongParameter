import os, sys, json, re, random
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

from Settings_LastSongParameter import LastSongParameterSettings

ScriptName = "LastSongParameter"
Website = "https://github.com/mfrankruijter/LastSongParameter"
Description = "Adds a $lastsong parameter to StreamLabs Chatbot."
Creator = "Marcel Frankruijter"
Version = "1.0.0"

ScriptSettings = LastSongParameterSettings()

def Init():
    global SettingsFile
    SettingsFile = os.path.join(os.path.dirname(__file__), "settings.json")
    global ScriptSettings
    ScriptSettings = LastSongParameterSettings(SettingsFile)
    path = ScriptSettings.TextFilePath.rstrip('/\\')
    global lastSongPath
    lastSongPath = path + '\\lastSong.txt'
    global lastSongPathRequester
    lastSongPathRequester = path + '\\lastSongRequester.txt'
    global lastSongPathRequested
    lastSongPathRequested = path + '\\lastSongRequested.txt'
    global currentSong
    currentSong = ''
    global currentSongRequester
    currentSongRequester = ''
    global lastSong
    lastSong = ''
    global lastSongRequester
    lastSongRequester = ''
    return

def Execute(data):
    return

def Tick():
    song = Parent.GetNowPlaying()
    if (currentSong != song.Key):
        global lastSong
        lastSong = currentSong
        global lastSongRequester
        lastSongRequester = currentSongRequester
        with open(lastSongPath, 'w') as f_out:
            f_out.write(lastSong)
        f_out.close()
        with open(lastSongPathRequester, 'w') as f_out:
            f_out.write(lastSongRequester)
        f_out.close()
        with open(lastSongPathRequested, 'w') as f_out:
            f_out.write(lastSong + ' ' + lastSongRequester)
        f_out.close()
        global currentSong
        currentSong = song.Key
        global currentSongRequester
        currentSongRequester = song.Value
    return

def Parse(parseString, userid, username, targetid, targetname, message):
    if ("$lastsongrequester" in parseString):
        if (lastSongRequester != ''):
            parseString = parseString.replace("$lastsongrequester", lastSongRequester)
        parseString = parseString.replace("$lastsongrequester", 'N/A')
    
    if ("$lastsongrequested" in parseString):
        if (lastSongRequester != '' and lastSong != ''): 
            parseString = parseString.replace("$lastsongrequested", lastSong + ' ' + lastSongRequester)
        parseString = parseString.replace("$lastsongrequested", 'N/A')

    if ("$lastsong" in parseString):
        if (lastSong != ''):
            parseString = parseString.replace("$lastsong", lastSong)
        parseString = parseString.replace("$lastsong", 'N/A')

    return parseString

def ReloadSettings(jsonData):
    ScriptSettings.__dict__ = json.loads(jsonData)
    ScriptSettings.Save(SettingsFile)
    return
