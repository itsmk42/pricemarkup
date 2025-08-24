/**
 * ViralDeals Pricing Calculator - JavaScript Implementation
 * Mirrors the Python algorithm for web interface
 */

class ViralDealsPricingCalculator {
    constructor() {
        // Base markup tiers
        this.baseMarkupTiers = [
            { min: 100, max: 299, markup: 0.60 },
            { min: 300, max: 699, markup: 0.45 },
            { min: 700, max: 1199, markup: 0.35 },
            { min: 1200, max: 2000, markup: 0.25 },
            { min: 2001, max: Infinity, markup: 0.20 }
        ];

        // Category adjustments
        this.categoryAdjustments = {
            'electronics': 0.85,
            'fashion': 1.15,
            'home_kitchen': 1.0,
            'beauty': 1.2,
            'sports': 0.9,
            'books': 0.7,
            'toys': 1.1,
            'generic': 1.0
        };

        // Competition adjustments
        this.competitionAdjustments = {
            'low': 1.2,
            'medium': 1.0,
            'high': 0.85,
            'very_high': 0.7
        };

        // Cost factors
        this.costFactors = {
            paymentGatewayFee: 0.02,
            platformFee: 0.03,
            packagingCost: 10.0,
            returnsBuffer: 0.03,
            gstRate: 0.18
        };
    }

    getBaseMarkup(supplierPrice) {
        for (let tier of this.baseMarkupTiers) {
            if (supplierPrice >= tier.min && supplierPrice <= tier.max) {
                return tier.markup;
            }
        }
        
        // Fallback
        if (supplierPrice < 100) {
            return 0.70;
        } else {
            return 0.15;
        }
    }

    calculateAdjustedMarkup(baseMarkup, category = 'generic', competition = 'medium', hasUniqueValue = false) {
        let adjustedMarkup = baseMarkup;
        
        // Apply category adjustment
        adjustedMarkup *= this.categoryAdjustments[category] || 1.0;
        
        // Apply competition adjustment
        adjustedMarkup *= this.competitionAdjustments[competition] || 1.0;
        
        // Bonus for unique value
        if (hasUniqueValue) {
            adjustedMarkup *= 1.15;
        }
        
        // Ensure minimum 15% markup
        return Math.max(adjustedMarkup, 0.15);
    }

    calculateTotalCosts(supplierPrice, sellingPrice) {
        const costs = {};
        
        costs.paymentGateway = sellingPrice * this.costFactors.paymentGatewayFee;
        costs.platformFee = sellingPrice * this.costFactors.platformFee;
        costs.packaging = this.costFactors.packagingCost;
        costs.returnsBuffer = sellingPrice * this.costFactors.returnsBuffer;
        costs.gst = sellingPrice * this.costFactors.gstRate;
        
        return costs;
    }

    applyPsychologicalPricing(price) {
        if (price < 100) {
            return Math.floor(price / 10) * 10 + 9;
        } else if (price < 1000) {
            return Math.floor(price / 100) * 100 + 99;
        } else {
            const hundreds = Math.floor(price / 100);
            if (hundreds % 10 < 5) {
                return hundreds * 100 - 1;
            } else {
                return (hundreds - hundreds % 10 + 4) * 100 + 99;
            }
        }
    }

    calculatePrice(supplierPrice, category = 'generic', competition = 'medium', hasUniqueValue = false, applyPsychological = true) {
        // Step 1: Get base markup
        const baseMarkup = this.getBaseMarkup(supplierPrice);
        
        // Step 2: Apply adjustments
        const adjustedMarkup = this.calculateAdjustedMarkup(baseMarkup, category, competition, hasUniqueValue);
        
        // Step 3: Calculate selling price
        const sellingPrice = supplierPrice * (1 + adjustedMarkup);
        
        // Step 4: Calculate additional costs
        const costBreakdown = this.calculateTotalCosts(supplierPrice, sellingPrice);
        const totalAdditionalCosts = Object.values(costBreakdown).reduce((sum, cost) => sum + cost, 0);
        
        // Step 5: Adjust for costs
        const adjustedSellingPrice = sellingPrice + totalAdditionalCosts;
        
        // Step 6: Apply psychological pricing
        const finalPrice = applyPsychological ? this.applyPsychologicalPricing(adjustedSellingPrice) : adjustedSellingPrice;
        
        // Step 7: Calculate profit margin
        const profit = finalPrice - supplierPrice - totalAdditionalCosts;
        const profitMargin = finalPrice > 0 ? (profit / finalPrice) * 100 : 0;
        
        return {
            supplierPrice,
            baseMarkupPercent: baseMarkup * 100,
            adjustedMarkupPercent: adjustedMarkup * 100,
            sellingPrice,
            finalPrice,
            profitMargin,
            costBreakdown,
            totalCosts: totalAdditionalCosts
        };
    }
}

