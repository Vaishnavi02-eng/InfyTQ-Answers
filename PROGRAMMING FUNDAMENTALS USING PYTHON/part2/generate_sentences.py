#lex_auth_0127136011356405761166

def generate_sentences(subjects,verbs,objects):
    sentence_list=[]
    for i in range(0,len(subjects)):
        for j in range(0,len(verbs)):
            for k in range(0,len(objects)):
                sentence_list.append(subjects[i]+" "+verbs[j]+" "+objects[k])
	
    return sentence_list

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))
