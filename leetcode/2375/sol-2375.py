class Solution(object):
    def smallestNumber(self, pan):
        pattern=pan
        x=[0 for i in range(len(pattern)+1)]
        f,i=1,0
        
        while i<len(pattern):
            if x[i]!=0:
                i+=1

            elif pattern[i]=="I" :
                x[i]=f
                f+=1
                if i==len(pattern)-1:
                    x[-1]=f
                    break
                i+=1

            else:
                i,f=self.rerun(i,f,pattern,x)
                i+=1
        if x[-1]==0:
            x[-1]=f

        return ''.join(map(str, x))

    def rerun(self,i,f,pattern,x):
        j=i+1
        if i==len(pattern)-1:
            x[i]=f+1
            x[j]=f
            f=f+2

        elif pattern[j]=="I":
            x[i]=f+1
            x[j]=f
            f=f+2

        else:
            m,f=self.rerun(j,f,pattern,x)
            x[i]=f
            f+=1
            
        return j,f
    
