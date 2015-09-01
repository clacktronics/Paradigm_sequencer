# Paradigm Sequencer

## PyBoard
This is the program written for sequencing LED's in a very specific way. It uses the Micro Python pyBoard device reading sequences in text files. Each LED is controlled by its own PWM clock so that both pitch and PWM can be set for each output individually.

It crudley syncs with Raspberry Pi video by waiting for 4 specified inputs to go high before running this allows the 4 Raspberry Pi's to tell it that all the videos are loaded and ready. This could be done over networking but it was much simpler to attache all of them together down a single ribbon cable rather than use a hub.

## PCB 

The PCB takes the pinout from the Pyboard and connects the 4 wait pins and power to a RPi compatable header. It also has 8 FETs to drive 8 LED strips.

Both 12v and 5v need to be supplied to the board, this can be done using a simple buck-boost converter or a  fixed 12>5v converter (these are typically supplied for use in cars)

## Raspberry Pi's

Theese use my Pisign python module which controls OMXPlayer, when the video is ready it simply goes high.