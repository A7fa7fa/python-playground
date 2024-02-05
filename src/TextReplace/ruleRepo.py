
from typing import Dict, List
from rule import Rule
from validator import RuleValidatorAbc


class RuleRepository():

    def __init__(self, validator: "RuleValidatorAbc | None" = None) -> None:
        self.validators: List["RuleValidatorAbc"] = []
        if validator:
            self.validators.append(validator)
        self.repo: Dict[str, Rule] = dict()

    def __append(self, rule: Rule) -> None:
        self.repo[rule.getSymbol()] = rule

    def includeValidator(self, validator: "RuleValidatorAbc") -> "RuleRepository":
        self.validators.append(validator)
        return self

    def register(self, rule: Rule | None) -> Rule | None:
        if rule is None:
            return None

        if not all([val.validate(self.repo, rule) for val in self.validators]):
            return None

        self.__append(rule)
        return rule

    def apply(self, text: str) -> str:

        temp = ""
        while temp != text:
            temp = text
            for rule in self.repo.values():
                text = text.replace(rule.getSymbol(), rule.getTargetLiteral())
        return text
