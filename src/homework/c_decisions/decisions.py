#Homework 3 decisions functions file

def get_options_ratio(option,total):
    ratio = int(option)/int(total)
    return ratio

def get_faculty_rating(ratio):
    if ratio >= .9 and ratio < 1:
        return "Excellent"
    
    elif ratio >= .8 and ratio < .9:
        return "Very Good"
        
    elif ratio >= .7 and ratio < .8:
        return "Good"
    
    elif ratio >= .6 and ratio <.7:
        return "Needs Improvement"
    
    elif ratio >= 0 and ratio <= .5999999999:
            return "Unacceptable"
