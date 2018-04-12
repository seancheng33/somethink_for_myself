'''
python极客项目编程一书的第一个练习。根据iTunes的播放列表统计数据。
'''
import plistlib
import numpy as np
from matplotlib import pyplot


def findDuplicates(fileName):
    print('Finding duplicate traces in %s ...' % fileName)
    # read in a playlist
    plist = plistlib.readPlist(fileName)
    # get the tracks from the Tracks dictionary
    tracks = plist['Tracks']
    # create a track name dictionary
    trackNames = {}
    # iterate through the tracks
    for trackId, track in tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time']
            # look for existing entries
            if name in trackNames:
                # if a name and duration match. increment the count
                # round the track length to the nearest second
                if duration//1000 == trackNames[name][0]//1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration, count+1)
            else:
                # add dictionary entry as tuple (duration,count)
                trackNames[name] = (duration, 1)
        except:
            # ignore
            pass

    dups = []
    for k, v in trackNames.items():
        if v[1] > 1:
            dups.append((v[1], k))
    # save duplicates to a file
    if len(dups) > 0:
        print('Found %d duplicates. Track names saved to dup.txt' % len(dups))
    else:
        print('No duplicate tracks found!')
    with open('dups.txt', 'w', encoding='utf-8') as f:
        for val in dups:
            f.write('[%d] %s\n' % (val[0], val[1]))

def findCommonTracks(fileNames):
    # a list of sets of track names
    trackNameSets = []
    for fileName in fileNames:
        # create a new set
        trackNames = set()
        # read in platlist
        plist = plistlib.readPlist(fileName)
        # get the tracks
        tracks = plist['Tracks']
        # iterate through the tracks
        for trackId, track in tracks.items():
            try:
                # add the track name to a set
                trackNames.add(track['Name'])
            except:
                # ignore
                pass
        # add to list
        trackNameSets.append(trackNames)
        # get the set of common tracks
        commonTracks = set.intersection(*trackNameSets)
        # write to file
        if len(commonTracks) > 0:
            with open('common.txt', 'w', encoding='utf-8') as f:
                for val in commonTracks:
                    s = "%s\n" % val
                    f.write(s)
            print('%d common tracks found. Track names written to common.txt' % len(commonTracks))
        else:
            print('No common tracks!')

def plotStats(fileName):
    # read in a playlist
    plist = plistlib.readPlist(fileName)
    # get the tracks from the playlist
    tracks = plist['Tracks']
    # create lists of song ratings and track durations
    ratings = []
    durations = []
    # iterate through the tracks
    for trackId, track in tracks.items():
        try:
            ratings.append(track['Album Rating'])
            durations.append(track['Total Time'])
        except:
            # ignore
            pass
    if ratings == [] or durations == []:
        print('No valid Album Rating/Total Time data in %s.' % fileName)
        return
    x = np.array(durations, np.int32)
    x = x/60000.0
    y = np.array(ratings, np.int32)
    pyplot.subplot(2, 1, 1)
    pyplot.plot(x, y, 'o')
    pyplot.axis([0, 1.05*np.max(x), -1, 110])
    pyplot.xlabel('Track duration')
    pyplot.ylabel('Track rating')

    # plot histogram
    pyplot.subplot(2, 1, 2)
    pyplot.hist(x, bins=20)
    pyplot.xlabel('Track duration')
    pyplot.ylabel('Count')

    # show plot
    pyplot.show()

def main():
    findCommonTracks(['test-data/pl1.xml','test-data/rating.xml','test-data/pl1.xml'])
    # plotStats('test-data/rating.xml')
    # findDuplicates('test-data/rating.xml')

if __name__ == '__main__':
    main()