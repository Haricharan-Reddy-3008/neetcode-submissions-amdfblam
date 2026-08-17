class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        lst=path.split("/")

        for c in lst :
            if c=='..':
                if stack:
                    stack.pop()
            elif c != '.' and c != "":
                stack.append(c)
        return "/"+"/".join(stack)



        