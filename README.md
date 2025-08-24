# 🚀 ViralDeals Pricing Algorithm

An intelligent markup prediction system designed specifically for reselling businesses in India. This algorithm ensures maximum profitability while maintaining competitive pricing across different product categories and market conditions.

## 📊 Core Features

### 🎯 Tiered Markup System
- **₹100-₹299**: 60% markup
- **₹300-₹699**: 45% markup  
- **₹700-₹1,199**: 35% markup
- **₹1,200-₹2,000**: 25% markup
- **₹2,000+**: 20% markup

### 🧠 Smart Adjustments
- **Category-based pricing** (Electronics, Fashion, Beauty, etc.)
- **Competition level analysis** (Low, Medium, High, Very High)
- **Unique value proposition bonuses**
- **Psychological pricing** (prices ending in 9s)

### 💰 Cost Factor Integration
- Payment gateway fees (2%)
- Platform fees (3%)
- Packaging costs (₹10 fixed)
- Returns buffer (3%)
- GST calculations (18% default)

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7+ (for backend algorithm)
- Modern web browser (for web interface)

### Quick Start
1. **Clone or download** this repository
2. **Open `index.html`** in your web browser for the interactive interface
3. **Run tests**: `python test_pricing.py`

### Python Usage
```python
from pricing_algorithm import ViralDealsPricingAlgorithm, ProductCategory, CompetitionLevel

# Initialize the algorithm
pricing_algo = ViralDealsPricingAlgorithm()

# Calculate price for a single product
result = pricing_algo.calculate_price(
    supplier_price=500,
    category=ProductCategory.FASHION,
    competition=CompetitionLevel.MEDIUM,
    has_unique_value=True
)

print(f"Final Price: ₹{result.final_price}")
print(f"Profit Margin: {result.profit_margin:.1f}%")
```

## 🌐 Web Interface

The web interface provides:
- **Single product calculator** with real-time results
- **Bulk pricing** for multiple products
- **Interactive cost breakdown**
- **Mobile-responsive design**
- **Psychological pricing toggle**

### Using the Web Interface
1. Open `index.html` in your browser
2. Enter supplier price and select options
3. View instant pricing recommendations
4. Use bulk calculator for multiple products

## 📈 Algorithm Logic

### Base Markup Calculation
```python
def get_base_markup(supplier_price):
    if 100 <= supplier_price <= 299:
        return 0.60  # 60%
    elif 300 <= supplier_price <= 699:
        return 0.45  # 45%
    # ... and so on
```

### Smart Adjustments
1. **Category Multiplier**: Electronics (0.85x), Beauty (1.2x), Fashion (1.15x)
2. **Competition Factor**: Low (1.2x), High (0.85x), Very High (0.7x)
3. **Unique Value Bonus**: +15% for bundled/warranty products
4. **Minimum Margin**: Always ensures at least 15% markup

### Cost Integration
The algorithm automatically adds:
- Payment processing fees
- Platform commissions
- Packaging and shipping prep
- Returns/warranty buffer
- Applicable taxes

## 🧪 Testing & Validation

Run the comprehensive test suite:
```bash
python test_pricing.py
```

This validates:
- ✅ Correct markup tiers
- ✅ Category adjustments
- ✅ Competition factors
- ✅ Psychological pricing
- ✅ Cost calculations
- ✅ Real-world scenarios

## 📊 Example Results

| Supplier Price | Category | Competition | Final Price | Markup | Margin |
|---------------|----------|-------------|-------------|---------|---------|
| ₹150 | Electronics | High | ₹239 | 51.0% | 31.8% |
| ₹500 | Fashion | Medium | ₹899 | 51.8% | 34.1% |
| ₹900 | Beauty | Low | ₹1,699 | 50.4% | 33.5% |
| ₹1,600 | Generic | Medium | ₹2,499 | 25.0% | 20.0% |

## 🎛️ Customization Options

### Adjust Cost Factors
```python
from pricing_algorithm import CostFactors

custom_costs = CostFactors(
    payment_gateway_fee=0.025,  # 2.5%
    platform_fee=0.02,         # 2%
    packaging_cost=15.0,        # ₹15
    returns_buffer=0.05,        # 5%
    gst_rate=0.12              # 12%
)

pricing_algo = ViralDealsPricingAlgorithm(custom_costs)
```

### Category-Specific Adjustments
Modify `CATEGORY_ADJUSTMENTS` in the algorithm to fine-tune for your specific market:
```python
CATEGORY_ADJUSTMENTS = {
    ProductCategory.ELECTRONICS: 0.80,  # More competitive
    ProductCategory.BEAUTY: 1.25,       # Higher margins
    # ... customize as needed
}
```

## 🚀 Advanced Features

### Bulk Processing
```python
products = [
    {"supplier_price": 150, "category": "electronics", "competition": "high"},
    {"supplier_price": 500, "category": "fashion", "competition": "medium"}
]

results = pricing_algo.bulk_calculate(products)
```

### API Integration Ready
The algorithm is designed to integrate with:
- E-commerce platforms (Shopify, WooCommerce)
- Inventory management systems
- Supplier APIs
- Marketplace integrations

## 📱 Mobile Optimization

The web interface is fully responsive and optimized for:
- Mobile price checking
- Quick calculations on-the-go
- Touch-friendly controls
- Fast loading times

## 🔧 Troubleshooting

### Common Issues
1. **Prices seem too high**: Adjust competition level to "High" or "Very High"
2. **Margins too low**: Enable "unique value proposition" or choose less competitive category
3. **Bulk calculator errors**: Ensure JSON format is correct

### Support
- Check the test suite for examples
- Review cost factor settings
- Validate input data format

## 🎯 Best Practices

1. **Regular Market Research**: Update competition levels based on current market
2. **Category Analysis**: Monitor which categories perform best
3. **Seasonal Adjustments**: Consider seasonal demand in competition settings
4. **A/B Testing**: Test different pricing strategies with small batches
5. **Margin Monitoring**: Track actual vs. predicted margins

## 📈 Future Enhancements

Planned features:
- Machine learning price optimization
- Competitor price tracking
- Seasonal adjustment algorithms
- Integration with popular e-commerce platforms
- Advanced analytics dashboard

## 📄 License

This pricing algorithm is designed for ViralDeals business use. Modify and adapt as needed for your specific requirements.

---

**Ready to maximize your profits?** 🚀
Open `index.html` and start calculating optimal prices for your products!
