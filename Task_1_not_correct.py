def total_salary(path):
    import re
    from pathlib import Path
    
    total_salary = 0
    total_employers = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
            salarys = re.findall(r"\d+", content)
        
            for salary in salarys:
                total_salary += int(salary)
                total_employers += 1

                
    except Exception as errors_file:
        print (errors_file)
    
    return total_salary, (total_salary / total_employers)

total, average = total_salary("salary/salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")



