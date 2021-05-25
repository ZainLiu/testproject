import time

import numpy


class NeuralNetwork:
    """
    定义神经网络类
    """

    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        """
        初始化
        """
        # 输入层、隐藏层、输出层
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        # 学习率
        self.lr = learningrate

        # 网络核心
        # 权重矩阵,减去0.5为了均匀数据均匀分布在 [-1,1]
        # self.wih = (numpy.random.rand(self.hnodes, self.inodes) - 0.5)
        # self.who = (numpy.random.rand(self.onodes, self.hnodes) - 0.5)

        # 比较复杂的权重
        # 正态概率分布采样权重，其中平均值为0，标准方差为节点传入链接数目的开方，
        # 即1/根号(传入连接数目)
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

        # 更复杂的权重 Xavier Glorot
        # todo:Xavier初始权重

        # 激活函数，Sigmoid函数
        # self.activation_func = lambda x: scipy.special.expit(x)
        self.activation_func = lambda x: 1 / (1 + numpy.exp(-x))

    def train(self, inputs_list, targets_list):
        """
        训练
        :return:
        """
        # part 1,针对训练样本输出
        inputs = numpy.array(inputs_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_func(hidden_inputs)
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_func(final_inputs)

        # part 2,反向误差传导,更改权重
        targets = numpy.array(targets_list, ndmin=2).T
        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.who.T, output_errors)

        self.who += self.lr * numpy.dot(
            (output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs)
        )

        self.wih += self.lr * numpy.dot(
            (hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs)
        )

    def train2(self, inputs_list, targets_list):
        """
        利用hessian矩阵计算
        :param inputs_list:
        :param targets_list:
        :return:
        """
        pass

    def query(self, inputs_list):
        """
        函数接受神经网络的输入，返回网络的输出
        :return:
        """
        inputs = numpy.array(inputs_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_func(hidden_inputs)
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_func(final_inputs)
        return final_outputs


# mnist,数字识别，0-9 共 10 个输出

inodes = 784  # 28*28 的输入
hnodes = 100  # 100个隐藏层
onodes = 10  # 10 个输出

learningrate = 0.3  # 学习率

nnc = NeuralNetwork(inodes, hnodes, onodes, learningrate)

"""
数据集：
https://pjreddie.com/media/files/mnist_train.csv
测试集：
https://pjreddie.com/media/files/mnist_test.csv
100训练集：
https://raw.githubusercontent.com/makeyourownneuralnetwork/makeyourownneuralnetwork/master/mnist_dataset/mnist_train_100.csv
10测试集：
https://raw.githubusercontent.com/makeyourownneuralnetwork/makeyourownneuralnetwork/master/mnist_dataset/mnist_test_10.csv
"""

# 读取训练数据
training_data_file = open('./mnist_train_100.csv', 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

start_time = time.time()
# 训练
for record in training_data_list:
    all_values = record.split(',')
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    targets = numpy.zeros(onodes) + 0.01
    targets[int(all_values[0])] = 0.99
    nnc.train(inputs, targets)

# 读取测试数据
test_data_file = open('./mnist_test_10.csv', 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

# 测试
scorecard = []
for record in test_data_list:
    all_values = record.split(',')
    correct_label = int(all_values[0])
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    outputs = nnc.query(inputs)
    label = numpy.argmax(outputs)
    print('标签:', correct_label, '网络输出:', label)
    if correct_label == label:
        scorecard.append(1)
    else:
        scorecard.append(0)
scorecard_array = numpy.asfarray(scorecard)
print('准确率：', scorecard_array.sum() / scorecard_array.size)

end_time = time.time()

print('消耗时间', end_time - start_time)