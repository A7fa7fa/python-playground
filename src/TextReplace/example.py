from ruleRepo import RuleRepository
from rule import Rule
from validator import RuleValidatorDefault, RuleValidatorIncludeDeterm, RuleValidatorIncludeOtherRules

repo = RuleRepository()
repo.includeValidator(RuleValidatorDefault()) \
    .includeValidator(RuleValidatorIncludeOtherRules()) \
    .includeValidator(RuleValidatorIncludeDeterm())

rule1 = Rule(
    symbol="asdf", targetLiteral=r"111111111111%1 1111111111111111111%311111111")
repo.register(rule1)
rule2 = Rule(symbol="1", targetLiteral=r"q q q q q q q q q q q qq q q qq q  q")
repo.register(rule2)
rule3 = Rule(symbol="123345",
             targetLiteral=r"q q q q q q q q q q q qq q q qq q %1  q")
repo.register(rule3)
rule3 = Rule(symbol="3", targetLiteral=r"__ this is rule num 3 __ %12345")
repo.register(rule3)

text = r"askd aspd asdm %asdf asdm asd %3"
print(repo.apply(text))
