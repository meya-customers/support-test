from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from typing import List
from typing import Optional


@dataclass
class LogComponentElement(Component):
    message: str = element_field()
    data: Optional[dict] = element_field(default_factory=dict)

    async def start(self) -> List[Entry]:
        # self.log.debug(self.message, context=self.context)
        self.log.info(self.message, context=self.context)
        # self.log.warning(self.message, context=self.context)
        # self.log.error(self.message, context=self.context)
        return self.respond()
