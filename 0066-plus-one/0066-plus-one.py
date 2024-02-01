class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for i in range(len(digits)):
            num=num*10+int(digits[i])
        List_new=[]
        num=num+1
        while num!=0:
            List_new.insert(0,num%10)
            num=num//10
            
            
        return List_new