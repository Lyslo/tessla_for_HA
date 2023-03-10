"""Platform for Tessla custom sensors."""
import logging

from homeassistant.const import CONF_NAME
from homeassistant.const import CONF_SENSORS
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    # get the list of sensors from the config
    sensors = config.get(CONF_SENSORS, [])

    # create a list of TesslaSensor instances with unique names
    entities = [TesslaSensor(sensor["name"]) for sensor in sensors]

    # add the entities to Home Assistant
    async_add_entities(entities)


class TesslaSensor(Entity):
    """Representation of a Tessla sensor."""

    def __init__(self, name):
        """Initialize the sensor."""
        self._name = name
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unique_id(self):
        # generate a unique entity ID using the name
        return f"tessla_{self._name.lower().replace(' ', '_')}"

    async def async_update(self):
        """Fetch new state data for the sensor."""
        # Update your sensor state here

        self._state = 999999  # Example state
