import tkinter as tk
import time
import datetime


# First create the window
# Start:
# If the stopwatch had not been running before, starttime is current time
# If it had been running before, add the length of the pause to starttime
#
# Pause:
# Record the start of the pause and the end, pass them onto the start
#
# Reset: Reset the starttime to current time, display 00:00.00

class Stopwatch:
    def __init__(self):
        self.pauseStart = 0
        self.startTime = -1
        self.running = False


    def start(self, label):
        print("Started stopwatch")
        self.updateLabel(label)
        if not self.running:
            if self.startTime == -1:
                self.startTime = time.time()
            else:
                self.startTime += time.time() - self.pauseStart
        self.running = True
    def pause(self):
        print("Paused stopwatch")
        if self.running:
            self.pauseStart = time.time()
            # print(f"PauseStart changed to: {self.pauseStart}")
            self.running = False

    def reset(self):
        print("Reset stopwatch")
        if self.running:
            self.running = False
            self.startTime = -1

    def getCurTime(self):
        if self.running:
            # print(time.time, self.startTime)
            return str(datetime.timedelta(seconds=time.time() - self.startTime))
        else:
            return str(datetime.timedelta(seconds=self.pauseStart-self.startTime))

    def updateLabel(self, label): # Update the label 30 times each second?



    def displayStopwatch(self):
        self.window = tk.Tk()
        self.window.minsize(width=600, height=120)
        timeLabel = tk.Label(self.window, text="00:00.00", font=("Courier", 100))
        startButtom = tk.Button(self.window, text='Start', width=12, height=5, command=lambda: self.start(timeLabel))
        pauseButton = tk.Button(self.window, text='Stop', width=12, height=5, command=lambda: self.pause())
        resetButton = tk.Button(self.window, text="Reset", width=12, height=5, command=lambda: self.reset())
        startButtom.pack(side="left")
        pauseButton.pack(side='left')
        resetButton.pack(side="left")
        timeLabel.pack(side="right")
        self.window.mainloop()




sw = Stopwatch()
sw.displayStopwatch()

# sw.start()
# print(f"Started at: {time.time()}")
# time.sleep(1)
# print("After one second:", sw.getCurTime())
# sw.pause()
# print("Pausing for 2 seconds...")
# time.sleep(2)
# print(f"Slept 2 seconds, stopwatch is:{sw.getCurTime()}")
# sw.start()
# time.sleep(2)
# sw.pause()
# print(f"Final: {sw.getCurTime()}")
#
