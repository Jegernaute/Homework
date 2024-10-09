import re
def total_salary(path):
    
    total = 0
    count = 0
    
    try:
    
        with open(path, 'r', encoding="utf-8") as file:
            
            for line in file.readlines():
                line = line.strip()
                line = re.sub(r"[^\s\w,]", ",", line)
                _,  line = line.split(",")
                total += int(line)
                count += 1
                average =  total / count
    
    except FileNotFoundError:
        print("Please check the file path or if the file exists")  

    return print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
        
    
            
total_salary('./salary.txt')