// Initialize calculator
const calculator = new ViralDealsPricingCalculator();

// Single product calculation
function calculatePrice() {
    const supplierPrice = parseFloat(document.getElementById('supplierPrice').value);
    const category = document.getElementById('category').value;
    const competition = document.getElementById('competition').value;
    const hasUniqueValue = document.getElementById('uniqueValue').checked;
    const applyPsychological = document.getElementById('psychological').checked;

    if (!supplierPrice || supplierPrice <= 0) {
        alert('Please enter a valid supplier price');
        return;
    }

    const result = calculator.calculatePrice(supplierPrice, category, competition, hasUniqueValue, applyPsychological);
    
    // Display results
    document.getElementById('finalPrice').textContent = `₹${Math.round(result.finalPrice)}`;
    document.getElementById('baseMarkup').textContent = `${result.baseMarkupPercent.toFixed(1)}%`;
    document.getElementById('adjustedMarkup').textContent = `${result.adjustedMarkupPercent.toFixed(1)}%`;
    document.getElementById('profitMargin').textContent = `${result.profitMargin.toFixed(1)}%`;
    document.getElementById('totalCosts').textContent = `₹${Math.round(result.totalCosts)}`;
    
    // Show results
    document.getElementById('results').classList.add('show');
}

// Bulk calculation
function calculateBulk() {
    const bulkInput = document.getElementById('bulkInput').value;
    const resultsContainer = document.getElementById('bulkResults');
    
    try {
        const products = JSON.parse(bulkInput);
        let resultsHTML = '';
        
        products.forEach((product, index) => {
            const result = calculator.calculatePrice(
                product.supplier_price,
                product.category || 'generic',
                product.competition || 'medium',
                product.has_unique_value || false,
                true
            );
            
            resultsHTML += `
                <div class="bulk-result-item">
                    <div>
                        <strong>Product ${index + 1}</strong><br>
                        Cost: ₹${product.supplier_price}
                    </div>
                    <div>
                        <strong>Final Price</strong><br>
                        ₹${Math.round(result.finalPrice)}
                    </div>
                    <div>
                        <strong>Markup</strong><br>
                        ${result.adjustedMarkupPercent.toFixed(1)}%
                    </div>
                    <div>
                        <strong>Profit Margin</strong><br>
                        ${result.profitMargin.toFixed(1)}%
                    </div>
                </div>
            `;
        });
        
        resultsContainer.innerHTML = resultsHTML;
        
    } catch (error) {
        alert('Invalid JSON format. Please check your input.');
        console.error('JSON parsing error:', error);
    }
}

// Auto-calculate on input change
document.getElementById('supplierPrice').addEventListener('input', function() {
    if (this.value) {
        calculatePrice();
    }
});

// Example data for bulk calculator
function loadExampleData() {
    const exampleData = [
        {"supplier_price": 150, "category": "electronics", "competition": "high"},
        {"supplier_price": 500, "category": "fashion", "competition": "medium"},
        {"supplier_price": 900, "category": "beauty", "competition": "low", "has_unique_value": true},
        {"supplier_price": 1600, "category": "generic", "competition": "medium"}
    ];
    
    document.getElementById('bulkInput').value = JSON.stringify(exampleData, null, 2);
}

// Initialize with example calculation
window.addEventListener('load', function() {
    document.getElementById('supplierPrice').value = '500';
    calculatePrice();
});

// Export functions for testing
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { ViralDealsPricingCalculator, calculatePrice, calculateBulk };
}
