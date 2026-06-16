class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check acyclic and connected
        # dfs check if there is back edge and connected
        # initialize from 0
        state = ["white" for _ in range(n)]
        pred = [None for _ in range(n)]
        trees = []
        global dfs_tree
        self.has_back_edge = False

        def find_adjacent_nodes(num):
            adjacent_nodes = []
            for edge in edges:
                new_edge = edge.copy()
                if num in new_edge:
                    new_edge.remove(num)
                    adjacent_nodes.append(new_edge.pop())

            if pred[num] in adjacent_nodes:
                adjacent_nodes.remove(pred[num])
            return adjacent_nodes


        def visit(num):
            global dfs_tree
            state[num] = "gray"
            adjacent_nodes = find_adjacent_nodes(num)
            print(self.has_back_edge)
            for node in adjacent_nodes:
                if state[node] == "white":
                    pred[node] = num
                    visit(node)
                elif state[node] == "gray":
                    self.has_back_edge = True

            state[num] = "black"
            dfs_tree.append(num)

        for node in range(n):
            if state[node] == "white":
                dfs_tree = []
                pred[node] = None
                visit(node)
                trees.append(dfs_tree)
        
        # print(trees)

        if len(trees) > 1 or self.has_back_edge:
            return False
        else:
            return True

            
        