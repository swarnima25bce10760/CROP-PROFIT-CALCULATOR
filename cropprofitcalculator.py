def crop_profit_calculator():
    print("crop profit prediction calculator")
    crop_name = input("enter the name of crop: ")
    try:
        land_area= float(input("enter area of land: "))
        yield_per_acre = float(input("enter expected yeild per acre(kg): "))
        market_price = float(input("enter expected price of market per kg: "))
        cost_per_acre = float(input("enter total cultivation cost per acre: "))
    except ValueError:
        print("invalid input! enter numeric values for area, yield, price, and cost")
        return
    total_yield = land_area* yield_per_acre
    total_revenue= total_yield* market_price
    total_cost= land_area* cost_per_acre
    profit= total_revenue - total_cost
    print("crop profit prediction result")
    print(f"crop: {crop_name}")
    print(f"total expected yield: {total_yield:.2f}kg")
    print(f"total expected revenue: in rupees {total_revenue:.2f}")
    print(f"total cultivation cost: in rupees {total_cost:.2f}")
    if profit > 0:
        print(f"estimate profit: in rupees {profit:.2f}")
    elif profit == 0:
        print("no profit and no loss")
    else:
        print(f"estimated loss: in rupees {profit:.2f}")

if __name__ == "__main__":
     crop_profit_calculator()
