'''
Using custom class Node to indicate size of a folder, its parent folder, and whether the folder has been checked out (ls).
The has_ls is to ensure that the logic for counting folder size does not count the folder size more than once.
Caveats - I did not use full path name in my dict of folders. 
        - '..' is different for the root folder
'''
class Node:
    def __init__(self, size=0, prev=None, has_ls=False):
        self.size = size
        self.prev = prev
        self.has_ls = has_ls
    
    def __repr__(self) -> str:
        return f"Size {self.size}, prev {self.prev}, has_ls {self.has_ls}"


def add_path(curr, add):
    if add == '/':
        new = '/'
    elif curr == '/':
        new = curr + add
    else:
        new = curr + '/' + add
    return new


def f1(input, current_directory, directories):
    input = input.lstrip()
    if input[:2] == 'cd':
        cd_to = input[2:input.find('\n')].strip()
        if cd_to == '..':
            if current_directory == '/':
                return '/'
            else:
                return directories[current_directory].prev
        elif directories.get('/' + cd_to) != None:
            return '/' + cd_to
        else:
            new_directory = add_path(current_directory, cd_to)
            if directories.get(new_directory) == None:
                directories[new_directory] = Node(size=0, prev=None)
            current_directory = new_directory
    elif input[:2] == 'ls':
        if directories[current_directory].has_ls == True:
            folder = input.splitlines()[1:]
        else:
            directories[current_directory].has_ls = True
            folder = input.splitlines()[1:]
            for item in folder:
                if not item.startswith('dir'):
                    file_size, _ = item.split(' ')
                    traverse_directory = current_directory
                    while traverse_directory != None:
                        directories[traverse_directory].size += int(file_size)
                        traverse_directory = directories[traverse_directory].prev
                else:
                    _, folder_name = item.split(' ')
                    new_directory = add_path(current_directory, folder_name)
                    if directories.get(new_directory) == None:
                        directories[new_directory] = Node(size=0, prev=current_directory)
    return current_directory


def size_small_folders(directories):
    size_folders = 0
    for _, node in directories.items():
        if node.size <= 100000:
            size_folders += node.size
    return size_folders


def size_smallest_folder_constrained(directories):
    required_size = directories['/'].size - 40_000_000
    min_size = 10**9
    for _, node in directories.items():
        if node.size > required_size:
            if min_size > node.size:
                min_size = node.size
    return min_size
                

def main():
    with open("data/input_day7.txt", "r") as input:
        input = input.read().split('$')[1:]
    current_directory = '/'
    home = Node()
    directories = {current_directory: home}

    for result in input:
        current_directory = f1(result, current_directory, directories)

    print ('Total size of small folders:', size_small_folders(directories=directories))
    print ('Size of smallest big enough folder', size_smallest_folder_constrained(directories=directories))

if __name__ == '__main__':
    main()