class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        hashmap = {}
        for equation in equations:
            l, r = equation[0], equation[-1]
            if l == r and equation[1:3] == '!=':
                return False
            if l in hashmap:
                if equation[1:3] == '==':
                    hashmap[l][0].add(r)
                else:
                    hashmap[l][1].add(r)
            else:
                if equation[1:3] == '==':
                    hashmap[l] = [{r}, set()]
                else:
                    hashmap[l] = [set(), {r}]
            if r in hashmap:
                if equation[1:3] == '==':
                    hashmap[r][0].add(l)
                else:
                    hashmap[r][1].add(l)
            else:
                if equation[1:3] == '==':
                    hashmap[r] = [{l}, set()]
                else:
                    hashmap[r] = [set(), {l}]
            if equation[1:3] == '==':
                res = hashmap[l][0].copy()
                res.update(hashmap[r][0])
                for r in res:
                    c = res.copy()
                    c.discard(r)
                    hashmap[r][0].update(c)
        res = set()
        for value in hashmap.values():
            res.update(value[0].intersection(value[1]))
        if len(res) > 0:
            return False
        return True
