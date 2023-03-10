"""The tessla component."""

DOMAIN = "tessla"


async def async_setup(hass, config):
    """Set up the Tessla component."""
    hass.async_create_task(
        hass.helpers.discovery.async_load_platform("sensor", DOMAIN, {}, config)
    )

    return True
