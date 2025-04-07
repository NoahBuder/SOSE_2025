class Pferd():#

    #Konstruktor
    def init(self, mein_Name, meine_groesse):
        print("Hier wird ein Pferd geboren!")
        print("Das Pferd ist ", meine_groesse)


        #Das erste Attribut hinzufügen
        self.groesse = meine_groesse
        self.name = mein_Name


    def sich_vorstellen(self):
        print("Ich bin", self.name, "und bin", self.groesse, "groß!")

    def laufen(self, meine_geschwindigkeit):
        print("ich laufe mit", meine_geschwindigkeit)

#Instanziierung eines Objekts

#Self müssen wir nie übergeben!
pf1 = Pferd("Beauty", "1,70 m")
pf2 = Pferd("Black", "2,20 m")

pf1.sich_vorstellen()
pf2.sich_vorstellen()

pf1.laufen("30km/h")
print(pf1.geschwindigkeit)
#print(pf1.groesse)
#print(pf2.groesse)

#print(pf1.name, "ist", pf1.groesse)
#print(pf2.name, "ist", pf2.groesse)
