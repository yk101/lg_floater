from collections import deque
from lib.sensor import Sensor

class Altimeter(Sensor):
    def __init__(self, name, avg_samples, log):
        super().__init__(name, avg_samples)
        # self.avg_samples = avg_samples
        self.log = log

        self.distance = deque(maxlen=self.avg_samples)
        self.confidance = deque(maxlen=self.avg_samples)

        self._queues_are_full = False
        self.log.write("Temperature controller was initialized successfully\n")

    def add_sample(self, sample_arr):
        # if len(sample_arr) != 2:
            # return

        # sample_id = sample_arr[0].lower()
        # sample_val = float(sample_arr[1])

        self.distance.append(sample_arr)

    def add_confidance(self, sample):
        # TODO:// try except prase
        self.confidance.append(float(sample))

        # self.log.write("Added temperature sample: {}\n".format(str(sample_arr)))

        # We can start using the samples once:
        #       We received data from all temperature sensors
        #       We received enough samples from all sensors
        # if not self._queues_are_full:
        #     if len(self.t1) == self.avg_samples and \
        #             len(self.t2) == self.avg_samples and \
        #             len(self.t3) == self.avg_samples and \
        #             len(self.t4) == self.avg_samples:
        #         self._queues_are_full = True

    def getLast(self):
        if len(self.distance)>0:
            return self.distance[0]
        print(f"{self.getName()} buffer empty")
        return 0


    def getConfidance(self):
        if len(self.confidance)>0:
            return self.confidance[0]
        print(f"{self.getName()} buffer empty")
        return 0