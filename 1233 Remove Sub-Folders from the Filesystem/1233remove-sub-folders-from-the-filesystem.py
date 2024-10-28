class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        uniq = set()
        folder.sort(key=len)

        for f in folder:

            for i in range(2, len(f)):
                if f[i] == '/' and f[:i] in uniq:
                    break
            else:
                uniq.add(f)

        return list(uniq)



        