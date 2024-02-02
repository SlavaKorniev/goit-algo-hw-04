def total_salary(path:str):
    
    total_salary = 0
    total_employers = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for lines in file.readlines():
                total_employers += 1
                
                content_line = lines.strip().split(",")
                total_salary += int(content_line [1])
                
        return total_salary, (total_salary / total_employers)
    
    except Exception as errors_file:
        print (errors_file)
    

total, average = total_salary("salary/salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")



