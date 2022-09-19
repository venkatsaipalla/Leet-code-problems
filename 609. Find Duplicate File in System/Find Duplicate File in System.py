class File:
    def __init__(self, directory, raw_file):
        content_extraction_regex = "(?<=\()\w*(?=\))" # Wanted to have fun with regex
        file_name_extraction_regex = "[\w\.]*"
        extract = lambda text, regex: re.search(regex, text).group(0)
        
        self.directory = directory
        self.file_name = extract(raw_file, file_name_extraction_regex)
        self.content = extract(raw_file, content_extraction_regex)
        
    def get_full_path(self):
        return f"{self.directory}/{self.file_name}"

    def get_content_hash(self):
        return hash(self.content)
        

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = []
        for path in paths:
            directory, *raw_files = path.split(" ")
            for raw_file in raw_files:
                files.append(File(directory, raw_file))
        
        content_hash_map = defaultdict(list)
        for file in files:
            content_hash_map[file.get_content_hash()].append(file)
        
        answer = []
        for files_for_hash in content_hash_map.values():
            hash_duplicates = []
            if len(files_for_hash) <= 1:
                # no duplicate
                continue
            for file in files_for_hash:
                hash_duplicates.append(file.get_full_path())
            
            answer.append(hash_duplicates)
        return answer
