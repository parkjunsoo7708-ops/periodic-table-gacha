import random

# ── Rarity tiers ──────────────────────────────────────────────────────────────
# SSR  3%  – noble gases, precious/platinum-group metals, radioactive elements
# SR  17%  – transition metals, metalloids, halogens
# R   80%  – nonmetals, alkali/alkaline-earth metals, common post-transition metals

ELEMENTS = [
    # symbol, name, atomic number, rarity
    ("H",  "Hydrogen",      1,  "R"),
    ("He", "Helium",        2,  "SSR"),
    ("Li", "Lithium",       3,  "R"),
    ("Be", "Beryllium",     4,  "SR"),
    ("B",  "Boron",         5,  "SR"),
    ("C",  "Carbon",        6,  "R"),
    ("N",  "Nitrogen",      7,  "R"),
    ("O",  "Oxygen",        8,  "R"),
    ("F",  "Fluorine",      9,  "SR"),
    ("Ne", "Neon",         10,  "SSR"),
    ("Na", "Sodium",       11,  "R"),
    ("Mg", "Magnesium",    12,  "R"),
    ("Al", "Aluminum",     13,  "R"),
    ("Si", "Silicon",      14,  "R"),
    ("P",  "Phosphorus",   15,  "R"),
    ("S",  "Sulfur",       16,  "R"),
    ("Cl", "Chlorine",     17,  "SR"),
    ("Ar", "Argon",        18,  "SSR"),
    ("K",  "Potassium",    19,  "R"),
    ("Ca", "Calcium",      20,  "R"),
    ("Sc", "Scandium",     21,  "SR"),
    ("Ti", "Titanium",     22,  "SR"),
    ("V",  "Vanadium",     23,  "SR"),
    ("Cr", "Chromium",     24,  "SR"),
    ("Mn", "Manganese",    25,  "SR"),
    ("Fe", "Iron",         26,  "R"),
    ("Co", "Cobalt",       27,  "SR"),
    ("Ni", "Nickel",       28,  "SR"),
    ("Cu", "Copper",       29,  "SR"),
    ("Zn", "Zinc",         30,  "R"),
    ("Ga", "Gallium",      31,  "SR"),
    ("Ge", "Germanium",    32,  "SR"),
    ("As", "Arsenic",      33,  "SR"),
    ("Se", "Selenium",     34,  "SR"),
    ("Br", "Bromine",      35,  "SR"),
    ("Kr", "Krypton",      36,  "SSR"),
    ("Rb", "Rubidium",     37,  "SR"),
    ("Sr", "Strontium",    38,  "SR"),
    ("Y",  "Yttrium",      39,  "SR"),
    ("Zr", "Zirconium",    40,  "SR"),
    ("Nb", "Niobium",      41,  "SR"),
    ("Mo", "Molybdenum",   42,  "SR"),
    ("Tc", "Technetium",   43,  "SSR"),
    ("Ru", "Ruthenium",    44,  "SSR"),
    ("Rh", "Rhodium",      45,  "SSR"),
    ("Pd", "Palladium",    46,  "SSR"),
    ("Ag", "Silver",       47,  "SSR"),
    ("Cd", "Cadmium",      48,  "SR"),
    ("In", "Indium",       49,  "SR"),
    ("Sn", "Tin",          50,  "R"),
    ("Sb", "Antimony",     51,  "SR"),
    ("Te", "Tellurium",    52,  "SR"),
    ("I",  "Iodine",       53,  "SR"),
    ("Xe", "Xenon",        54,  "SSR"),
    ("Cs", "Cesium",       55,  "SR"),
    ("Ba", "Barium",       56,  "SR"),
    ("La", "Lanthanum",    57,  "SR"),
    ("Ce", "Cerium",       58,  "SR"),
    ("Pr", "Praseodymium", 59,  "SR"),
    ("Nd", "Neodymium",    60,  "SR"),
    ("Pm", "Promethium",   61,  "SSR"),
    ("Sm", "Samarium",     62,  "SR"),
    ("Eu", "Europium",     63,  "SR"),
    ("Gd", "Gadolinium",   64,  "SR"),
    ("Tb", "Terbium",      65,  "SR"),
    ("Dy", "Dysprosium",   66,  "SR"),
    ("Ho", "Holmium",      67,  "SR"),
    ("Er", "Erbium",       68,  "SR"),
    ("Tm", "Thulium",      69,  "SR"),
    ("Yb", "Ytterbium",    70,  "SR"),
    ("Lu", "Lutetium",     71,  "SR"),
    ("Hf", "Hafnium",      72,  "SR"),
    ("Ta", "Tantalum",     73,  "SR"),
    ("W",  "Tungsten",     74,  "SR"),
    ("Re", "Rhenium",      75,  "SR"),
    ("Os", "Osmium",       76,  "SSR"),
    ("Ir", "Iridium",      77,  "SSR"),
    ("Pt", "Platinum",     78,  "SSR"),
    ("Au", "Gold",         79,  "SSR"),
    ("Hg", "Mercury",      80,  "SR"),
    ("Tl", "Thallium",     81,  "SR"),
    ("Pb", "Lead",         82,  "R"),
    ("Bi", "Bismuth",      83,  "SR"),
    ("Po", "Polonium",     84,  "SSR"),
    ("At", "Astatine",     85,  "SSR"),
    ("Rn", "Radon",        86,  "SSR"),
    ("Fr", "Francium",     87,  "SSR"),
    ("Ra", "Radium",       88,  "SSR"),
    ("Ac", "Actinium",     89,  "SSR"),
    ("Th", "Thorium",      90,  "SSR"),
    ("Pa", "Protactinium", 91,  "SSR"),
    ("U",  "Uranium",      92,  "SSR"),
    ("Np", "Neptunium",    93,  "SSR"),
    ("Pu", "Plutonium",    94,  "SSR"),
]

