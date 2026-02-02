import module
results = {}

if __name__ == "__main__":
    results["Rectangle area"] = module.rectangle_area(2,5)
    results["Triangle area"] = module.triangle_area(3,4)
    results["Circle area"] = module.circle_area(5)
    print(results)
