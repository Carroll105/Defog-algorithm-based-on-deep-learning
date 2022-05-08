Path = 'data\1\';                   % 设置数据存放的文件夹路径
File = dir(fullfile(Path,'*.png'));  % 显示文 FileNames(k)件夹下所有符合后缀名为.txt文件的完整信息
FileNames = {File.name}';            % 提取符合后缀名为.txt的所有文件的文件名，转换为n行1列
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Length_Names = size(FileNames,1);    % 获取所提取数据文件的个数
for k = 1 : Length_Names
    % 连接路径和文件名得到完整的文件路径
    img_name = strcat(Path, FileNames(k));
    img_name = img_name{1}
    I=imread(img_name);
    I1 = imresize(I,[64,64]);
    %subplot(2,2,1);
    %figure(1);
    %imshow(I1);
    %imagesc(I1);
    I1=double(I1)/255;
    I = I1;

    Im_dealt = I;
    [row,col,z] = size(Im_dealt);
    landline = 0;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Iw = I;
    A = 0.8;
    m = 100;
    n = 300;
    tidx = 2;
	beta = 0.05;  %:0.05:0.15  % for beta = 0.20:0.05:0.30

    for i=1:3
        for j=landline+1:row
            for l=1:col
                d(j,l) = 1/((j-landline)^.05 + 0.0001);
                d2(j,l) = d(j,l)*8;
                if j < landline
                    d(j,l) = -0.04*landline + 18;
                    td(j,l) = exp(-beta*d(j,l));
                    Iw(j,l,i) = I(landline,l,i)*td(landline,l) + A*(1-td(j,l));

                else
                    d(j,l) = -0.04*sqrt((j-m).^2+(l-n).^2) + 17;
                    td(j,l) = exp(-beta*d(j,l));
                    Iw(j,l,i) = I(j,l,i)*td(j,l) + A*(1-td(j,l));
                end

            end
        end
    end
    for k = 1:landline
        for kj = 1:col
            Iw(k,kj,: ) = Iw(landline+1,100,:);
        end
    end
    %figure(tidx);imshow(Iw);
    filename = strcat('.\test\', img_name);
    %filename = filename{1};
    imwrite(Iw,filename);

    a = sprintf('%s %f','beta=',beta);
    title(a);
    tidx = tidx+1;
end