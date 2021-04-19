class FYI:
    def __init__(self, log):
        self.log = log
        self.log.write("FYI controller was initialized successfully\n")


    def add_sample(self, sample):
        sample_arr = sample.split(":")
        if len(sample_arr) != 2:
            return

        sample_id = sample_arr[0].lower()
        sample_val = float(sample_arr[1])

        if sample_id == "pu": #pump on|off
            if bool(sample_val):
                self.log.write("FYI: Pump is on\n")
            else:
                self.log.write("FYI: Pump is off\n")

        elif sample_id == "cu": #berez on|off
            if bool(sample_val):
                self.log.write("FYI: Berez is on\n")
            else:
                self.log.write("FYI: Berez is off\n")

        elif sample_id == "ir": #iridium on|off
            if bool(sample_val):
                self.log.write("FYI: Iridium is on\n")
            else:
                self.log.write("FYI: Iridium is off\n")

        else:
            return








