"""
ViralDeals Pricing Algorithm
Intelligent markup prediction system for reselling business
"""

import math
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum

class ProductCategory(Enum):
    """Product categories with different competitive pressures"""
    ELECTRONICS = "electronics"
    FASHION = "fashion"
    HOME_KITCHEN = "home_kitchen"
    BEAUTY = "beauty"
    SPORTS = "sports"
    BOOKS = "books"
    TOYS = "toys"
    GENERIC = "generic"

class CompetitionLevel(Enum):
    """Market competition intensity"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    VERY_HIGH = "very_high"

@dataclass
class CostFactors:
    """Additional costs that affect final pricing"""
    payment_gateway_fee: float = 0.02  # 2%
    platform_fee: float = 0.03  # 3%
    packaging_cost: float = 10.0  # Fixed ₹10
    returns_buffer: float = 0.03  # 3%
    gst_rate: float = 0.18  # 18% (can vary by category)

@dataclass
class PricingResult:
    """Result of pricing calculation"""
    supplier_price: float
    base_markup_percent: float
    adjusted_markup_percent: float
    selling_price: float
    final_price: float  # After psychological pricing
    profit_margin: float
    cost_breakdown: Dict[str, float]

class ViralDealsPricingAlgorithm:
    """
    Intelligent pricing algorithm for ViralDeals reselling business
    """
    
    # Base markup tiers as specified
    BASE_MARKUP_TIERS = [
        (100, 299, 0.60),   # ₹100-₹299: +60%
        (300, 699, 0.45),   # ₹300-₹699: +45%
        (700, 1199, 0.35),  # ₹700-₹1199: +35%
        (1200, 2000, 0.25), # ₹1200-₹2000: +25%
        (2001, float('inf'), 0.20)  # Above ₹2000: +20%
    ]
    
    # Category adjustments (multipliers to base markup)
    CATEGORY_ADJUSTMENTS = {
        ProductCategory.ELECTRONICS: 0.85,      # Highly competitive
        ProductCategory.FASHION: 1.15,          # Higher margins possible
        ProductCategory.HOME_KITCHEN: 1.0,      # Standard
        ProductCategory.BEAUTY: 1.2,            # Premium category
        ProductCategory.SPORTS: 0.9,            # Competitive
        ProductCategory.BOOKS: 0.7,             # Very competitive
        ProductCategory.TOYS: 1.1,              # Good margins
        ProductCategory.GENERIC: 1.0            # Standard
    }
    
    # Competition level adjustments
    COMPETITION_ADJUSTMENTS = {
        CompetitionLevel.LOW: 1.2,
        CompetitionLevel.MEDIUM: 1.0,
        CompetitionLevel.HIGH: 0.85,
        CompetitionLevel.VERY_HIGH: 0.7
    }
    
    def __init__(self, cost_factors: Optional[CostFactors] = None):
        self.cost_factors = cost_factors or CostFactors()
    
    def get_base_markup(self, supplier_price: float) -> float:
        """Get base markup percentage based on price tier"""
        for min_price, max_price, markup in self.BASE_MARKUP_TIERS:
            if min_price <= supplier_price <= max_price:
                return markup
        
        # Fallback for prices outside defined ranges
        if supplier_price < 100:
            return 0.70  # Higher markup for very low-cost items
        else:
            return 0.15  # Conservative markup for very high-cost items
    
    def calculate_adjusted_markup(
        self, 
        base_markup: float,
        category: ProductCategory = ProductCategory.GENERIC,
        competition: CompetitionLevel = CompetitionLevel.MEDIUM,
        has_unique_value: bool = False
    ) -> float:
        """Calculate adjusted markup based on various factors"""
        
        adjusted_markup = base_markup
        
        # Apply category adjustment
        adjusted_markup *= self.CATEGORY_ADJUSTMENTS[category]
        
        # Apply competition adjustment
        adjusted_markup *= self.COMPETITION_ADJUSTMENTS[competition]
        
        # Bonus for unique value proposition
        if has_unique_value:
            adjusted_markup *= 1.15
        
        # Ensure minimum markup of 15% for sustainability
        return max(adjusted_markup, 0.15)
    
    def calculate_total_costs(self, supplier_price: float, selling_price: float) -> Dict[str, float]:
        """Calculate all additional costs"""
        costs = {}
        
        # Payment gateway fee
        costs['payment_gateway'] = selling_price * self.cost_factors.payment_gateway_fee
        
        # Platform fee
        costs['platform_fee'] = selling_price * self.cost_factors.platform_fee
        
        # Fixed packaging cost
        costs['packaging'] = self.cost_factors.packaging_cost
        
        # Returns buffer
        costs['returns_buffer'] = selling_price * self.cost_factors.returns_buffer
        
        # GST (if applicable)
        costs['gst'] = selling_price * self.cost_factors.gst_rate
        
        return costs
    
    def apply_psychological_pricing(self, price: float) -> float:
        """Apply psychological pricing (ending in 9s)"""
        if price < 100:
            # For prices under ₹100, end with 9
            return math.floor(price / 10) * 10 + 9
        elif price < 1000:
            # For prices ₹100-999, end with 99
            return math.floor(price / 100) * 100 + 99
        else:
            # For prices ₹1000+, end with 999 or 499
            hundreds = math.floor(price / 100)
            if hundreds % 10 < 5:
                return hundreds * 100 - 1  # End with 999
            else:
                return (hundreds - hundreds % 10 + 4) * 100 + 99  # End with 499
    
    def calculate_price(
        self,
        supplier_price: float,
        category: ProductCategory = ProductCategory.GENERIC,
        competition: CompetitionLevel = CompetitionLevel.MEDIUM,
        has_unique_value: bool = False,
        apply_psychological: bool = True
    ) -> PricingResult:
        """
        Main pricing calculation method
        """
        
        # Step 1: Get base markup
        base_markup = self.get_base_markup(supplier_price)
        
        # Step 2: Apply adjustments
        adjusted_markup = self.calculate_adjusted_markup(
            base_markup, category, competition, has_unique_value
        )
        
        # Step 3: Calculate selling price
        selling_price = supplier_price * (1 + adjusted_markup)
        
        # Step 4: Calculate additional costs
        cost_breakdown = self.calculate_total_costs(supplier_price, selling_price)
        total_additional_costs = sum(cost_breakdown.values())
        
        # Step 5: Adjust for costs to maintain margin
        adjusted_selling_price = selling_price + total_additional_costs
        
        # Step 6: Apply psychological pricing
        final_price = self.apply_psychological_pricing(adjusted_selling_price) if apply_psychological else adjusted_selling_price
        
        # Step 7: Calculate actual profit margin
        profit = final_price - supplier_price - total_additional_costs
        profit_margin = (profit / final_price) * 100 if final_price > 0 else 0
        
        return PricingResult(
            supplier_price=supplier_price,
            base_markup_percent=base_markup * 100,
            adjusted_markup_percent=adjusted_markup * 100,
            selling_price=selling_price,
            final_price=final_price,
            profit_margin=profit_margin,
            cost_breakdown=cost_breakdown
        )
    
    def bulk_calculate(self, products: List[Dict]) -> List[PricingResult]:
        """Calculate prices for multiple products"""
        results = []
        for product in products:
            result = self.calculate_price(
                supplier_price=product['supplier_price'],
                category=ProductCategory(product.get('category', 'generic')),
                competition=CompetitionLevel(product.get('competition', 'medium')),
                has_unique_value=product.get('has_unique_value', False)
            )
            results.append(result)
        return results

# Example usage and testing
if __name__ == "__main__":
    # Initialize the pricing algorithm
    pricing_algo = ViralDealsPricingAlgorithm()
    
    # Test cases based on your examples
    test_cases = [
        {"price": 150, "desc": "Low-cost item"},
        {"price": 500, "desc": "Mid-range item"},
        {"price": 900, "desc": "Higher-cost item"},
        {"price": 1600, "desc": "Premium item"}
    ]
    
    print("ViralDeals Pricing Algorithm Test Results")
    print("=" * 50)
    
    for test in test_cases:
        result = pricing_algo.calculate_price(test["price"])
        print(f"\n{test['desc']} (₹{test['price']}):")
        print(f"  Base Markup: {result.base_markup_percent:.1f}%")
        print(f"  Final Price: ₹{result.final_price:.0f}")
        print(f"  Profit Margin: {result.profit_margin:.1f}%")
