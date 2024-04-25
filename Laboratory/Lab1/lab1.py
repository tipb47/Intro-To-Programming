def computeShippingPrice(height, length, width, weight):
    return f'${(5 * height * length * width) + (0.5*weight)}'

if __name__ == "__main__":
    x = computeShippingPrice(7, 4, 5, 2.3)
    print(f'Computed shipping price: {x}')
    x2 = computeShippingPrice(73, 42, 51, 7)
    print(f'Computed shipping price: {x2}')