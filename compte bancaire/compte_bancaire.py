from typing import Self


class compte_bancaire :
    def __init__(self,interet, solde = 0.00):
        self.interet = interet
        self.solde = solde
    
    def deposer (self, montant):
        self.solde += montant
        return self

    def retirer (self, montant):
        if montant<self.solde:
          self.solde-=montant
        else:
            self.solde-5.00
            print( "solde insuffisant: retrait de 5$ frais")
            return self 
        
    def display_compte_info(self):
        print(f"solde: $"+str(self.balance))
        return self
    def yield_interet(self):
        self.solde+=self.solde*self.interet
        return self
        
account(0.05,500)
account(0.04,400)
    




    






        