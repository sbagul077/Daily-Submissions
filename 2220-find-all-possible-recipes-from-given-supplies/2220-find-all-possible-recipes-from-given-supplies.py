class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        queue = deque() #to store supplies
        result = list() #output resultant list
        hashMap = dict() # supplies to reciepes mapping dependency list
        adjList = [0 for i in range(len(recipes))] # keep count of dependent nodes
        countMap= dict()

        for i in range(len(recipes)):
            recipe = recipes[i]
            items = ingredients[i]
  
            # adding items in dependency list and adjList
            for item in items:
                #is item is not present we add it as a key and value as list aling with the recipe
                if item not in hashMap.keys():
                    hashMap[item] = [recipe]
                #if already exist then we just add it in the list
                else:
                    hashMap.get(item).append(recipe)
                #we increment the value of each recipe by 1 for the items its dependent on
                adjList[i] += 1
            countMap[recipe] = i
    

        #adding items in queue for processing
        for supply in supplies:
            queue.append(supply)

        # we'll process the queue until it's empty
        while queue:
            ingredient = queue.popleft()
            # if that item in dependency list
            if ingredient in hashMap:
                li = hashMap.get(ingredient)

                #iterate over the dependent reciope
                for i in range(len(li)):
                    item = li[i]
                    #we reduce count by 1, we means we found 1 ingredient
                    if item in countMap:
                        index = countMap.get(item)
                        adjList[index] -= 1
                        #if in the adjList the count becomes which that recipe is ready and we 
                        #add it out the output result list and add it supplies
                        if adjList[index] == 0:
                            result.append(item)
                            queue.append(item)
        
        return result
                
#graph
#time complexity: O(E+V)
#Space Complexity: O(E+V)

