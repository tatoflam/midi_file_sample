import sys
from mido import MidiFile

#mid = MidiFile('new_song.mid')
mid = MidiFile(sys.argv[1])

print(mid.ticks_per_beat)
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)
#        print(msg.dict()) 
