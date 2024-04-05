from __future__ import annotations

import asyncio
from collections.abc import Iterable, Sequence
from homeassistant.components.camera import Camera
import logging

from pysmartthings import Attribute, Capability

from homeassistant.components.camera.const import (
	DOMAIN,

)



class SamsungFamilyHubCamera(Camera):

	def __init__(self, hass, token, name, image_path):
		super().__init__()
		self._parent = hass
		self._image_path = image_path
		self._name = name


	def camera_image(self):
		with open(image_path, 'wb') as f:
			return f.read()

    @property
    def name(self):
        """Return the name of this camera."""
        return self._name

