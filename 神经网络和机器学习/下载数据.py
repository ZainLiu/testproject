import requests

content = requests.get('https://raw.githubusercontent.com/makeyourownneuralnetwork/makeyourownneuralnetwork/master/mnist_dataset/mnist_train_100.csv').content
with open('./mnist_train_100.csv', 'wb') as f:
    f.write(content)