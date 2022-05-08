function test_SSR(filename, filename1)

I=imread(filename);

%I=imread('test.jpg');
 
Ir=I(:,:,1);%提取红色分量
Ig=I(:,:,2);%提取绿色分量
Ib=I(:,:,3);%提取蓝色分量
I1=SSR(Ir); %自定义单尺度Retinex处理函数
I2=SSR(Ig);
I3=SSR(Ib);
In=cat(3,I1,I2,I3);          %cat用于构造多维数组

imwrite(In/256,filename1)
end
 
%——————————————划重点！！！！！！！！！！！！！！！！！！！！————————————————