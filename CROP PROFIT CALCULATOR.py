def crop_profit_calculator():
    print("Crop profit prediction calculator")
    crop_name = input("Enter the name of crop: ")
    try:
        land_area = float(input("Enter area of land: "))
        yield_per_acre = float(input("Enter expected yield per acre(kg): "))
        market_price = float(input("Enter expected price of market per kg: "))
        total_cost_per_acre = float(input("Enter total cultivation cost per acre: "))
    except ValueError:
        print("Invalid input! Enter numeric values for area, yield, price, and cost")
        return
    total_yield = land_area * yield_per_acre
    total_revenue = total_yield * market_price
    total_cost = land_area * total_cost_per_acre
    profit = total_revenue - total_cost
    print("\nCrop profit prediction result")
    print(f"Crop name: {crop_name}")
    print(f"Total yield: {total_yield:.2f} kg")
    print(f"Total revenue: {total_revenue:.2f} rupees")
    print(f"Total cost: {total_cost:.2f} rupees")
    print(f"Profit: {profit:.2f} rupees")
    if profit > 0:
        print(f"Estimated profit: in rupees {profit:.2f}")
    else:
        print(f"Estimated loss: in rupees {profit:.2f}")

if __name__ == "__main__":
    crop_profit_calculator()