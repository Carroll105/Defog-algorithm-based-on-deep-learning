% --------------------------------------------------------------------
% ��������
% --------------------------------------------------------------------
function m_special_fog_Callback(handles)
% hObject handle to m_special_fog (see GCBO)
% eventdata reserved - to be defined in a future version of MATLAB
% handles structure with handles and user data (see GUIDATA)
global img_src
m=size(img_src,1);
n=size(img_src,2);
r=img_src(:,:,1);
g=img_src(:,:,2);
b=img_src(:,:,3);
for i=2:m-10
    for j=2:n-10
        k=rand(1)*10; %����һ���������Ϊ�뾶
        di=i+round(mod(k,33)); %�õ����������
        dj=j+round(mod(k,33));%�õ����������
        rr(i,j)=r(di,dj); %��ԭ���ص���������ص����
        gg(i,j)=g(di,dj);
        bb(i,j)=b(di,dj);
    end
end
A(:,:,1)=rr;
A(:,:,2)=gg;
A(:,:,3)=bb;
axes(handles.axes_dst);
imshow(A)
set(handles.text,'String','����')