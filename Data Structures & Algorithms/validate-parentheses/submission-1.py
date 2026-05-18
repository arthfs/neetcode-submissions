class Solution:
    def isValid(self, s: str) -> bool:
        ref = []
        for l in s:
            if l in ['(', '{', '[']:
                ref.append(l)
            else:
                try:
                    if l == ')' and ref[-1]!= '(':
                        return False
                    
                    if l == ']' and ref[-1]!= '[':
                        return False
                    
                    if l == '}' and ref[-1]!= '{':
                        return False

                    ref.pop()
                    
                except:
                    return False
        return ref == []