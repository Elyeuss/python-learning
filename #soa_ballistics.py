#soa_ballistics.py
def armor_material_adjustment(material):
    materials = {
        "aramid": 0.80,
        "uhmwpe": 0.77,
        "composite": 0.75,
        "steel": 0.70,
        "titanium": 0.60,
        "aluminum": 0.55,
        "ceramic": 0.50,
        "wood": 0.45,
        "glass": 0.25
    }

    return materials.get(material, 0)


def calculate_damage(ammo, armor, distance, limb_multiplier):
    damage = ammo["flesh_damage_max"]

    range_multiplier = min(
        1,
        (ammo["min_range"] / distance)
    )

    damage *= range_multiplier
    damage *= limb_multiplier

    return max(
        ammo["flesh_damage_min"],
        damage
    )

damage calculation (ammo, armor, distance, limb)
damage = ammo[fleshdamagemax]

range_multiplier = min