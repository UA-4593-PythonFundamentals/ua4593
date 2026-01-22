
__all__ = ["Name", "_age", "country"]

Name = "myall"
_age = 25
country = "USA"
is_student = False
height = 5.9
skills = ["Python", "Data Analysis", "Machine Learning"]

def get_profile():
    return {
        "Name": Name,
        "Age": _age,
        "Country": country,
        "Is Student": is_student,
        "Height": height,
        "Skills": skills
    }