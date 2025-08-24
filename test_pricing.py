"""
Test suite and demo for ViralDeals Pricing Algorithm
"""

from pricing_algorithm import (
    ViralDealsPricingAlgorithm, 
    ProductCategory, 
    CompetitionLevel, 
    CostFactors
)
import json

def test_basic_tiers():
    """Test the basic markup tiers match your requirements"""
    print("🧪 Testing Basic Markup Tiers")
    print("=" * 50)
    
    pricing_algo = ViralDealsPricingAlgorithm()
    
    test_cases = [
        (150, "₹100-₹299 tier", 60),
        (500, "₹300-₹699 tier", 45),
        (900, "₹700-₹1199 tier", 35),
        (1600, "₹1200-₹2000 tier", 25),
        (2500, "Above ₹2000 tier", 20)
    ]
    
    for price, description, expected_markup in test_cases:
        result = pricing_algo.calculate_price(price)
        print(f"\n{description} (₹{price}):")
        print(f"  Expected Base Markup: {expected_markup}%")
        print(f"  Actual Base Markup: {result.base_markup_percent:.1f}%")
        print(f"  Final Price: ₹{result.final_price:.0f}")
        print(f"  Profit Margin: {result.profit_margin:.1f}%")
        
        # Verify base markup is correct
        assert abs(result.base_markup_percent - expected_markup) < 1, f"Base markup mismatch for {price}"
    
    print("\n✅ All basic tier tests passed!")

def test_category_adjustments():
    """Test category-based adjustments"""
    print("\n🏷️ Testing Category Adjustments")
    print("=" * 50)
    
    pricing_algo = ViralDealsPricingAlgorithm()
    base_price = 500  # Mid-tier price
    
    categories = [
        (ProductCategory.ELECTRONICS, "Electronics (competitive)"),
        (ProductCategory.FASHION, "Fashion (higher margins)"),
        (ProductCategory.BEAUTY, "Beauty (premium)"),
        (ProductCategory.BOOKS, "Books (very competitive)"),
        (ProductCategory.GENERIC, "Generic (standard)")
    ]
    
    for category, description in categories:
        result = pricing_algo.calculate_price(base_price, category=category)
        print(f"\n{description}:")
        print(f"  Adjusted Markup: {result.adjusted_markup_percent:.1f}%")
        print(f"  Final Price: ₹{result.final_price:.0f}")
        print(f"  Profit Margin: {result.profit_margin:.1f}%")

def test_competition_levels():
    """Test competition level adjustments"""
    print("\n🏆 Testing Competition Level Adjustments")
    print("=" * 50)
    
    pricing_algo = ViralDealsPricingAlgorithm()
    base_price = 800
    
    competition_levels = [
        (CompetitionLevel.LOW, "Low Competition"),
        (CompetitionLevel.MEDIUM, "Medium Competition"),
        (CompetitionLevel.HIGH, "High Competition"),
        (CompetitionLevel.VERY_HIGH, "Very High Competition")
    ]
    
    for competition, description in competition_levels:
        result = pricing_algo.calculate_price(base_price, competition=competition)
        print(f"\n{description}:")
        print(f"  Adjusted Markup: {result.adjusted_markup_percent:.1f}%")
        print(f"  Final Price: ₹{result.final_price:.0f}")
        print(f"  Profit Margin: {result.profit_margin:.1f}%")

def test_psychological_pricing():
    """Test psychological pricing feature"""
    print("\n🧠 Testing Psychological Pricing")
    print("=" * 50)
    
    pricing_algo = ViralDealsPricingAlgorithm()
    
    test_prices = [85, 250, 750, 1500, 2200]
    
    for price in test_prices:
        result_with = pricing_algo.calculate_price(price, apply_psychological=True)
        result_without = pricing_algo.calculate_price(price, apply_psychological=False)
        
        print(f"\nSupplier Price: ₹{price}")
        print(f"  Without Psychological: ₹{result_without.final_price:.0f}")
        print(f"  With Psychological: ₹{result_with.final_price:.0f}")

def test_cost_breakdown():
    """Test detailed cost breakdown"""
    print("\n💰 Testing Cost Breakdown")
    print("=" * 50)
    
    pricing_algo = ViralDealsPricingAlgorithm()
    result = pricing_algo.calculate_price(1000)
    
    print(f"Supplier Price: ₹{result.supplier_price}")
    print(f"Base Selling Price: ₹{result.selling_price:.2f}")
    print(f"Final Price: ₹{result.final_price}")
    print(f"\nCost Breakdown:")
    
    for cost_type, amount in result.cost_breakdown.items():
        print(f"  {cost_type.replace('_', ' ').title()}: ₹{amount:.2f}")
    
    print(f"\nTotal Additional Costs: ₹{sum(result.cost_breakdown.values()):.2f}")
    print(f"Profit Margin: {result.profit_margin:.1f}%")

