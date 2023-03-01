
class CheckBanInfoRsDto:
    reason_commonly_reported = ""
    number_times_reported = 0
    number_games_reported = 0

    def __init__(self, reason_commonly_reported, number_times_reported, number_games_reported):
        self.reason_commonly_reported = reason_commonly_reported
        self.number_games_reported = number_games_reported
        self.number_times_reported = number_times_reported

