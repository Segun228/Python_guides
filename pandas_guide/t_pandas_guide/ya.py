import math
import json
from itertools import combinations
import sys

def calculate_reldcg(results):
    return sum(d['relevance']/(i+1) for i,d in enumerate(results))

def calculate_revenue(results):
    return sum(d['cost']/math.sqrt(i+1) for i,d in enumerate(results))

def solve(serpset, new_documents):
    total = 0.0
    new_docs = {}
    
    for doc in new_documents:
        if doc['query'] not in new_docs:
            new_docs[doc['query']] = []
        new_docs[doc['query']].append(doc)
    
    for query_data in serpset:
        query = query_data['query']
        original = query_data['results']
        original_reldcg = calculate_reldcg(original)
        original_revenue = calculate_revenue(original)
        best_revenue = original_revenue
        
        if query not in new_docs:
            total += original_revenue
            continue
        
        candidates = new_docs[query]
        n = len(original)
        for doc in candidates:
            for pos in range(n+1):
                temp = [d.copy() for d in original]
                temp.insert(pos, doc.copy())
                for i in range(len(temp)):
                    temp[i]['position'] = i
                if len(temp) > n:
                    to_remove = None
                    min_ratio = float('inf')
                    
                    for i in range(len(temp)):
                        if i == pos: continue 
                        trial = temp[:i] + temp[i+1:]
                        trial_reldcg = calculate_reldcg(trial)
                        
                        if trial_reldcg >= original_reldcg:
                            ratio = temp[i]['cost']/math.sqrt(temp[i]['position']+1)
                            if ratio < min_ratio:
                                min_ratio = ratio
                                to_remove = i
                    
                    if to_remove is not None:
                        temp.pop(to_remove)
                        for i in range(len(temp)):
                            temp[i]['position'] = i
                
                if len(temp) == n:
                    current_reldcg = calculate_reldcg(temp)
                    if current_reldcg >= original_reldcg:
                        current_revenue = calculate_revenue(temp)
                        if current_revenue > best_revenue:
                            best_revenue = current_revenue
        
        total += best_revenue
    
    return round(total, 2)


input_json = sys.stdin.read()
data = json.loads(input_json)
result = solve(data['serpset'], data['new_documents'])
print(result)