import time
from threading import Timer


class ChessClock:
    def __init__(self, initial_time):
        self.initial_time = initial_time
        self.player1_time = initial_time
        self.player2_time = initial_time
        self.active_player = 1
        self.timer = None
        self.on_update = None

    def format_time(self, seconds):
        return time.strftime("%M:%S", time.gmtime(seconds))

    def switch_clock(self, player):
        if self.active_player != player:
            return
        self.stop_timer()
        self.active_player = 1 if player == 2 else 2
        self.start_timer()

    def start_timer(self):
        if self.active_player == 1:
            self.timer = Timer(1, self.decrement_player1_time)
        else:
            self.timer = Timer(1, self.decrement_player2_time)
        self.timer.start()

    def stop_timer(self):
        if self.timer:
            self.timer.cancel()

    def decrement_player1_time(self):
        if self.player1_time > 0:
            self.player1_time -= 1
            self.start_timer()
            if self.on_update:
                self.on_update()

    def decrement_player2_time(self):
        if self.player2_time > 0:
            self.player2_time -= 1
            self.start_timer()
            if self.on_update:
                self.on_update()

    def reset_clocks(self):
        self.stop_timer()
        self.player1_time = self.initial_time
        self.player2_time = self.initial_time
        self.active_player = 1
        if self.on_update:
            self.on_update()
        self.start_timer()
