class Pokemon:
    def __init__(self, nom: str, type: str, caps : list, statut: str, stats: dict):
        self.nom = nom
        self.type = type
        self.caps = caps
        self.statut = statut
        self.stats = stats

    def utilise_sur(self, cap: Capacite, other: Pokemon):
        if self.stats['precision']