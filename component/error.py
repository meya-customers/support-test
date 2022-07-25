from dataclasses import dataclass
from meya.component.element import Component
from meya.entry import Entry
from typing import List


@dataclass
class ErrorComponentElement(Component):
    async def start(self) -> List[Entry]:
        print(1 / 0)
        return self.respond()
