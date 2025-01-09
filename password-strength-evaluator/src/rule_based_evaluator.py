class RuleBasedEvaluator:
    def __init__(self):
        self.rules = {
            'length': lambda password: len(password) >= 8,
            'uppercase': lambda password: any(c.isupper() for c in password),
            'lowercase': lambda password: any(c.islower() for c in password),
            'digit': lambda password: any(c.isdigit() for c in password),
            'special_char': lambda password: any(c in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for c in password)
        }

    def evaluate(self, password):
        score = 0
        for rule, check in self.rules.items():
            if check(password):
                score += 1
        return score

    def is_strong(self, password):
        return self.evaluate(password) >= 4  # At least 4 out of 5 rules must be satisfied