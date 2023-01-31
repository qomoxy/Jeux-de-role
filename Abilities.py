from globalInfo import TupleToRandom
from effects import EffectManager


class Ability():
    def __init__(self, speed: tuple[int, int], name: str, info: str, abilityEffects: EffectManager, cellColor: str = "Red", shape: list[str] = ["•••",
                                                                                                                                                "•P•",
                                                                                                                                                "•••"]) -> None:
        self.name: str = name
        self.info: str = info
        self.speed: int = TupleToRandom(speed)
        self.shape = shape
        self.cellColor = cellColor
        self.abilityEffects: EffectManager = abilityEffects