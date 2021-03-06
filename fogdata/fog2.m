% --------------------------------------------------------------------
% 雾化处理
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
        k=rand(1)*10; %产生一个随机数作为半径
        di=i+round(mod(k,33)); %得到随机横坐标
        dj=j+round(mod(k,33));%得到随机纵坐标
        rr(i,j)=r(di,dj); %将原像素点用随机像素点代替
        gg(i,j)=g(di,dj);
        bb(i,j)=b(di,dj);
    end
end
A(:,:,1)=rr;
A(:,:,2)=gg;
A(:,:,3)=bb;
axes(handles.axes_dst);
imshow(A)
set(handles.text,'String','雾化')