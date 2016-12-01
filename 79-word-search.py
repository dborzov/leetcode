
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board)==0 or len(board[0])==0:
            return False
        if len(word)==0:
            return True
        def matching(pos, visited, i,j):
            if pos==len(word)-1:
                return True
            result = False
            visited[(i,j)] = True
            for pi, pj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if (pi<0) or (pi>=len(board)):
                    continue
                if (pj<0) or (pj>=len(board[0])):
                    continue
                if (pi,pj) in visited:
                    continue
                if board[pi][pj]==word[pos+1]:
                    if matching(pos+1,visited,pi,pj):
                        return True
            del visited[(i,j)]
            return result

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if word[0]==board[i][j]:
                    if matching(0,{},i,j):
                        return True
        return False

board = ["baabab","abaaaa","abaaab","ababba","aabbab","aabbba","aabaab"]

Solution().exist(board, "aabbbbabbaababaaaabababbaaba")
