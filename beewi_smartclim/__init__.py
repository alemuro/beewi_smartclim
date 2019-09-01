""" Beewi Smartclim Poller used by Home Assistant """ 

from datetime import datetime, timedelta
import logging
from btlewrap.base import BluetoothInterface, BluetoothBackendException

_LOGGER = logging.getLogger(__name__)

class BeewiSmartClimPoller:
    """This class will interact with the sensor and aggregates all data."""

    def __init__(self, mac):
        """Initialize the Poller."""
        try:
            from btlewrap import BluepyBackend

            backend = BluepyBackend
        except ImportError:
            from btlewrap import GatttoolBackend

            backend = GatttoolBackend

        self._backend = backend
        self._mac = mac
        self._temp = None
        self._humidity = None
        self._battery = None
        self._last_update = None

        _LOGGER.debug("MiTempBtSensorPoller initiated with backend %s", self._backend)

    def get_temperature(self):
        """ Return temperature readed from the sensor. """
        if (self._last_update is None) or (
            datetime.now() - timedelta(minutes=3) > self._last_update
        ):
            self.update_sensor()
        else:
            _LOGGER.debug("Serving data from cache")
        
        return self._temp

    def get_humidity(self):
        """ Return humidity readed from the sensor. """
        if (self._last_update is None) or (
            datetime.now() - timedelta(minutes=3) > self._last_update
        ):
            self.update_sensor()
        else:
            _LOGGER.debug("Serving data from cache")

        return self._humidity

    def get_battery(self):
        """ Return battery readed from the sensor. """
        if (self._last_update is None) or (
            datetime.now() - timedelta(minutes=3) > self._last_update
        ):
            self.update_sensor()
        else:
            _LOGGER.debug("Serving data from cache")
            
        return self._battery

    def update_sensor(self):
        """
        Get data from device.

        This method reads the handle 0x003f that contains temperature, humidity
        and battery level.
        """
        bt_interface = BluetoothInterface(self._backend, "hci0")

        try:
            with bt_interface.connect(self._mac) as connection:
                raw = connection.read_handle(0x003F)  # pylint: disable=no-member

            if not raw:
                raise BluetoothBackendException("Could not read 0x003f handle")

            raw_bytes = bytearray(raw)

            temp = int.from_bytes(raw_bytes[1:3], "little") / 10.0
            if temp >= 32768:
                temp = temp - 65535

            humidity = int(raw_bytes[4])
            battery = int(raw_bytes[9])

            self._temp = temp
            self._humidity = humidity
            self._battery = battery
            self._last_update = datetime.now()

            _LOGGER.debug("%s: Find temperature with value: %s", self._mac, self._temp)
            _LOGGER.debug("%s: Find humidity with value: %s", self._mac, self._humidity)
            _LOGGER.debug("%s: Find battery with value: %s", self._mac, self._battery)
        except BluetoothBackendException:
            return
