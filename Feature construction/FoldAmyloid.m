function FoldAmyloid_code=FoldAmyloid(Seq)
%导入Seq序列以及FoldAmyloid矩阵；输出编码结果
% Seq: N*M;
% FoldAmyloid:L*21;
% FoldAmyloid_code: N*(M*L);
% N: 行数,表示数据个数;
% M: 列数,表示序列长度;
% L: 选取的FoldAmyloid中的特征数目;
model=['A'    'R'    'N'    'D'    'C'    'Q'    'E'  ...
    'G'    'H'    'I'    'L'    'K'    'M'    'F' ...  
    'P'    'S'    'T'    'W'    'Y'    'V'   'X'];
FoldAmyloid=[19.89 21.03 18.49 17.41 23.52 19.23 17.46 17.11 21.72 25.71 25.36 17.67 24.82 27.18 17.43 18.19 19.81 28.48 25.93 23.93 20.73];
%% 指数数据归一化
[p,q]=size(FoldAmyloid);
FoldAmyloidscale=zeros(p,q);%归一化后的矩阵
    M1=max(FoldAmyloid(p,:));
    M2=min(FoldAmyloid(p,:));
    for b=1:q
        FoldAmyloidscale(p,b)=(FoldAmyloid(p,b)-M2)/(M1-M2);
    end
FoldAmyloidscale=FoldAmyloidscale';%转置得到21行的归一化矩阵;
%% 构造编码矩阵
[m,n]=size(Seq);
FoldAmyloid_code=[];
for i=1:m
    FoldAmyloid_row=[];
    for j=1:n
        for l=1:21 
            if Seq(i,j)==model(l)
                FoldAmyloid_ele=FoldAmyloidscale(l,:); 
                break;
            end
        end
        FoldAmyloid_row=[FoldAmyloid_row FoldAmyloid_ele];
    end
    FoldAmyloid_code= [FoldAmyloid_code; FoldAmyloid_row];
end
end