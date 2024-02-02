def get_cats_info(path:str):
    
    cats_info = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for lines in file.readlines():
                content_dict = {}          
                content_line = lines.strip().split(",")
                # Заповнення словника
                content_dict ["id"] = content_line [0]
                content_dict ["name"] = content_line [1]
                content_dict ["age"] = content_line [2]

                # заповнення списку
                cats_info.append(content_dict)
                
        return cats_info
    
    except Exception as errors_file:
        print (errors_file)
    

cats_info = get_cats_info("cats_file.txt")
print(cats_info)