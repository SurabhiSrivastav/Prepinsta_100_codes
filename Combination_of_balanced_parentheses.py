n=int(input('Enter a number: '))
# n=1-- {} -- 1o1c
# n=2-- {{}},{}{} -- 1o2o2c1c,1o1c2o2c
# n=3-- {{{}}},{}{}{},{}{{}},{{}}{},{{}{}} -- 1o2o3o3c2c1c, 1o1c2o2c3o3c, 1o1c2o3o3c2c, 1o2o2c1c3o3c, 1o2o2c3o3c1c
def generate(n):
    final_res=[]
    def balanced_parentheses(init_str,open,close):
        if len(init_str)==2*n:
            final_res.append(init_str)
            return final_res
        # will backtrack and check for all possible valid combinations
        if open<n:
            balanced_parentheses(init_str+'{',open+1,close)
        if close<open:
            balanced_parentheses(init_str+'}',open,close+1)

    balanced_parentheses("",0,0)
    return final_res

print(generate(n))