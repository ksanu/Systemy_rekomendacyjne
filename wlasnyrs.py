from systemomierz import recSystem

#Autor: Sebastian Szneider
#Data: 14.12.2016

#Wspomnijcie chociaż, że to moje bo mam u dr ocene do przepisania :P

class OwnRecSystem(recSystem):
    def __init__(self, dids1, inputArray):
        recSystem.__init__(self, dids1, inputArray, -1)

    def GetSystemName(self):
        return "Studentowy System Poleceniowy (bardzo przykładowy)"
            
    def processInputArray(self):
		#przetwarzanie danych wejsciowych (jakiekolwiek by one nie byly)
        self.inputDataProcessed = True
        
    def getQueryFloatResult(self, queryTuple):
		#prawdopodobienstwo ze uzyszkodnik user_id lubi film movie_id
		#jesli dr Szwabe sie nie mylil (a pewnie tak bylo) to wyniki moga miec dowolny zakres bo i tak sa sortowane
        prob = 0.0
        user_id = int(queryTuple[0]) - 1
        movie_id = int(queryTuple[1]) - 1
        return prob