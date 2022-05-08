function A = SSR(I)
G=I;
[m,n]=size(I);
I=double(I);
x0=floor((m+1)/2);y0=floor((n+1)/2);
c = 200;
K=1/(sqrt(2*pi)*c);
for x=1:m
    for y=1:n
            G(x,y)=K*(exp(-((x-x0)^2+(y-y0)^2)/(2*c^2))); %高斯函数
    end
end
 
Gfft=fft2(G);
Ifft=fft2(I);
Lfft=Gfft.*Ifft;
L=ifft2(Lfft);
 
r=log(I+1)-log(L+1);                   %加1是为了防止对数为0时，log0没有定义
 
%线性拉伸，将灰度范围转换到0-255，（直接求反对数的效果不好）
MIN=min(min(r));
MAX=max(max(r));
new=(r-MIN)*255/(MAX-MIN);
A=new;
end
