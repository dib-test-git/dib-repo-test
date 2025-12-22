# Dubai Islamic Bank (DIB) – Demo Feature
# Feature Name: Smart Zakat & Charity Recommendation Engine
#
# DISCLAIMER:
# This is a fictional feature and demo-only code.
# It does NOT represent real systems, data, or implementations of Dubai Islamic Bank.

"""
Feature Description:
--------------------
The Smart Zakat & Charity Recommendation Engine is a conceptual feature designed
for a digital Islamic banking platform. The feature helps customers calculate
estimated Zakat obligations and recommends verified charity channels based on
their account balances and spending patterns.

Key Objectives:
- Improve customer engagement through value-added Islamic finance services
- Provide transparency and guidance for Zakat calculations
- Enable digital charity contributions directly from mobile banking apps
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Account:
    account_id: str
    balance_aed: float


@dataclass
class Charity:
    name: str
    category: str
    min_donation_aed: float


class ZakatEngine:
    ZAKAT_RATE = 0.025  # 2.5%

    def calculate_zakat(self, accounts: List[Account]) -> float:
        """
        Calculate estimated Zakat based on total account balances.
        """
        total_balance = sum(a.balance_aed for a in accounts)
        zakat_due = total_balance * self.ZAKAT_RATE
        return round(zakat_due, 2)

    def recommend_charities(
        self, zakat_amount: float, charities: List[Charity]
    ) -> List[Charity]:
        """
        Recommend charities that match the Zakat amount.
        """
        return [
            charity for charity in charities
            if charity.min_donation_aed <= zakat_amount
        ]


if __name__ == "__main__":
    # Demo execution
    accounts = [
        Account(account_id="SAV-001", balance_aed=120000.0),
        Account(account_id="CUR-045", balance_aed=30000.0),
    ]

    charities = [
        Charity("Education Support Fund", "Education", 500),
        Charity("Healthcare Aid", "Health", 1000),
        Charity("Disaster Relief", "Humanitarian", 250),
    ]

    engine = ZakatEngine()
    zakat_due = engine.calculate_zakat(accounts)
    recommendations = engine.recommend_charities(zakat_due, charities)

    print(f"Estimated Zakat Due: AED {zakat_due}")
    print("Recommended Charities:")
    for charity in recommendations:
        print(f"- {charity.name} ({charity.category})")
