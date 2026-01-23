def recommend(rules, user_courses):
    matched_rules = rules[
        rules["antecedents"].apply(lambda x: x.issubset(user_courses))
    ]
    
    matched_rules = matched_rules.sort_values(['lift', 'confidence'], ascending=[False, False])
    
    recommended_courses = []
    seen = set(user_courses)
    
    for consequents in matched_rules['consequents']:
        for course in consequents:
            if course not in seen:
                recommended_courses.append(course)
                seen.add(course)
    
    return recommended_courses
