# Solution 1: Hash Table
# Use the contents as keys and the paths as values to build a hash table.

# Time Complexity: O(NL)
# Space Complexity: O(NL)

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        Dict = dict()
        for path in paths:
            split_path = path.split(' ')
            directory = split_path[0]
            for i in range(1, len(split_path)):
                split_file = split_path[i].split('(')
                file_name = split_file[0]
                content = split_file[1]
                if content in Dict:
                    Dict[content].append(directory + '/' + file_name)
                else:
                    Dict[content] = [directory + '/' + file_name]
        return [x for x in Dict.values() if len(x) > 1]