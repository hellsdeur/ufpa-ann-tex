clear all;
clc;

data = csvread('Quali_Bank.csv');

input = transpose(data(1:250,1:6));
output = transpose(data(1:250,7));

net = newff(input,output,30,{'logsig','tansig'},'trainlm');

net.divideFcn = 'divideind';
net.divideParam.trainInd = 1:1:176;
net.divideParam.valInd = 177:1:213;
net.divideParam.testInd = 214:1:250;

net = train(net,input,output);

p1 = input(:,214:250);
t1 = output(1,214:250);

a = sim(net,p1);

erro = a - t1;
erro = abs(erro);
conta = 0;
for i = 1:36;
    if erro(i) < 0.5
        conta = conta + 1;
    end
end
conta
plotconfusion(t1,a)