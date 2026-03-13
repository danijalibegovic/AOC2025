def load_data(filename):
    with open(filename) as f:
        content = f.read().strip().split("\n\n")
        *shapes, regions = content
    return shapes, regions


def calculate_shape_sizes(shapes):
    return [sum(c == "#" for c in shape) for shape in shapes]


def parse_region(region):
    cleaned = region.replace("x", " ").replace(":", "").split(" ")
    values = list(map(int, cleaned))
    width = values[0]
    height = values[1]
    object_counts = values[2:]
    return width, height, object_counts


def can_fit_shapes(area, object_counts, shape_sizes):
    total_required_area = sum(count * size for count, size in zip(object_counts, shape_sizes))
    return area >= total_required_area


def main():
    shapes, regions = load_data("christmasTreeFarm.txt")
    shape_sizes = calculate_shape_sizes(shapes)
    
    valid_regions = 0
    for region in regions.split("\n"):
        width, height, object_counts = parse_region(region)
        region_area = width * height
        
        if can_fit_shapes(region_area, object_counts, shape_sizes):
            valid_regions += 1
    
    print(valid_regions)


if __name__ == "__main__":
    main()