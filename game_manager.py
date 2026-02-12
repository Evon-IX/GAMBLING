class GameManager:
    def __init__(self):
        self.money = 777
        self.k = 0  # odd counter
        self.e = 0  # even counter
        self.spin_history = []
        self.jackpot_payouts = 0

    def get_jackpot_probability(self):
        P_k = 1 / (239 - 8 * self.k)
        return min(P_k, 1 / 25)

    def get_spin_time(self):
        T_e = 3.0 - 0.3 * self.e
        return max(T_e, 1.5)

    def spin_wheel(self):
        import random
        return random.randint(0, 9)

    def process_spin_result(self, result):
        if result % 2 == 0:
            self.e += 1  # even
        else:
            self.k += 1  # odd
        self.spin_history.append(result)

    def check_jackpot(self):
        return random.random() < self.get_jackpot_probability()

    def trigger_jackpot(self):
        self.jackpot_payouts += 500
        self.k = 0  # reset odd counter
        self.e = 0  # reset even counter

    def deduct_spin_cost(self):
        self.money -= 10
        if self.money <= 0:
            self.money = 777  # reset money

    def get_game_state(self):
        return {
            'money': self.money,
            'odd_count': self.k,
            'even_count': self.e,
            'spin_history': self.spin_history,
            'jackpot_payouts': self.jackpot_payouts
        }