RARITY_WEIGHTS = {
    "SSR": 3,
    "SR":  17,
    "R":   80,
}


def gacha(draw_pool=None):
    """
    Perform a gacha draw and return one element.

    Args:
        draw_pool: Optional list of dicts, each with keys:
                       'symbol', 'name', 'atomic_number', 'rarity'
                   Defaults to all 94 elements defined above.

    Returns:
        dict with keys: symbol, name, atomic_number, rarity
    """
    if draw_pool is None:
        draw_pool = [
            {
                "symbol":        sym,
                "name":          name,
                "atomic_number": num,
                "rarity":        rarity,
            }
            for sym, name, num, rarity in ELEMENTS
        ]

    if not draw_pool:
        raise ValueError("draw_pool cannot be empty")

    # Step 1 – pick a rarity tier based on overall probabilities
    rarity_roll = random.random()  # [0.0, 1.0)

    if rarity_roll < 0.03:
        chosen_rarity = "SSR"
    elif rarity_roll < 0.20:   # 0.03 + 0.17
        chosen_rarity = "SR"
    else:
        chosen_rarity = "R"

    # Step 2 – filter pool to that tier; fall back to full pool if tier is empty
    tier_pool = [item for item in draw_pool if item.get("rarity") == chosen_rarity]
    if not tier_pool:
        tier_pool = draw_pool

    # Step 3 – uniform draw within the tier (each element equally likely)
    return random.choice(tier_pool)


# ── Example usage ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    items = ["SSR", "SR", "R"]
    probabilities = [3, 17, 80]   # percent chance per tier

    print("Single draw:")
    result = gacha()
    print(f"  [{result['rarity']}] {result['symbol']} – {result['name']} (Z={result['atomic_number']})")

    print("\n10-pull:")
    for _ in range(10):
        r = gacha()
        print(f"  [{r['rarity']}] {r['symbol']:2s} – {r['name']}")
