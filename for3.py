###########

all_scores = [
    {'school_class':'1a','scores':[4,5,2,3,2]},
    {'school_class':'1b','scores':[5,3,2,4,5]},
    {'school_class':'2a','scores':[2,3,4,2,4]},
    {'school_class':'2b','scores':[5,4,4,5,5]}
]

school_scores_sum = 0
school_scores_quant = 0
for score_avg in all_scores:
    class_scores_sum = 0
    class_scores_sum = sum(score_avg['scores'])
    print(class_scores_sum)
    class_scores_avg = class_scores_sum / len(score_avg["scores"])
    print(f"Средняя оценка по классу {class_scores_avg}")
    school_scores_quant += len(score_avg["scores"])
    school_scores_sum += class_scores_sum
school_scores_avg = school_scores_sum / school_scores_quant
print('-----------------------')
print(f"Средняя оценка по школе {school_scores_avg}")
