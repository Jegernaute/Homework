import re

def get_cats_info(path):
    list_key = ["id", "name", "age"]
    finish_list = []

    try:
        with open(path, "r", encoding="utf-8") as cats:
            for line in cats.readlines():
                line = line.strip()
                line = re.sub(r"[^\s\w,]", ",", line)  
                line = line.split(",")
                cat_dict = {}

                for v, k in zip(line, list_key):
                    cat_dict[k] = v  
                    
                if len(cat_dict["id"]) == 24: 
                    try:
                        age = int(cat_dict["age"]) 
                        if age <= 38:  
                            finish_list.append(cat_dict)  
                    except ValueError:
                        print(f"Incorrect age format for id: {cat_dict['id']}") 
                else:
                   print(f"Incorrect id: {cat_dict['id']}") 

    except FileNotFoundError:
        print("Please check the file path or if the file exists")  

    return finish_list

cats_info = get_cats_info("./cats.txt")
print(cats_info)
