from collections import defaultdict

class Atomos:

    """Represetação Bosica da Classe Atomos"""

    propriedades = [
        {"nome": "Hidrogenio", "sigla": "H", "massa atômica": 1.008},
        {"nome": "Helio", "sigla": "He", "massa atômica": 4.003},
        {"nome": "Litio", "sigla": "Li", "massa atômica": 6.941},
        {"nome": "Berilio", "sigla": "Be", "massa atômica": 9.012},
        {"nome": "Boro", "sigla": "B", "massa atômica": 10.81},
        {"nome": "Carbono", "sigla": "C", "massa atômica": 12.01},
        {"nome": "Nitrogenio", "sigla": "N", "massa atômica": 14.01},
        {"nome": "Oxigenio", "sigla": "O", "massa atômica": 16.00},
        {"nome": "Fluor", "sigla": "F", "massa atômica": 19.00},
        {"nome": "Neonio", "sigla": "Ne", "massa atômica": 20.18},
        {"nome": "Sodio", "sigla": "Na", "massa atômica": 22.99},
        {"nome": "Magnesio", "sigla": "Mg", "massa atômica": 24.31},
        {"nome": "Aluminio", "sigla": "Al", "massa atômica": 26.98},
        {"nome": "Silicio", "sigla": "Si", "massa atômica": 28.09},
        {"nome": "Fosforo", "sigla": "P", "massa atômica": 30.97},
        {"nome": "Enxofre", "sigla": "S", "massa atômica": 32.065},
        {"nome": "Cloro", "sigla": "Cl", "massa atômica": 35.45},
        {"nome": "Argon", "sigla": "Ar", "massa atômica": 39.95},
        {"nome": "Potossio", "sigla": "K", "massa atômica": 39.10},
        {"nome": "Colcio", "sigla": "Ca", "massa atômica": 40.08},
        {"nome": "Escandio", "sigla": "Sc", "massa atômica": 44.96},
        {"nome": "Titanio", "sigla": "Ti", "massa atômica": 47.87},
        {"nome": "Vanodio", "sigla": "V", "massa atômica": 50.94},
        {"nome": "Cromio", "sigla": "Cr", "massa atômica": 52.00},
        {"nome": "Manganes", "sigla": "Mn", "massa atômica": 54.94},
        {"nome": "Ferro", "sigla": "Fe", "massa atômica": 55.85},
        {"nome": "Cobalto", "sigla": "Co", "massa atômica": 58.93},
        {"nome": "Niquel", "sigla": "Ni", "massa atômica": 58.69},
        {"nome": "Cobre", "sigla": "Cu", "massa atômica": 63.55},
        {"nome": "Zinco", "sigla": "Zn", "massa atômica": 65.38},
        {"nome": "Galio", "sigla": "Ga", "massa atômica": 69.72},
        {"nome": "Germanio", "sigla": "Ge", "massa atômica": 72.63},
        {"nome": "Arsenio", "sigla": "As", "massa atômica": 74.92},
        {"nome": "Selenio", "sigla": "Se", "massa atômica":78.96},
        {"nome": "Bromo", "sigla": "Br", "massa atômica":79.90},
        {"nome": "Kripton", "sigla": "Kr", "massa atômica":83.79},
        {"nome": "Rubidio", "sigla": "Rb", "massa atômica":85.46},
        {"nome": "Estroncio", "sigla": "Sr", "massa atômica":87.62},
        {"nome": "itrio", "sigla": "Y", "massa atômica":88.90},
        {"nome": "Zirconio", "sigla": "Zr", "massa atômica":91.22},
        {"nome": "Niobio", "sigla": "Nb", "massa atômica":92.90},
        {"nome": "Molibdenio", "sigla": "Mo", "massa atômica":95.95},
        {"nome": "Tecnecio", "sigla": "Tc", "massa atômica":98},
        {"nome": "Rutenio", "sigla": "Ru", "massa atômica":101.07},
        {"nome": "Rodio", "sigla": "Rh", "massa atômica":102.91},
        {"nome": "Palodio", "sigla": "Pd", "massa atômica":106.42},
        {"nome": "Prata", "sigla": "Ag", "massa atômica":107.87},
        {"nome": "Codmio", "sigla": "Cd", "massa atômica":112.41},
        {"nome": "indio", "sigla": "In", "massa atômica":114.82},
        {"nome": "Estanho", "sigla": "Sn", "massa atômica":118.71},
        {"nome": "Antimonio", "sigla": "Sb", "massa atômica": 121.76},
        {"nome": "Telurio", "sigla": "Te", "massa atômica": 127.60},
        {"nome": "Iodeto", "sigla": "I", "massa atômica": 126.9},
        {"nome": "Xenonio", "sigla": "Xe", "massa atômica": 131.29},
        {"nome": "Cesio", "sigla": "Cs", "massa atômica": 132.91},
        {"nome": "Bario", "sigla": "Ba", "massa atômica": 137.33},
        {"nome": "Lantanio", "sigla": "La", "massa atômica": 138.91},
        {"nome": "Cerio", "sigla": "Ce", "massa atômica": 140.12},
        {"nome": "Praseodimio", "sigla": "Pr", "massa atômica": 140.91},
        {"nome": "Neodimio", "sigla": "Nd", "massa atômica": 144.24},
        {"nome": "Promecio", "sigla": "Pm", "massa atômica": 145.0},
        {"nome": "Samorio", "sigla": "Sm", "massa atômica": 150.36},
        {"nome": "Europio", "sigla": "Eu", "massa atômica": 152.0},
        {"nome": "Gadolinio", "sigla": "Gd", "massa atômica": 157.25},
        {"nome": "Terbio", "sigla": "Tb", "massa atômica": 158.93},
        {"nome": "Disprosio", "sigla": "Dy", "massa atômica": 162.50},
        {"nome": "Holmio", "sigla": "Ho", "massa atômica": 164.93},
        {"nome": "Erbio", "sigla": "Er", "massa atômica": 167.26},
        {"nome": "Tulerio", "sigla": "Tm", "massa atômica": 168.93},
        {"nome": "Iterbio", "sigla": "Yb", "massa atômica": 173.04},
        {"nome": "Lutecio", "sigla": "Lu", "massa atômica": 175.0},
        {"nome": "Hafnio", "sigla": "Hf", "massa atômica": 178.49},
        {"nome": "Tantalo", "sigla": "Ta", "massa atômica": 180.95},
        {"nome": "Tungstenio", "sigla": "W", "massa atômica": 183.84},
        {"nome": "Renio", "sigla": "Re", "massa atômica": 186.21},
        {"nome": "osmio", "sigla": "Os", "massa atômica": 190.23},
        {"nome": "Iridio", "sigla": "Ir", "massa atômica": 192.22},
        {"nome": "Platina", "sigla": "Pt", "massa atômica": 195.08},
        {"nome": "Ouro", "sigla": "Au", "massa atômica":196.97},
        {"nome": "Mercurio", "sigla": "Hg", "massa atômica": 200.59},
        {"nome": "Tolio", "sigla": "Tl", "massa atômica": 204.38},
        {"nome": "Chumbo", "sigla": "Pb", "massa atômica": 207.2},
        {"nome": "Bismuto", "sigla": "Bi", "massa atômica": 209.0},
        {"nome": "Polonio", "sigla": "Po", "massa atômica": 209.0},
        {"nome": "Astato", "sigla": "At", "massa atômica": 210.0},
        {"nome": "Radonio", "sigla": "Rn", "massa atômica": 222.0},
        {"nome": "Francio", "sigla": "Fr", "massa atômica": 223.0},
        {"nome": "Radium", "sigla": "Ra", "massa atômica": 226.0},
        {"nome": "Actinio", "sigla": "Ac", "massa atômica": 227.0},
        {"nome": "Torio", "sigla": "Th", "massa atômica": 232.04},
        {"nome": "Protactinio", "sigla": "Pa", "massa atômica": 231.04},
        {"nome": "Urano", "sigla": "U", "massa atômica": 238.03},
        {"nome": "Neptunio", "sigla": "Np", "massa atômica": 237.0},
        {"nome": "Plutonio", "sigla": "Pu", "massa atômica": 244.0},
        {"nome": "Americio", "sigla": "Am", "massa atômica": 243.0},
        {"nome": "Curio", "sigla": "Cm", "massa atômica": 247.0},
        {"nome": "Berquelio", "sigla": "Bk", "massa atômica": 247.0},
        {"nome": "Californio", "sigla": "Cf", "massa atômica": 251.0},
        {"nome": "Einstenio", "sigla": "Es", "massa atômica": 252.0},
        {"nome": "Fermio", "sigla": "Fm", "massa atômica": 257.0},
        {"nome": "Mendelevio", "sigla": "Md", "massa atômica": 258.0},
        {"nome": "Nobelio", "sigla": "No", "massa atômica": 259},
        {"nome": "Laurencio", "sigla": "Lr", "massa atômica": 262.0},
        {"nome": "Rutherfordio", "sigla": "Rf", "massa atômica": 261.0},
        {"nome": "Dubnium", "sigla": "Db", "massa atômica": 262.0},
        {"nome": "Seaborgio", "sigla": "Sg", "massa atômica": 266.0},
        {"nome": "Bohrio", "sigla": "Bh", "massa atômica": 264.0},
        {"nome": "Hossio", "sigla": "Hs", "massa atômica": 277.0},
        {"nome": "Meitnerio", "sigla": "Mt", "massa atômica": 268.0},
        {"nome": "Darmstodio", "sigla": "Ds", "massa atômica": 281.0},
        {"nome": "Roentgenio", "sigla": "Rg", "massa atômica": 280.0},
        {"nome": "Copernicio", "sigla": "Cn", "massa atômica": 285.0},
        {"nome": "Nihonio", "sigla": "Nh", "massa atômica": 286.0},
        {"nome": "Flerovio", "sigla": "Fl", "massa atômica": 289.0},
        {"nome": "Moscovio", "sigla": "Mc", "massa atômica": 289.0},
        {"nome": "Livermorio", "sigla": "Lv", "massa atômica": 293.0},
        {"nome": "Tennessine", "sigla": "Ts", "massa atômica": 294.0},
        {"nome": "Oganessonio", "sigla": "Og", "massa atômica": 294.0},
    ]


if __name__ == "__main__":
    print(Atomos.propriedades)