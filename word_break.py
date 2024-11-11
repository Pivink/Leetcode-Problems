def Break(s,wordDict):
   
   memo={}
   def dp(s):
      
      if len(s)==0:
         return True
      if s in memo:
         return memo[s]
      for i in wordDict:
         if s.startswith(i):
            if dp(s[len(i):]):
               memo[i]=True
               return True
      memo[s]=False
      return False
   return dp(s)

print(Break("applepenapple",["apple","pen"]))