from basePLC import BasePLC
from utils import PLC9_DATA, STATE, PLC9_PROTOCOL
from utils import T7, ENIP_LISTEN_PLC_ADDR, CTOWN_IPS
from decimal import Decimal
import sys
import threading

plc9_log_path = 'plc9.log'


class PLC9(BasePLC):

    def pre_loop(self):
        print 'DEBUG: plc9 enters pre_loop'
        self.local_time = 0
        self.week_index = sys.argv[2]
        self.week_index = 0
        print "Week index in PLC9 is: " + str(self.week_index)

        # Flag used to stop the thread
        self.reader = True
        self.t7 = Decimal(self.get(T7))

        self.lock = threading.Lock()
        tags = [T7]
        values = [self.t7]

        # Used in handling of sigint and sigterm signals, also sets the parameters to save the system state variable
        # values into a persistent file
        BasePLC.set_parameters(self, tags, values, self.reader, self.lock,
                               ENIP_LISTEN_PLC_ADDR, self.week_index)
        self.startup()

    def main_loop(self):
        get_error_counter = 0
        get_error_counter_limit = 100
        while True:
            try:
                with self.lock:
                    self.t7 = Decimal(self.get(T7))
            except Exception:
                get_error_counter += 1
                if get_error_counter < get_error_counter_limit:
                    continue
                else:
                    print("System database is locked, aborting process")
                    exit(0)

            self.local_time += 1


if __name__ == "__main__":
    plc9 = PLC9(
        name='plc9',
        state=STATE,
        protocol=PLC9_PROTOCOL,
        memory=PLC9_DATA,
        disk=PLC9_DATA)