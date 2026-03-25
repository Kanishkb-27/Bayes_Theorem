p_st=0.2
p_st_pos=0.2*0.85
p_nst_pos=0.8*0.02
p_positive=p_st_pos*p_nst_pos
p_pos_given_st=0.85
result=(p_st*p_pos_given_st)/p_positive
print("Probability of having strep throat when positive is",round(result,3))