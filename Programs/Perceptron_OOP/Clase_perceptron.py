class perceptron:

    def insert_matriz(self):
        # La mas sencilla e intuitiva
        self.numero_filas=2
        numero_columnas=2
        matriz = []
        for i in range(numero_filas):
            matriz.append([])
            for j in range(numero_columnas):
                print("Ingrese elemento:")
                matriz[i].append(input())
        print(matriz)

    def insert_arreglo(self):
        arr = []
        self.numero_filas = 2
        for i in range(self.numero_filas):
            print("Ingrese elemento:")
            arr.append(input())
        print(arr)
    def learn1(self):
        learn_rate = 0.1
        return learn_rate
    def learn2(self):
        learn_rate = 0.01
        return learn_rate
    def learn3(self):
        learn_rate = 0.001
        return learn_rate
    def numbers_learn(self,argument):
        switcher = {
            0: self.learn1,
            1: self.learn2,
            2: self.learn3,
        }
        return switcher.get(argument,lambda: "Invalid")

    def signo(self,net):
        fsigno = [1. if elem >=0 else -1. for elem in net]
        return fsigno
    def paso(self,net):
        fpaso = [1. if elem >= 0 else 0. for elem in net]
        return fpaso
    def sigmoide(self,net):
        fsigmoide=1/(1+np.exp(elem) for elem in net)
        return fsigmoide
    def tanhip(self,net):
        ftanhip=((np.exp(elem)-np.exp(-elem))/(np.exp(elem)+np.exp(-elem)) for elem in net )
        return ftanhip

    def funcion(self,argumento):
        switcher = {
            1: self.signo(),
            2: self.paso(),
            3: self.sigmoide(),
            4: self.tanhip(),
        }
    # Get the function from switcher dictionary
        return switcher.get(argumento, lambda: "Invalid")
