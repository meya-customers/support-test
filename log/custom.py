from dataclasses import dataclass
from meya.element.field import element_field
from meya.entry import Entry
from meya.log.element import LogElement
from typing import List


@dataclass
class CustomLogElement(LogElement):
    inspector_url: str = element_field()
    entry_types: List[str] = element_field()

    async def process(self) -> List[Entry]:
        if self.entry.get_entry_type() in self.entry_types:
            await self.http.post(
                self.inspector_url, json=self.entry.to_typed_dict()
            )
        return []
