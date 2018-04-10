class palindrome:
    
    def rev(self,str):# to reverse the input string
        r=""
        k=len(str)-1
        while k>=0:
            
            if (str[k]>='a' and str[k]<='z') or(str[k]>='A' and str[k]<='Z') or(str[k]>='0' and str[k]<='9'):
                r=r+str[k]
            
            k-=1
        return r
        
    def rem(self,str): # to ignore the special character
        v=""
        k=len(str)-1
        i=0
        while i<=k:
            
          
            
            if (str[i]>='a' and str[i]<='z') or(str[i]>='A' and str[i]<='Z')or(str[i]>='0' and str[i]<='9'):
                v=v+str[i]
            i+=1
        return v
        
    def com(self,a,b):# to compare the reverse and straight strings
        if (a.lower()==b.lower()):
            print("The input string is palindrom")
        else: 
            print("The input string is not palindrom")
        
ob=palindrome()
wr=open("palindrome1.txt","w")# this is to create a text file which contans input strings.
list=['Terralogic\n',"Madam I'm Adam\n",'A man, a plan, a canal: Panama\n']# creating a list with the delimeter \n
wr.writelines(list)
wr.close()
be=open("palindrome1.txt","r")
b=be.read().split("\n") #spliting the input strings from where the line is changing

for line in b: #passing the string line by line fron the list 
    if line=='':
        break
    revers=ob.rev(line)# calling the reverse function
    

    straight=ob.rem(line)
    
    ob.com(straight,revers)
be.close()


        
        
        
    

