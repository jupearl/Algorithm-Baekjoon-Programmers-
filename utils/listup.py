import os


def problem_source_code():
    py_problem_list = []
    java_problem_list = []

    for files in os.walk("../백준/"):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.py':
                py_problem_list.append(filename[:-3])
            if ext == '.java':
                java_problem_list.append(filename[:-5])
    
    return py_problem_list, java_problem_list


def make_read_me(py_name_list, java_name_list):
    return f"""# Baekjoon
<img src="https://img.shields.io/badge/python-3776AB?style=flat&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/-JAVA-007396?style=flat&logo=OpenJDK&logoColor=white"> 
자동으로 푼 문제 리스트업도 가능하게 매크로 설정해두었음. 

- Python 문제 리스트업   
{','.join(py_name_list)}

- Java 문제 리스트업   
{','.join(java_name_list)}
"""


def update_readme_md():
    py_name_list, java_name_list = problem_source_code()

    readme = make_read_me(py_name_list=py_name_list, java_name_list=java_name_list)

    return readme


if __name__ == "__main__":
    readme = update_readme_md()
    with open("../README.md", 'w', encoding='utf-8') as f:
        f.write(readme)