def demo_real_world_scenarios():
    """Demo with real-world product scenarios"""
    print("\n🌟 Real-World Scenarios Demo")
    print("=" * 50)
    
    pricing_algo = ViralDealsPricingAlgorithm()
    
    scenarios = [
        {
            "name": "Budget Smartphone Case",
            "supplier_price": 120,
            "category": ProductCategory.ELECTRONICS,
            "competition": CompetitionLevel.VERY_HIGH,
            "has_unique_value": False
        },
        {
            "name": "Premium Beauty Serum",
            "supplier_price": 800,
            "category": ProductCategory.BEAUTY,
            "competition": CompetitionLevel.MEDIUM,
            "has_unique_value": True
        },
        {
            "name": "Trendy Fashion Accessory",
            "supplier_price": 350,
            "category": ProductCategory.FASHION,
            "competition": CompetitionLevel.LOW,
            "has_unique_value": True
        },
        {
            "name": "Generic Kitchen Gadget",
            "supplier_price": 600,
            "category": ProductCategory.HOME_KITCHEN,
            "competition": CompetitionLevel.HIGH,
            "has_unique_value": False
        }
    ]
    
    for scenario in scenarios:
        result = pricing_algo.calculate_price(
            supplier_price=scenario["supplier_price"],
            category=scenario["category"],
            competition=scenario["competition"],
            has_unique_value=scenario["has_unique_value"]
        )
        
        print(f"\n📦 {scenario['name']}")
        print(f"   Supplier Cost: ₹{scenario['supplier_price']}")
        print(f"   Category: {scenario['category'].value.replace('_', ' ').title()}")
        print(f"   Competition: {scenario['competition'].value.replace('_', ' ').title()}")
        print(f"   Unique Value: {'Yes' if scenario['has_unique_value'] else 'No'}")
        print(f"   → Final Price: ₹{result.final_price:.0f}")
        print(f"   → Markup: {result.adjusted_markup_percent:.1f}%")
        print(f"   → Profit Margin: {result.profit_margin:.1f}%")

def test_bulk_processing():
    """Test bulk processing capability"""
    print("\n📊 Testing Bulk Processing")
    print("=" * 50)
    
    pricing_algo = ViralDealsPricingAlgorithm()
    
    products = [
        {"supplier_price": 150, "category": "electronics", "competition": "high"},
        {"supplier_price": 500, "category": "fashion", "competition": "medium"},
        {"supplier_price": 900, "category": "beauty", "competition": "low", "has_unique_value": True},
        {"supplier_price": 1600, "category": "generic", "competition": "medium"}
    ]
    
    # Convert string values to enums for bulk processing
    processed_products = []
    for product in products:
        processed_product = {
            "supplier_price": product["supplier_price"],
            "category": product["category"],
            "competition": product["competition"],
            "has_unique_value": product.get("has_unique_value", False)
        }
        processed_products.append(processed_product)
    
    results = pricing_algo.bulk_calculate(processed_products)
    
    print(f"Processed {len(results)} products:")
    for i, result in enumerate(results):
        print(f"\nProduct {i+1}: ₹{products[i]['supplier_price']} → ₹{result.final_price:.0f}")
        print(f"  Markup: {result.adjusted_markup_percent:.1f}%, Margin: {result.profit_margin:.1f}%")

def generate_pricing_report():
    """Generate a comprehensive pricing report"""
    print("\n📈 Comprehensive Pricing Report")
    print("=" * 50)
    
    pricing_algo = ViralDealsPricingAlgorithm()
    
    # Test across price ranges
    price_ranges = [100, 200, 400, 600, 800, 1000, 1500, 2000, 3000]
    
    print("\nPrice Range Analysis:")
    print("Supplier Price | Base Markup | Final Price | Profit Margin")
    print("-" * 55)
    
    for price in price_ranges:
        result = pricing_algo.calculate_price(price)
        print(f"₹{price:>10} | {result.base_markup_percent:>9.1f}% | ₹{result.final_price:>8.0f} | {result.profit_margin:>10.1f}%")

if __name__ == "__main__":
    print("🚀 ViralDeals Pricing Algorithm Test Suite")
    print("=" * 60)
    
    # Run all tests
    test_basic_tiers()
    test_category_adjustments()
    test_competition_levels()
    test_psychological_pricing()
    test_cost_breakdown()
    demo_real_world_scenarios()
    test_bulk_processing()
    generate_pricing_report()
    
    print("\n🎉 All tests completed successfully!")
    print("\n💡 Your pricing algorithm is ready to maximize profits!")
    print("   Open index.html in your browser to use the web interface.")
