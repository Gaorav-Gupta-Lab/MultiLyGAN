function CKspace_seq=CKspace(seqs)
%对序列矩阵按space间隔的氨基酸对进行编码
%seqs 序列矩阵，行数为序列条数,短肽数据
%space 氨基酸对间隔数
space_n=3; %总间隔数
%amino =['A'    'C'    'D'    'E'    'F'    'G'    'H'  'I'    'K'  'L'    'M'    'N'    'P'    'Q'   'R'    'S'    'T'    'V'    'W'    'Y'   'X' ];
amino =['A'    'C'    'D'    'E'    'F'    'G'    'H'  'I'    'K'  'L'    'M'    'N'    'P'    'Q'   'R'    'S'    'T'    'V'    'W'    'Y'  ];
% matrix_code=zeros(length(amino),length(amino),size(seqs,1));
[m,n]=size(seqs);% m为蛋白质条数，n为一条蛋白质氨基酸个数
M=zeros(m,length(amino)*length(amino),space_n);
for space=0:space_n-1 %n=5种情况【0,1,2,3,4】
    matrix_code=zeros(length(amino),length(amino),m);
    for j = 1:m
        seq_singal = seqs(j,:);  %取seqs的每一行短肽ACKEF或者EFCKA
        for i=1:n-space-1  %对matrix_code进行基于space的两个氨基酸编码
            a1=find(amino==seq_singal(i));
            a2=find(amino==seq_singal(i+space+1));
            matrix_code(a1,a2,j)=matrix_code(a1,a2,j)+1/(n-space-1);
        end
    end
    for k=1:m
        sub_code(k,:) = reshape(matrix_code(:,:,k)',1,length(amino)*length(amino));  %按照AA，AC，AE等等对应成一行441列
    end
    M(:,:,space+1)=sub_code(:,:);%将sub_code按短肽个数排成几行
end
CKspace_seq=zeros(m,length(amino)*length(amino)*space_n);
for i=1:m
    temp=[];
    for j=1:space_n
        temp=[temp M(i,:,j)];
    end
    CKspace_seq(i,:)=temp;
end