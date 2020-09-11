import sys
from mido import MidiFile, tick2second

mid = MidiFile(sys.argv[1])
tempo = 500000 #microseconds per beat(120BPM)

print('Ticks per beat: {}'.format(mid.ticks_per_beat))

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if msg.type == 'set_tempo':
            tempo = msg.tempo
            print('Tempo is changed to {}'.format(tempo))
        if msg.time > 0:
            delta = tick2second(msg.time, mid.ticks_per_beat, tempo)
        else:
            delta = 0

#        print(msg)
        if msg.type == 'note_on':
            print('MIDI note:{}, time:{}, delta_sec:{}'.format(msg.note, msg.time, delta))

