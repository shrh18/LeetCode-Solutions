class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        ingToRec = defaultdict(set)
        recReqIng = defaultdict(set)
        ret = set()
        supplies = deque(supplies)

        for idx, recipe in enumerate(recipes):
            for ing in ingredients[idx]:
                ingToRec[ing].add(recipe)
                recReqIng[recipe].add(ing)
        
        while len(supplies)>0:
            ing = supplies.popleft()

            if len(ingToRec[ing]) == 0:
                continue

            for rec in ingToRec[ing]:
                recReqIng[rec].remove(ing)
                if len(recReqIng[rec]) == 0:
                    ret.add(rec)
                    if rec in ingToRec:
                        supplies.append(rec)

        return list(ret)