n = int(input("enter count of conditions "))
c = []
#you need to enter to what change, where go and what condition for example 0 > 2 or 1 < 1
events = []
out = ""
for i in range(1, n+1):
    #c.append(list(input("enter r, g, b of condition").split()))

    l = input("enter events when letter = 0 ").split()
    print(l)
    l1=  input("enter events when letter = 1 ").split()
    l2 = input("enter events when there in no letter ").split()
    d0 = "(m_i_n_f \\to r_e_p_l_a_c_e(m_i_n_f, t+d_o_f_f_s_e_t,"+l[0]+"),"+"t \\to t"+ ("+"if l[1]==">" else "-") + "1, b_c_u_r \\to "+l[2]+")"
    d1 = "(m_i_n_f \\to r_e_p_l_a_c_e(m_i_n_f, t+d_o_f_f_s_e_t,"+l1[0]+"),"+"t \\to t"+ ("+"if l1[1]==">" else "-") + "1, b_c_u_r \\to "+l1[2]+")"
    d2 = "(m_i_n_f \\to r_e_p_l_a_c_e(m_i_n_f, t+d_o_f_f_s_e_t,"+l2[0]+"),"+"t \\to t"+ ("+"if l2[1]==">" else "-") + "1, b_c_u_r \\to "+l2[2]+")"
    out += "d_"+str(i)+"= \\left\\{m_i_n_f[t+d_o_f_f_s_e_t]=0: "+d0 +",\\left\\{m_i_n_f[t+d_o_f_f_s_e_t]=1:"+d1+","+d2+"\\right\\}\\right\\}\n"
    out += "c_"+str(i)+"=\\left\\{b_c_u_r ="+str(i)+":d_"+str(i)+",c_"+str(i+1) +"\\right\\}\n"
#out += "c_c_o_l_r_s=[",",".join("rgb("+j+")" for j in c), "]"
print(out)
