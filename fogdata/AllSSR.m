Path = 'data\data_beta_0.1\1\';                   % �������ݴ�ŵ��ļ���·��
File = dir(fullfile(Path,'*.png'));  % ��ʾ�� FileNames(k)���������з��Ϻ�׺��Ϊ.txt�ļ���������Ϣ
FileNames = {File.name}';            % ��ȡ���Ϻ�׺��Ϊ.txt�������ļ����ļ�����ת��Ϊn��1��
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Length_Names = size(FileNames,1);    % ��ȡ����ȡ�����ļ��ĸ���
for k = 1 : Length_Names
    img_name = strcat(Path, FileNames(k));
    img_name = img_name{1};
    img_name2 = strcat('test\SSR\data_beta_0.1\1\', FileNames(k));
    img_name2 = img_name2{1};
    test_SSR(img_name,img_name2)
end