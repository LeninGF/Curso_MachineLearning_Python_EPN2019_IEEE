"""
Fecha: 26 -ago-2019

"""

#%% importar librerias
import numpy as np

#%% Funciones:
def signo(net):
    fsigno = [1. if elem >=0 else -1. for elem in net]
    return fsigno
def paso(net):
    fpaso = [1. if elem >= 0 else 0. for elem in net]
    return fpaso
def sigmoide(net):
    fsigmoide=1/(1+np.exp(elem) for elem in net)
    return fsigmoide
def tanhip(net):
    ftanhip=((np.exp(elem)-np.exp(-elem))/(np.exp(elem)+np.exp(-elem)) for elem in net )
    return ftanhip
def signo_escalar(net_escalar):
    y_pred = 1 if net_escalar >=0 else -1
    return y_pred

def iniciar_pesos(num_features):
    W = np.random.rand(num_features + 1)
    bias_val = np.random.random()
    W[2] = bias_val
    return W

def net(x_input, W):
    Net = np.dot(x_input, np.transpose(W))
    return Net

def funcion_error(y_verdadero, y_predicho):
    cont = 0
    for indice, y_i in enumerate(y_predicho):
        if y_i != y_verdadero[indice]:
            cont = cont+1
    return cont
def predecir(x,w_new):
    #Sacar la salida del perceptron para un x dado como deber
    net_final=net(x_input=x,w=w_new)
    y_final=signo_escalar(net_final)
    return y_final

#%% programa
# Definiendo el dataset de entrada
X = np.array([[-1, -1],
              [-1, 1],
              [1,-1],
              [1, 1]], dtype=np.float)

# Definiendo las salidas
Y = np.array([[-1],[1],[1],[1]], dtype=np.float)

samples, features = np.shape(X)  # samples = muestra/ ejemplo. features = característica
x_bias = -np.ones((samples,1))
X_comp = np.concatenate((X, x_bias), axis=1)

#---- Inicializacion de pesos
# W = np.random.rand(features+1)
# bias_val = np.random.random()
# W[2] = bias_val

W = iniciar_pesos(num_features=features)

#---- Calcular Net
# Net = np.dot(X_comp, np.transpose(W))
Net = net(x_input=X_comp, W=W)
#----

#---- signo
# signo_res = []
# for elem in Net:
#     if elem >=0:
#         signo_res.append(1.)
#     else:
#         signo_res.append(-1.)

Y_pred = signo(Net)

error_v = funcion_error(y_verdadero=Y, y_predicho=Y_pred)

# Algoritmo de Aprendizaje del Perceptron

print('error inicial {}'.format(error_v))

learning_rate = 0.01
epoca = 0
Num_Max_Epocas = 150
terminar = False

while(epoca<Num_Max_Epocas):
    # Entrenar el perceptron

    for indice, muestra in enumerate(X_comp):
        W_new = W+2*learning_rate*muestra*Y[indice]
        Net_new = net(X_comp, W=W_new)
        Y_pred_new = signo(net=Net_new)
        error_new = funcion_error(y_verdadero=Y, y_predicho=Y_pred_new)

        if error_new == 0:
            terminar = True
            break
        else:
            W = W_new
            continue
    print('Epoca {}, y_pred = {}, error = {}'.format(epoca, Y_pred_new, error_new))
    if terminar:
        break
    else:
        epoca += 1
        continue
X_new=np.array([1,-1,-1],dtype=np.float)
print('El modelo es: {}'.format(W_new))
y_predicha=predecir(X_new,W_new)
print('La y predicha es: {}'.format(y_predicha))
