from typing import Set, Tuple

class Rule():

    def __init__(self, symbol: str, targetLiteral: str, ruleDeter: str = "%") -> None:
        self.__symbol = symbol
        self.__targetLiteral = targetLiteral
        self.ruleDeter = ruleDeter

    def getSymbol(self) -> str:
        return f"{self.ruleDeter}{self.__symbol}"

    def getTargetLiteral(self) -> str:
        return f"{self.__targetLiteral}"

    def getTargetSymbols(self, symbols: Tuple[str, ...]) -> Set[str]:
        result: Set[str] = set()
        for symbol in symbols:
            if symbol in self.__targetLiteral:
                result.add(symbol)
        return result

    def __str__(self) -> str:
        return f"{self.__symbol} - {self.__targetLiteral}"

    def __repr__(self) -> str:
        return self.__str__()