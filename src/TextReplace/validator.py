from abc import ABC, abstractmethod
from typing import Dict, List, Set, Tuple
from rule import Rule


class RuleValidatorAbc(ABC):

    @abstractmethod
    def validate(self, rules: Dict[str, Rule], newRule: Rule) -> bool:
        raise NotImplementedError

class RuleValidatorIncludeOtherRules(RuleValidatorAbc):

    def validate(self, rules: Dict[str, Rule], newRule: Rule) -> bool:
        registedSymbols = list(rules.keys())
        newSymbol = newRule.getSymbol()
        for symbol in registedSymbols:
            if symbol.startswith(newSymbol):
                return False
            if newSymbol.startswith(symbol):
                return False
        return True

class RuleValidatorIncludeDeterm(RuleValidatorAbc):

    def validate(self, rules: Dict[str, Rule], newRule: Rule) -> bool:
        return newRule.ruleDeter not in newRule.getSymbol()[1:]

class RuleValidatorDefault(RuleValidatorAbc):

    def __dfs(self, registedSymbols: Tuple[str, ...], symbols: List[str], seen: Set[str], rules: Dict[str, Rule], newRule: Rule) -> bool:

        for symbol in symbols:
            if symbol in seen:
                return False
            seen.add(symbol)
            targets = rules.get(symbol, newRule).getTargetSymbols(registedSymbols)
            return self.__dfs(registedSymbols, list(targets), seen, rules, newRule)
        return True

    def validate(self, rules: Dict[str, Rule], newRule: Rule) -> bool:

        registedSymbols = list(rules.keys())
        registedSymbols.append(newRule.getSymbol())

        for rule in rules.values():
            seen: Set[str] = set()
            seen.add(rule.getSymbol())
            targets = rule.getTargetSymbols(tuple(registedSymbols))
            return self.__dfs(tuple(registedSymbols), list(targets), seen, rules, newRule)
        return True
