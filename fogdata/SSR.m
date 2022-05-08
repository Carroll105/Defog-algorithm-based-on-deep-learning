function A = SSR(I)
G=I;
[m,n]=size(I);
I=double(I);
x0=floor((m+1)/2);y0=floor((n+1)/2);
c = 200;
K=1/(sqrt(2*pi)*c);
for x=1:m
    for y=1:n
            G(x,y)=K*(exp(-((x-x0)^2+(y-y0)^2)/(2*c^2))); %��˹����
    end
end
 
Gfft=fft2(G);
Ifft=fft2(I);
Lfft=Gfft.*Ifft;
L=ifft2(Lfft);
 
r=log(I+1)-log(L+1);                   %��1��Ϊ�˷�ֹ����Ϊ0ʱ��log0û�ж���
 
%�������죬���Ҷȷ�Χת����0-255����ֱ���󷴶�����Ч�����ã�
MIN=min(min(r));
MAX=max(max(r));
new=(r-MIN)*255/(MAX-MIN);
A=new;
end
