Path = 'data\data_beta_0.1\1\';                   % 设置数据存放的文件夹路径
File = dir(fullfile(Path,'*.png'));  % 显示文 FileNames(k)件夹下所有符合后缀名为.txt文件的完整信息
FileNames = {File.name}';            % 提取符合后缀名为.txt的所有文件的文件名，转换为n行1列
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Length_Names = size(FileNames,1);    % 获取所提取数据文件的个数
for k = 1 : Length_Names
    img_name = strcat(Path, FileNames(k));
    img_name = img_name{1};
    img_name2 = strcat('test\SSR\data_beta_0.1\1\', FileNames(k));
    img_name2 = img_name2{1};
    test_SSR(img_name,img_name2)
end