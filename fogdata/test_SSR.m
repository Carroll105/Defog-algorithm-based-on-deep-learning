function test_SSR(filename, filename1)

I=imread(filename);

%I=imread('test.jpg');
 
Ir=I(:,:,1);%��ȡ��ɫ����
Ig=I(:,:,2);%��ȡ��ɫ����
Ib=I(:,:,3);%��ȡ��ɫ����
I1=SSR(Ir); %�Զ��嵥�߶�Retinex������
I2=SSR(Ig);
I3=SSR(Ib);
In=cat(3,I1,I2,I3);          %cat���ڹ����ά����

imwrite(In/256,filename1)
end
 
%�������������������������������ص㣡����������������������������������������������������������������������