from __future__ import annotations
from dataclasses import dataclass

@dataclass
class UiVector:
	"""A 2D coordinate for an X and Y axis.
	
	Attributes:
	x: position along X-axis 
	y: position along Y-axis
	"""
	x: int = 0
	y: int = 0

	def copy(self) -> UiVector:
		return UiVector(self.x, self.y)
		
		
UiCoord = UiVector
UiSize = UiVector
	
		
