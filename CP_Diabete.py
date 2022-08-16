'''Iago Taiyo Okuma de Azevedo
   Pedro Utida
   Pedro Costa
 ''' 
from logging import info, basicConfig, INFO
from cProfile import label
from pyexpat import features
import sklearn
from sklearn import tree
 
basicConfig(
    level=INFO,
    filename='c:/Users/iago_/Desktop/vscode/cp/github/ficha_pacientes.txt',
    filemode='a',
    encoding='UTF-8',
    format= "Data:%(asctime)s|%(levelname)s|Paciente:%(message)s"
)


print(("#"*50)+"\nBem-vindo Ao Dr. Diabetes\n"+("#"*50))

#Estatítica Glicemia dos paciêntes[jejum, pós-sobrecarga]:
#Glícemia normal[inferior à 100mg/DL, inferio à 140 mg/DL]
#Tolerância à glicose diminuida[100 - 126 mg/DL, 140 - 200 mg/DL]
#Diagnósticos de diabetes mellirus[+= 126mg/DL, +=200mg/DL]


features = [[33.3, 46.6], [66.6, 93.2], [99.9, 139.8],
            [101.6, 141], [117.2, 160], [125.8, 199.8],
            [126, 200], [150, 250], [200, 300]
            ]
labels = [0, 0, 0, 1, 1, 1, 2, 2, 2]

classifier = tree.DecisionTreeClassifier()
classifier.fit(features, labels)

print("="*50)
print("#"*5,"Menu principal","#"*5)

while True:
    print("Bem-Vindo ao teste de diabetes, por favor preencher sua ficha!")
    name = str(input("Insira o seu nome: "))
    age = int(input("Idade: "))
    print("Antes de iniciarmos, pedimos por gentileza que você fique de jejum antes do almoço para fazer o primeiro teste, e o segundo teste após o almoço(sobrecarga)")

    glicemiaJejum = str(input("Resultado do teste 1(jejum): "))
    glicemia_sobrecarga = str(input("Resultado do teste 2(sobrecarga): "))
    x = classifier.predict([[glicemiaJejum, glicemia_sobrecarga]])
    
    if x == 0:
        print("Glicemia está normal.")
        info("{}, {} anoes. OBS:Glicemia está normal.".format(name, age))
    elif x == 1:
        print("Sua glicose está no limite, recomendamos você procurar um profissional para controlar a sua glicemia.")
        info("{}, {} anos. OBS:Sua glicose está no limite, recomendamos você procurar um profissional para controlar a sua glicemia.".format(name, age))
    elif x == 2:
        print("Infelizmente com o resultado dos testes você está com diabetes, recomendamos que você procure um profissional para cuidar da sua diabete.")    
        info("{}, {} anos. OBS:Infelizmente com o resultado dos testes você está com diabetes, recomendamos que você procure um profissional para cuidar da sua diabete.".format(name, age))
    
    i = input("Obrigado por fazer o teste, deseja continuar?(s/n): ").upper()
    if i == "N":
        break