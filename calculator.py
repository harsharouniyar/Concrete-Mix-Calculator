def concrete_mix_calculator(volume, cement_ratio, sand_ratio, aggregate_ratio, wc_ratio):

    dry_volume = volume * 1.54

    total_parts = cement_ratio + sand_ratio + aggregate_ratio

    cement = (cement_ratio / total_parts) * dry_volume
    sand = (sand_ratio / total_parts) * dry_volume
    aggregate = (aggregate_ratio / total_parts) * dry_volume

    cement_bags = cement / 0.035
    cement_weight = cement_bags * 50

    water = wc_ratio * cement_weight

    strength = (cement_weight / water) * 10

    return cement_bags, sand, aggregate, water, strength
