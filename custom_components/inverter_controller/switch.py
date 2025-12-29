from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.device_registry import DeviceInfo
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add):
    async_add([InverterSwitch(hass.data[DOMAIN][entry.entry_id])])

class InverterSwitch(SwitchEntity):
    def __init__(self, coord):
        self.coord, self._attr_name, self._attr_is_on = coord, "Inverter Controller Enabled", True
        self._attr_unique_id = f"{coord.config_entry.entry_id}_enabled"
        self._attr_device_info = DeviceInfo(identifiers={(DOMAIN, coord.config_entry.entry_id)}, name="Inverter Controller")
    async def async_turn_on(self, **kwargs): self.coord.enabled = self._attr_is_on = True
    async def async_turn_off(self, **kwargs): self.coord.enabled = self._attr_is_on = False