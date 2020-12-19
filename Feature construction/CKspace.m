function CKspace_seq=CKspace(seqs)
%�����о���space����İ�����Խ��б���
%seqs ���о�������Ϊ��������,��������
%space ������Լ����
space_n=3; %�ܼ����
%amino =['A'    'C'    'D'    'E'    'F'    'G'    'H'  'I'    'K'  'L'    'M'    'N'    'P'    'Q'   'R'    'S'    'T'    'V'    'W'    'Y'   'X' ];
amino =['A'    'C'    'D'    'E'    'F'    'G'    'H'  'I'    'K'  'L'    'M'    'N'    'P'    'Q'   'R'    'S'    'T'    'V'    'W'    'Y'  ];
% matrix_code=zeros(length(amino),length(amino),size(seqs,1));
[m,n]=size(seqs);% mΪ������������nΪһ�������ʰ��������
M=zeros(m,length(amino)*length(amino),space_n);
for space=0:space_n-1 %n=5�������0,1,2,3,4��
    matrix_code=zeros(length(amino),length(amino),m);
    for j = 1:m
        seq_singal = seqs(j,:);  %ȡseqs��ÿһ�ж���ACKEF����EFCKA
        for i=1:n-space-1  %��matrix_code���л���space���������������
            a1=find(amino==seq_singal(i));
            a2=find(amino==seq_singal(i+space+1));
            matrix_code(a1,a2,j)=matrix_code(a1,a2,j)+1/(n-space-1);
        end
    end
    for k=1:m
        sub_code(k,:) = reshape(matrix_code(:,:,k)',1,length(amino)*length(amino));  %����AA��AC��AE�ȵȶ�Ӧ��һ��441��
    end
    M(:,:,space+1)=sub_code(:,:);%��sub_code�����ĸ����ųɼ���
end
CKspace_seq=zeros(m,length(amino)*length(amino)*space_n);
for i=1:m
    temp=[];
    for j=1:space_n
        temp=[temp M(i,:,j)];
    end
    CKspace_seq(i,:)=temp;
end