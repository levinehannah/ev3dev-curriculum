import ev3dev.ev3 as ev3
import time
import robot_controller as robo
import math

def main():

   play_Sandstorm()

def play_Sandstorm():

    play_note(440, 1, 80, 160)
    play_note(440, 5, 40, 80)
    play_note(440, 1, 80, 160)
    play_note(587.33, 6, 40, 80)
    play_note(587.33, 1, 80, 160)
    play_note(523.25, 6, 40, 80)
    play_note(523.25, 1, 80, 160)
    play_note(392, 1, 80, 160)

    play_note(440, 4, 40, 80)
    play_note(440, 1, 80, 160)
    play_note(440, 5, 40, 80)
    play_note(440, 1, 80, 160)
    play_note(587.33, 2, 40, 80)

    play_note(440, 4, 40, 80)
    play_note(440, 1, 80, 160)
    play_note(440, 5, 40, 80)
    play_note(440, 1, 80, 160)
    play_note(587.33, 2, 40, 80)

    play_note(440, 2, 40, 80)
    play_note(440, 2, 80, 160)
    play_note(440, 4, 40, 80)
    play_note(440, 1, 80, 160)
    play_note(523.25, 1, 160, 320)

    play_note(440, 2, 40, 80)
    play_note(440, 2, 80, 160)
    play_note(440, 4, 40, 80)
    play_note(440, 1, 80, 160)
    play_note(523.25, 2, 80, 160)

    play_note(440, 2, 40, 80)
    play_note(440, 2, 80, 160)
    play_note(440, 4, 40, 80)
    play_note(440, 2, 80, 160)
    play_note(587.33, 4, 40, 80)
    play_note(587.33, 2, 80, 160)

    play_note(523.25, 4, 40, 80)
    play_note(523.25, 2, 80, 160)
    play_note(392, 1, 80, 160)

    play_note(440, 2, 40, 80)
    play_note(440, 2, 80, 160)
    play_note(440, 4, 40, 80)
    play_note(440, 1, 80, 160)
    play_note(523.25, 2, 80, 160)

    play_note(440, 2, 40, 80)
    play_note(440, 2, 80, 160)
    play_note(440, 4, 40, 80)
    play_note(440, 1, 80, 160)
    play_note(523.25, 2, 80, 160)

    play_note(440, 2, 40, 80)
    play_note(440, 1, 80, 160)
    play_note(523.25, 2, 80, 160)
    play_note(440, 2, 40, 80)
    play_note(440, 1, 80, 160)
    play_note(523.25, 2, 80, 160)

    play_note(440, 2, 40, 80)
    play_note(440, 1, 80, 160)
    play_note(523.25, 2, 80, 160)
    play_note(440, 2, 40, 80)
    play_note(440, 1, 80, 160)
    play_note(523.25, 2, 80, 160)

    play_note(440, 2, 40, 80)
    play_note(523.25, 1, 80, 160)

    play_note(440, 2, 40, 80)
    play_note(523.25, 1, 80, 160)

    play_note(440, 2, 40, 80)
    play_note(523.25, 1, 80, 160)

    play_note(440, 2, 40, 80)
    play_note(523.25, 1, 80, 160)

    play_note(440, 2, 40, 80)
    play_note(523.25, 1, 80, 160)

    play_note(440, 2, 40, 80)
    play_note(523.25, 1, 80, 160)

    play_note(440, 2, 40, 80)
    play_note(523.25, 1, 80, 160)

    play_note(440, 2, 40, 80)
    play_note(523.25, 1, 80, 160)

    play_note(587.33, 4, 640, 10)

def play_note(frequency,repetition, duration, pause):
    for _ in range(repetition):
        ev3.Sound.tone([(frequency, duration, pause)])

main()