from typing import Optional

class Node:
    def __init__(self):
        self.children = {}
        self.isFile = False
        self.content = []


class FileSystem:

    def __init__(self):
        self.root = Node()

    def _parts(self, path: str) -> List[str]:
        return [part for part in path.split("/") if part]
    
    def _traverse(self, path: str, create: bool = False) -> Optional[Node]:

        node = self.root
        for part in self._parts(path):
            if part not in node.children:
                if not create:
                    return None
                node.children[part] = Node()

            node = node.children[part]
        return node

    def ls(self, path: str) -> List[str]:
        node = self._traverse(path)
        assert node is not None
        if node.isFile:
            return [self._parts(path)[-1]]
        return sorted(node.children.keys())


    def mkdir(self, path: str) -> None:
        self._traverse(path, create= True)
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._traverse(filePath, create= True)
        assert node is not None
        node.isFile = True
        node.content.append(content)
        

    def readContentFromFile(self, filePath: str) -> str:
        node = self._traverse(filePath)
        assert node is not None
        return "".join(node.content)
        

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
