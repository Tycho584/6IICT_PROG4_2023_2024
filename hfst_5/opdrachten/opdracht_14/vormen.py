class Rechthoek:
  def __init__(self, breedte, hoogte):
    self.breedte = breedte
    self.hoogte = hoogte
  
  def set_breedte(self, breedte):
    self.breedte = breedte
  def set_hoogte(self, hoogte):
    self.hoogte  = hoogte
  def get_oppervlakte(self):
    return self.breedte*self.hoogte
  def get_omtrek(self):
    return 2*self.breedte+2*self.hoogte
  
  def afbeelding(self):
    tekst = ""
    for _ in range(self.hoogte):
      for _ in range(self.breedte):
        tekst += "*"
      tekst += "\n"
    print(tekst)
            
  def get_hoeveel_binnen(self, recht):
    past_breedte = self.breedte//recht.breedte
    past_hoogte  = self.hoogte//recht.hoogte
    return past_breedte*past_hoogte



class Vierkant(Rechthoek):
  def __init__(self, zijde):
    super().__init__(zijde,zijde)

  def set_breedte(self, breedte):
    super().set_breedte(breedte)
    super().set_hoogte(breedte)
  def set_hoogte(self, hoogte):
    super().set_hoogte(hoogte)
    super().set_breedte(hoogte)
  def set_zijde(self, zijde):
    super().set_breedte(zijde)
    super().set_hoogte(zijde)


class Ruit(Rechthoek):
    pass

