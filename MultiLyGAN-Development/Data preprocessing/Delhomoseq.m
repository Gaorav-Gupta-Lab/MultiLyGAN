function [Seq,ID,Site]=Delhomoseq(Seqs,Did,Dsite)
%去除同源后相应的id和site、sequences也删除
[m,n]=size(Seqs);
k=1;
while(k<m-1)
    f=Seqs(k,:);
    de=[];
    for i=k+1:m
        s=f-Seqs(i,:);
        z=find(s==0);
 rate=length(z);      
        if rate>=n*0.3       %去除40%的同源蛋白序列
            de=[de,i];
        end        
    end
    Seqs(de,:)=[];
    Did(de,:)=[];
    Dsite(de,:)=[];
   [m,n]=size(Seqs);
    k=k+1;
end
Seq=Seqs;
ID=Did;
Site=Dsite;
        