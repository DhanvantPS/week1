from sympy import symbols, apart, fraction, sympify, init_printing, solve, div, Poly, simplify
import schemdraw
import schemdraw.elements as elm

# Initialize pretty printing for better readability
init_printing()

# Define the Laplace variable
s = symbols("s")

input_form = input("What form you need:\n1.f1\n2.f2\n3.c1\n4.c2\n")


# Get user input for a rational function
input_function = input("Enter a rational function in terms of s: ")
try:
    # Convert user input to a SymPy expression
    rational_function = sympify(input_function)

except Exception as e:
    print("Invalid input. Please enter a valid rational function")
    exit()

# Perform partial fraction decomposition
Zeroes=[0]
Poles=[0]
num_function , denom_function = fraction(rational_function)
Zeroes = solve(num_function,s)
Poles = solve(denom_function,s)

partial_fraction=apart(rational_function)

invert_flag=0

def division(dividend, divisor):
    dividend = Poly(dividend, s)
    divisor = Poly(divisor, s)
    
    # Calculate the leading term of the quotient
    leading_term_quotient = quotient, remainder = div(dividend,divisor, domain='QQ')

# Limit the quotient to the first (leading) term
    leading_term_quotient = quotient.as_expr().as_ordered_terms()[0]
    
    # Calculate the intermediate result of multiplying the leading term quotient by the divisor
    intermediate_result = leading_term_quotient * divisor.as_expr()
    
    # Calculate the remainder after one term of division
    remainder_after_one_step = dividend.as_expr() - intermediate_result

    
    return leading_term_quotient, remainder_after_one_step

def division_least(num,denom):
    dividend = num.as_poly(1/s)
    divisor = denom.as_poly(1/s)
    # Calculate the leading term of the quotient
    quotient = dividend.as_expr().as_ordered_terms()[-1]/divisor.as_expr().as_ordered_terms()[-1]

# Limit the quotient to the first (leading) term
    leading_term_quotient = quotient
    
    # Calculate the intermediate result of multiplying the leading term quotient by the divisor
    intermediate_result = leading_term_quotient * divisor.as_expr()
    
    # Calculate the remainder after one term of division
    remainder_after_one_step = dividend.as_poly() - intermediate_result
    remainder_after_one_step=remainder_after_one_step.as_expr()

    return leading_term_quotient, remainder_after_one_step

def division_least_lc(num,denom):
    dividend = num.as_poly(1/s)
    divisor = denom.as_poly(1/s)
    # Calculate the leading term of the quotient
    quotient,remainder = div(dividend,divisor,domain="QQ")

# Limit the quotient to the first (leading) term
    leading_term_quotient = quotient.as_expr().as_ordered_terms()[0]
    
    # Calculate the intermediate result of multiplying the leading term quotient by the divisor
    intermediate_result = leading_term_quotient * divisor.as_expr()
    
    # Calculate the remainder after one term of division
    remainder_after_one_step = dividend.as_poly() - intermediate_result
    remainder_after_one_step=remainder_after_one_step.as_expr()

    return leading_term_quotient, remainder_after_one_step




def draw_foster_1_lc_circuit(C_0, L_inf, LC_pairs):

    with schemdraw.Drawing() as d:
        d.config(unit=2)  # Set unit size for spacing

        # Start with initial capacitor C_0
        d += elm.Capacitor().label(f'C₀ = {C_0} F').right()

        # Add L-C pairs in series
        for i, (L_n, C_n) in enumerate(LC_pairs, start=1):
            d.push()
            d += elm. Line().down().length(0.5)
            d += elm. Inductor().label(f'L = {L_n} H').down()
            d += elm.Line().up().length(0.5)
            d.pop()
            d.push()
            d += elm. Line().right().length(2)
            d += elm.Line().down().length(0.5)
            d += elm.Capacitor().label(f'C = {C_n} F').down() 
            d += elm.Line().left().length(2)
            d += elm.Line().right().length(2)
            # d.pop()
            d += elm. Line().right()
        
        # Add final inductor L_inf
        d += elm.Inductor().right().label(f'L∞ = {L_inf} H')

        # Show the circuit
        d.draw()

def draw_foster_2_lc_circuit(C_0, L_inf, LC_pairs):

    with schemdraw.Drawing() as d:
        d.config(unit=2)  # Set unit size for spacing

        # Start with initial capacitor C_0
        d += elm.Line().right().length(1)
        d.push()
        d += elm.Line().down().length(1)
        d += elm.Capacitor().label(f'C₀ = {C_0} F').down()
        d += elm.Line().down().length(1)
        d += elm.Line().left().length(1)
        d.pop()

        # Add L-C pairs in series
        for i, (L_n, C_n) in enumerate(LC_pairs, start=1):
            d.push()
            d += elm. Line().right(i)
            d += elm. Inductor().label(f'L = {L_n} H').down()
            d += elm.Capacitor().label(f'C = {C_n} F').down() 
            d += elm. Line().left(i)
            d.pop()
        
        # Add final inductor L_inf
        d += elm.Line().right().length(n+1)
        d += elm.Line().down().length(1)
        d += elm.Inductor().down().label(f'L∞ = {L_inf} H')
        d += elm.Line().down().length(1)
        d += elm.Line().left().length(n+1)

        # Show the circuit
        d.draw()

import schemdraw
import schemdraw.elements as elm

def draw_foster_1_rl_circuit( L_inf,R_0, RL_pairs):

    with schemdraw.Drawing() as d:
        d.config(unit=2)  # Set unit size for spacing

        # Start with initial Resistor R_0
        d += elm.Resistor().label(f'R₀ = {R_0} Ohm').right()

        # Add L-C pairs in series
        for i, (L_n, R_n) in enumerate(RL_pairs, start=1):
            d.push()
            d += elm. Line().down().length(0.5)
            d += elm. Inductor().label(f'L = {L_n} H').down()
            d += elm.Line().up().length(0.5)
            d.pop()
            d.push()
            d += elm. Line().right().length(2)
            d += elm.Line().down().length(0.5)
            d += elm.Resistor().label(f'R = {R_n} Ohm').down() 
            d += elm.Line().left().length(2)
            d += elm.Line().right().length(2)
            # d.pop()
            d += elm. Line().right()
        
        # Add final inductor L_inf
        d += elm.Inductor().right().label(f'L∞ = {L_inf} H')

        # Show the circuit
        d.draw()

def draw_foster_2_rl_circuit(L_0, R_inf, RL_pairs):

    with schemdraw.Drawing() as d:
        d.config(unit=2)  # Set unit size for spacing
        n=len(RL_pairs)
        # Start with initial capacitor L_0
        d += elm.Line().right().length(1)
        d.push()
        d += elm.Line().down().length(1)
        d += elm.Inductor().label(f'L₀ = {L_0} H').down()
        d += elm.Line().down().length(1)
        d += elm.Line().left().length(1)
        d.pop()

        # Add L-C pairs in series
        for i, (R_n, L_n) in enumerate(RL_pairs, start=1):
            d.push()
            d += elm. Line().right(i)
            d += elm. Resistor().label(f'R = {R_n} Ohm').down()
            d += elm.Inductor().label(f'L = {L_n} H').down() 
            d += elm. Line().left(i)
            d.pop()
        
        # Add final inductor R_inf
        d += elm.Line().right().length(n+1)
        d += elm.Line().down().length(1)
        d += elm.Resistor().down().label(f'R∞ = {R_inf} Ohm')
        d += elm.Line().down().length(1)
        d += elm.Line().left().length(n+1)

        # Show the circuit
        d.draw()


def draw_foster_1_rc_circuit(C_0, R_inf, RC_pairs):
    
    with schemdraw.Drawing() as d:
        d.config(unit=2)  # Set unit size for spacing

        # Start with initial capacitor C_0
        d += elm.Capacitor().label(f'C₀ = {C_0} F').right()

        # Add R-C pairs in series
        for i, (R_n, C_n) in enumerate(RC_pairs, start=1):
            d.push()
            d += elm. Line().down().length(0.5)
            d += elm. Resistor().label(f'R = {R_n} Ohm').down()
            d += elm.Line().up().length(0.5)
            d.pop()
            d.push()
            d += elm. Line().right().length(2)
            d += elm.Line().down().length(0.5)
            d += elm.Capacitor().label(f'C = {C_n} F').down() 
            d += elm.Line().left().length(2)
            d += elm.Line().right().length(2)
            # d.pop()
            d += elm. Line().right()
        
        # Add final Resistor R
        d += elm.Resistor().right().label(f'R∞ = {R_inf} Ohm')

        # Show the circuit
        d.draw()




def draw_foster_2_rc_circuit(R_0, C_inf, RC_pairs):

    with schemdraw.Drawing() as d:
        d.config(unit=2)  # Set unit size for spacing
        n=len(RC_pairs)
        # Start with initial capacitor R_0
        d += elm.Line().right().length(1)
        d.push()
        d += elm.Line().down().length(1)
        d += elm.Resistor().label(f'R₀ = {R_0} Ohm').down()
        d += elm.Line().down().length(1)
        d += elm.Line().left().length(1)
        d.pop()

        # Add L-C pairs in series
        for i, (C_n, R_n) in enumerate(RC_pairs, start=1):
            d.push()
            d += elm. Line().right(i)
            d += elm. Capacitor().label(f'L = {C_n} F').down()
            d += elm.Resistor().label(f'C = {R_n} Ohm').down() 
            d += elm. Line().left(i)
            d.pop()
        
        # Add final inductor C_inf
        d += elm.Line().right().length(n+1)
        d += elm.Line().down().length(1)
        d += elm.Capacitor().down().label(f'C∞ = {C_inf} F')
        d += elm.Line().down().length(1)
        d += elm.Line().left().length(n+1)

        # Show the circuit
        d.draw()

def draw_cauer_2_lc_circuit(L, C):
    # Cauer 1 LC always starts with an inductor
    with schemdraw.Drawing() as d:
        d.config(unit=2)
        
        d += elm.Line().right(2)


        for i in range(len(C)):
            d.push()
            d += elm.Inductor().label(f'L = {L[i]} H').down()
            d += elm.Line().left(2)
            d.pop()
            
            d += elm.Capacitor().label(f'C = {C[i]} F').right() 
            

        if len(L) > len(C):
            d += elm.Inductor().label(f'L = {L[-1]} H').down()
            d.push()
            d += elm.Line().left(2)
        if len(L) ==len(C):
            d += elm.Line().down(2)
            d += elm.Line().left(2)

        d.draw()

def draw_cauer_1_lc_circuit(L, C):
    # Cauer 1 LC always starts with an inductor
    with schemdraw.Drawing() as d:
        d.config(unit=2)


        for i in range(len(C)):
            d += elm.Inductor().label(f'L = {L[i]} H').right()
            d.push()
            d += elm.Capacitor().label(f'C = {C[i]} F').down() 
            d += elm.Line().left(2)
            d.pop()

        if len(L) > len(C):
            d += elm.Inductor().label(f'L = {L[-1]} H').right()
            d.push()
            d += elm.Line().down(2)
            d += elm.Line().left(2)

        d.draw()

def draw_cauer_1_rc_circuit(R, C):
    # Cauer 1 LC always starts with an inductor
    with schemdraw.Drawing() as d:
        d.config(unit=2)


        for i in range(len(C)):
            d += elm.Resistor().label(f'R = {R[i]} Ohm').right()
            d.push()
            d += elm.Capacitor().label(f'C = {C[i]} F').down() 
            d += elm.Line().left(2)
            d.pop()

        if len(R) > len(C):
            d += elm.Resistor().label(f'R = {R[-1]} Ohm').right()
            d.push()
            d += elm.Line().down(2)
            d += elm.Line().left(2)

        d.draw()

def draw_cauer_1_rl_circuit(R, L):
    # Cauer 1 LC always starts with an inductor
    with schemdraw.Drawing() as d:
        d.config(unit=2)


        for i in range(len(L)):
            d += elm.Inductor().label(f'L = {L[i]} H').right()
            d.push()
            d += elm.Resistor().label(f'R = {R[i]} Ohms').down() 
            d += elm.Line().left(2)
            d.pop()

        if len(R) > len(L):
            d += elm.Inductor().label(f'L = {L[-1]} H').right()
            d.push()
            d += elm.Line().down(2)
            d += elm.Line().left(2)

        d.draw()

def draw_cauer_2_rl_circuit(R, L):
    # Cauer 1 LC always starts with an inductor
    with schemdraw.Drawing() as d:
        d.config(unit=2)
        
        d += elm.Line().right(2)


        for i in range(len(L)):
            d.push()
            d += elm.Resistor().label(f'R = {R[i]} Ohms').down()
            d += elm.Line().left(2)
            d.pop()
            
            d += elm.Inductor().label(f'L = {L[i]} H').right() 
            

        if len(R) > len(L):
            d += elm.Resistor().label(f'R = {R[-1]} Ohms').down()
            d.push()
            d += elm.Line().left(2)
        if len(R) ==len(L):
            d += elm.Line().down(2)
            d += elm.Line().left(2)
        
        if len(R) < len(C):
            d += elm.Capacitor().label(f'c = {C[-1]} Ohms').down()
            d.push()
            d += elm.Line().left(2)

        d.draw()


def draw_cauer_2_rc_circuit(R, C):
    # Cauer 1 LC always starts with an inductor
    with schemdraw.Drawing() as d:
        d.config(unit=2)
        
        d += elm.Line().right(2)


        for i in range(len(R)):
             d += elm.Capacitor().label(f'C = {C[i]} F').right() 
             d.push()
             d += elm.Resistor().label(f'R = {R[i]} Ohms').down()
             d += elm.Line().left(2)
             d.pop()
            
             
            

        if len(R) > len(C):
            d += elm.Resistor().label(f'R = {R[-1]} Ohms').down()
            d.push()
            d += elm.Line().left(2)
        if len(R) ==len(C):
            d += elm.Line().down(2)
            d += elm.Line().left(2)
        if len(R) < len(C):
            d += elm.Capacitor().label(f'c = {C[-1]} Ohms').right()
            d.push()
            d += elm.Line().down(2)
            d += elm.Line().left(2)

        d.draw()





def Foster_LC(partial_fraction):
    LC_pair_f1= []
    C_zero_f1 = 0
    L_infinte_f1= [0]
    # Loop through each term in the partial fraction decomposition
    for term in partial_fraction.as_ordered_terms():
        # Separate numerator and denominator of each term
        num, denom = fraction(term)

        if  denom.is_number and num.is_polynomial(s):
            L_infinte_f1= num.as_poly(s).all_coeffs()
    
        if  num.is_number and denom.is_polynomial(s):
            denom_poly = denom.as_poly(s)
            if(denom_poly.degree()==1):
                 C_zero_f1 = (denom.as_poly(s).all_coeffs()[0])/num

        # Check if the denominator is a polynomial in `s` and is not 1
        if denom.is_polynomial(s) and denom != 1:
            # Check if the degree of the denominator is 2
            denom_poly = denom.as_poly(s)
            if denom_poly and denom_poly.degree() == 2:
                # Extract the coefficients of s^2 and the constant term in the denominator
                coeffs = denom_poly.all_coeffs()
                # Ensure the term is in the form s / (s^2 + omega^2) by checking the numerator
                if len(coeffs) == 3:
                    # `a` is the coefficient of s^2, and `b` is the constant term
                    a,dummy, b = coeffs
                
                    # Calculate L and C for the LC circuit: L = 1/b and C = 1/a
                    C = a/num.as_poly(s).all_coeffs()[0]
                    L= num.as_poly(s).all_coeffs()[0]/ b
                    LC_pair_f1.append((L, C))

    # Output results
    if(input_form=="f1"):
        LC_pair_f1=tuple(LC_pair_f1)
        draw_foster_1_lc_circuit(C_zero_f1, L_infinte_f1[0], LC_pair_f1)
        print("Extracted LC Values for Foster I Network :")
        print("C zero = ",C_zero_f1)
        for idx, (L, C) in enumerate(LC_pair_f1, start=1):
            print(f"LC Pair {idx}: L = {L}, C = {C}")
        print("L infinity = ",L_infinte_f1[0])
        print(partial_fraction)
    if(input_form=="f2"):
        LC_pair_f1=tuple(LC_pair_f1)
        draw_foster_2_lc_circuit(L_infinte_f1[0],C_zero_f1, LC_pair_f1)
        print("Extracted LC Values for Foster II  Network :")
        print("C zero = ",L_infinte_f1[0])
        for idx, (L, C) in enumerate(LC_pair_f1, start=1):
            print(f"LC Pair {idx}: L = {C}, C = {L}")
        print("L infinity = ",C_zero_f1)



def Foster_RC(partial_fraction):

    RC_pair_f1= []
    C_zero_f1 = 0
    R_infinte_f1= 0
    R_zero_f2=0
    C_infinite_f2=0
    # Loop through each term in the partial fraction decomposition
    for term in partial_fraction.as_ordered_terms():
        # Separate numerator and denominator of each term
        num, denom = fraction(term)

        if  denom.is_number and num.is_number:
            R_infinte_f1= num/denom
            C_infinite_f2=num/denom
    
        if  num.is_number and denom.is_polynomial(s):
            denom_poly = denom.as_poly(s)
            if denom_poly and denom_poly.degree() == 1:
                 C_zero_f1 = (denom.as_poly(s).all_coeffs()[0])/num

        if  denom.is_number and num.is_polynomial(s):
            num_poly = num.as_poly(s)
            if num_poly and num_poly.degree() == 1:
                 R_zero_f2 = (num.as_poly(s).all_coeffs()[0])/denom

  
        if denom.is_polynomial(s) and denom != 1:
            denom_poly = denom.as_poly(s)
            
            if denom_poly and denom_poly.degree() == 1:
                coeffs = denom_poly.all_coeffs()
                if len(coeffs) == 2 and coeffs[1]!=0:
                    a, b = coeffs  
                    C = a/num
                    R = num/b
                    RC_pair_f1.append((R, C))
    if(input_form=="f1"):
        RC_pair_f1=tuple(RC_pair_f1)
        draw_foster_1_rc_circuit( C_zero_f1,R_infinte_f1, RC_pair_f1)
        print("Extracted RC Values for Foster I Network :")
        print("C zero = ",C_zero_f1)
        for idx, (R, C) in enumerate(RC_pair_f1, start=1):
            print(f"RC Pair {idx}: R = {R}, C = {C}")
        print("R infinity = ",R_infinte_f1)
    if(input_form=="f2"):
        RC_pair_f1=tuple(RC_pair_f1)
        draw_foster_2_rc_circuit(R_zero_f2, C_infinite_f2, RC_pair_f1)
        print("Extracted RC Values for Foster II  Network :")
        print("R zero = ",R_zero_f2)
        for idx, (R, C) in enumerate(RC_pair_f1, start=1):
            print(f"RC Pair {idx}: R = {C}, C = {R}")
        print("C infinity = ",C_infinite_f2)

def Foster_RL(partial_fraction):
    RL_pair_f1= []
    R_zero_f1 = 0
    L_infinte_f1= 0
    L_zero_f2=0
    R_infinite_f2=0
    print(partial_fraction)
    for term in partial_fraction.as_ordered_terms():
        if(input_form=="f1"):
             term=(term*s)
        num, denom = fraction(term)

        if  denom.is_number and num.is_number:
            R_zero_f1= num/denom
            R_infinite_f2= denom/num
    
        if  num.is_number and denom.is_polynomial(s):
            denom_poly = denom.as_poly(s)
            if denom_poly and denom_poly.degree() == 1:
                 L_zero_f2 = (denom.as_poly(s).all_coeffs()[0])/num
                 

        if  denom.is_number and num.is_polynomial(s):
            num_poly = num.as_poly(s)
            if num_poly and num_poly.degree() == 1:
                 L_infinte_f1 = (num.as_poly(s).all_coeffs()[0])/denom

  
        if denom.is_polynomial(s) and denom != 1:
            denom_poly = denom.as_poly(s)
            if denom_poly and denom_poly.degree() == 1:
                coeffs = denom_poly.all_coeffs()
                if len(coeffs) == 2 and coeffs[1]!=0:
                    a, b = coeffs  
                    L= a/num
                    R= b/num
                    if(input_form=="f1"):
                        num_poly = num.as_poly(s)
                        R=num_poly.all_coeffs()[0]/a
                        L=R*a/b
                        RL_pair_f1.append((L, R))
    if(input_form=="f1"):
        RL_pair_f1=tuple(RL_pair_f1)
        draw_foster_1_rl_circuit(L_infinte_f1, R_zero_f1, RL_pair_f1)
        print("Extracted RL Values for Foster I Network :")
        print("R zero = ",R_zero_f1)
        for idx, (L, R) in enumerate(RL_pair_f1, start=1):
            print(f"RL Pair {idx}: L = {L}, R = {R}")
        print("L infinity = ",L_infinte_f1)

    if(input_form=="f2"):
        RL_pair_f1=tuple(RL_pair_f1)
        draw_foster_2_rl_circuit(L_zero_f2, R_infinite_f2, RL_pair_f1)
        print("Extracted RL Values for Foster II  Network :")
        print("L zero = ",L_zero_f2)
        for idx, (L, R) in enumerate(RL_pair_f1, start=1):
            print(f"RL Pair {idx}: L = {L}, R = {R}")
        print("R infinity = ",R_infinite_f2)

def Cauer_1_LC(rational_function,invert_flag):
    imittances=[]
    num,denom=fraction(rational_function)
    remainder=1
    while(remainder!=0):
        quotient, remainder = division( num, denom)
        imittances.append(quotient)
        num=denom
        denom=remainder
    Capacitor_C2=[]
    Inductor_C2=[]
    counter=0
    for terms in imittances:
        terms = sympify(terms)
        num,denom = fraction(terms)
        if(invert_flag==0):
            if(counter%2==0):
                Capacitor_C2.append(num.as_poly(s).all_coeffs()[0]/denom.as_poly(s).all_coeffs()[0])
            else:
                Inductor_C2.append(num.as_poly(s).all_coeffs()[0]/denom.as_poly(s).all_coeffs()[0])
        elif(invert_flag==1):
                if(counter%2==0):
                    Inductor_C2.append(num.as_poly(s).all_coeffs()[0]/denom.as_poly(s).all_coeffs()[0])
                else:
                    Capacitor_C2.append(num.as_poly(s).all_coeffs()[0]/denom.as_poly(s).all_coeffs()[0])
        counter=counter+1
    if(invert_flag==1):
        Capacitor_C2.insert(0,0)
    
    draw_cauer_1_lc_circuit(Capacitor_C2, Inductor_C2)

    print("Inductors=",Capacitor_C2)
    print("Capacitors=",Inductor_C2)

def Cauer_1_RC(imittances,invert_flag):
    Resistor_C1=[]
    Capacitor_C1=[]
    counter=0
    for terms in imittances:
        terms = sympify(terms)
        num,denom = fraction(terms)
        if(invert_flag==0):
            if(counter%2==0):
                Resistor_C1.append(num.as_poly(s).all_coeffs()[0]/denom.as_poly(s).all_coeffs()[0])
            else:
                Capacitor_C1.append(num.as_poly(s).all_coeffs()[0]/denom.as_poly(s).all_coeffs()[0])
        if(invert_flag==1):
            if(counter%2==0):
                Capacitor_C1.append(num.as_poly(s).all_coeffs()[0]/denom.as_poly(s).all_coeffs()[0])
            else:
                Resistor_C1.append(num.as_poly(s).all_coeffs()[0]/denom.as_poly(s).all_coeffs()[0])
            
        counter=counter+1
    if(invert_flag==1):
        Resistor_C1.insert(0,0)
    draw_cauer_1_rc_circuit(Resistor_C1, Capacitor_C1)
    print("Resistors=",Resistor_C1)
    print("Capacitors=",Capacitor_C1)

def Cauer_1_RL(imittances,invert_flag):
    Resistor_C1=[]
    Inductor_C1=[]
    counter=0
    for terms in imittances:
        terms = sympify(terms)
        num,denom = fraction(terms)
        if(invert_flag==0):
            if(counter%2==0):
                Resistor_C1.append(denom.as_poly(s).all_coeffs()[0]/num.as_poly(s).all_coeffs()[0])
            else:
                Inductor_C1.append(num.as_poly(s).all_coeffs()[0]/denom.as_poly(s).all_coeffs()[0])
        if(invert_flag==1):
            if(counter%2==0):
                Resistor_C1.append(denom.as_poly(s).all_coeffs()[0]/num.as_poly(s).all_coeffs()[0])
            else:
                Inductor_C1.append(num.as_poly(s).all_coeffs()[0]/denom.as_poly(s).all_coeffs()[0])
        counter=counter+1
    if(invert_flag==1):
        Resistor_C1.insert(0,0)
    draw_cauer_1_rl_circuit(Resistor_C1, Inductor_C1)
    print("Resistors=",Resistor_C1)
    print("Inductors=",Inductor_C1)
 
def Cauer_2_LC(rational_function,invert_flag):
    imittances=[]
    num,denom=fraction(rational_function)
    num = num.as_poly(s)
    denom = denom.as_poly(s)
    highest_degree = max(num.degree(), denom.degree())
    num = num.as_expr() * (s**(-highest_degree))
    denom = denom.as_expr() * (s**(-highest_degree))
    remainder=1
    while(remainder!=0):
        quotient, remainder = division_least_lc( num, denom)
        imittances.append(quotient)
        print(quotient)
        num=denom
        denom=remainder
    print(imittances)
    Capacitor_C2=[]
    Inductor_C2=[]
    counter=0
    for terms in imittances:
        terms = sympify(terms)
        num,denom = fraction(terms)
        i = denom.as_poly(s).all_coeffs()[0]/num.as_poly(s).all_coeffs()[0]
        if(invert_flag==0):
            if(counter==0 and num.as_poly(s).all_coeffs()[0]==0):
                    Capacitor_C2.append(0)
            elif(counter%2==0):
                Capacitor_C2.append(i)
            else:
                Inductor_C2.append(i)
        elif(invert_flag==1):
                if(counter==0 and num.as_poly(s).all_coeffs()[0]==0):
                    Inductor_C2.append(0)
                elif(counter%2==0):
                    Inductor_C2.append(i)
                else:
                    Capacitor_C2.append(i)
        counter=counter+1
    draw_cauer_2_lc_circuit(Inductor_C2, Capacitor_C2)
    print("Inductors=",Inductor_C2)
    print("Capacitors=",Capacitor_C2)
    

def Cauer_2_RC(imittances,invert_flag):
    Capacitor_C2=[]
    Resistor_C2=[]
    counter=0
    for terms in imittances:
        terms = sympify(terms)
        num,denom = fraction(terms)
        i = denom.as_poly(s).all_coeffs()[0]/num.as_poly(s).all_coeffs()[0]
        if(invert_flag==0):
            if(counter==0 and num.as_poly(s).all_coeffs()[0]==0):
                    Capacitor_C2.append(0)
            elif(counter%2==0):
                Capacitor_C2.append(i)
            else:
                Resistor_C2.append(i)
        elif(invert_flag==1):
                if(counter==0 and num.as_poly(s).all_coeffs()[0]==0):
                    Resistor_C2.append(0)
                elif(counter%2==0):
                    Resistor_C2.append(i)
                else:
                    Capacitor_C2.append(i)
        counter=counter+1
    draw_cauer_2_rc_circuit(Resistor_C2, Capacitor_C2)
    print("Resistors=",Resistor_C2)
    print("Capacitors=",Capacitor_C2)

def Cauer_2_RL(imittances,invert_flag):
    Inductors_C2=[]
    Resistor_C2=[]
    counter=0
    for terms in imittances:
        terms = sympify(terms)
        num,denom = fraction(terms)
        i = denom.as_poly(s).all_coeffs()[0]/num.as_poly(s).all_coeffs()[0]
        if(invert_flag==0):
            if(counter==0 and num.as_poly(s).all_coeffs()[0]==0):
                    Inductors_C2.append(0)
            elif(counter%2==0):
                Resistor_C2.append(num.as_poly(s).all_coeffs()[0]/denom.as_poly(s).all_coeffs()[0])
            else:
                Inductors_C2.append(i)
        elif(invert_flag==1):
                if(counter==0 and num.as_poly(s).all_coeffs()[0]==0):
                    Resistor_C2.append(0)
                elif(counter%2==0):
                    Resistor_C2.append(num.as_poly(s).all_coeffs()[0]/denom.as_poly(s).all_coeffs()[0])
                else:
                    Inductors_C2.append(i)
        counter=counter+1
    draw_cauer_2_rl_circuit(Resistor_C2, Inductors_C2)
    print("Resistors=",Resistor_C2)
    print("Inductors=",Inductors_C2)

def Cauer_1(rational_function, invert_flag,degree_flag):
    imittances=[]
    num,denom=fraction(rational_function)
    remainder=1
    while(remainder!=0):
        quotient, remainder = division( num, denom)
        imittances.append(quotient)
        num=denom
        denom=remainder
    term0=imittances[0]
    term0 = sympify(term0)
    num0,denom0 = fraction(term0)
    term1=imittances[1]
    term1 = sympify(term1)
    num1,denom1 = fraction(term1)
    if(invert_flag==0 and degree_flag==0):
        if(num1.is_polynomial(s)):
            Cauer_1_RC(imittances,invert_flag)
    elif(invert_flag==0 and degree_flag==0):
        if(denom1.is_polynomial(s)):
            Cauer_1_RL(imittances,invert_flag)

    elif(invert_flag==1 and degree_flag==0):
        if(num0.is_polynomial(s)):
            Cauer_1_RC(imittances,invert_flag)
    elif(invert_flag==1 and degree_flag==0):
        if(denom0.is_polynomial(s)):
            Cauer_1_RL(imittances,invert_flag)
    elif(invert_flag==1 and degree_flag==1):
        if(num1.is_polynomial(s)):
            Cauer_1_RL(imittances,invert_flag)
    elif(invert_flag==1 and degree_flag==1):
        if(denom1.is_polynomial(s)):
            Cauer_1_RC(imittances,invert_flag)
    elif(invert_flag==0 and degree_flag==1):
        if(num1.is_polynomial(s)):
            Cauer_1_RC(imittances,invert_flag)
    elif(invert_flag==0 and degree_flag==1):
        if(denom1.is_polynomial(s)):
            Cauer_1_RL(imittances,invert_flag)

def Cauer_2(rational_function, invert_flag,degree_flag):
    imittances=[]
    num,denom=fraction(rational_function)
    num = num.as_poly(s)
    denom = denom.as_poly(s)
    highest_degree = max(num.degree(), denom.degree())
    num = num.as_expr() * (s**(-highest_degree))
    denom = denom.as_expr() * (s**(-highest_degree))
    remainder=1
    while(remainder!=0):
        quotient, remainder = division_least( num, denom)
        imittances.append(quotient)
        num=denom
        denom=remainder
    print("inv=",invert_flag)
    print("deg=",degree_flag)
    print(imittances)
    term0=imittances[0]
    term0 = sympify(term0)
    num0,denom0 = fraction(term0)
    term1=imittances[1]
    term1 = sympify(term1)
    num1,denom1 = fraction(term1)
    if(invert_flag==1 and degree_flag==0):
        if(num1.is_polynomial(s)):
            Cauer_2_RL(imittances,invert_flag)
    elif(invert_flag==0 and degree_flag==0):
        if(denom1.is_polynomial(s)):
            Cauer_2_RC(imittances,invert_flag)
    elif(invert_flag==0 and degree_flag==0):
        if(num0.is_polynomial(s)):
            Cauer_2_RL(imittances,invert_flag)
    elif(invert_flag==1 and degree_flag==0):
        if(denom0.is_polynomial(s)):
            Cauer_2_RC(imittances,invert_flag)


    elif(invert_flag==0 and degree_flag==1):
        if(num1.is_polynomial(s)):
            Cauer_2_RC(imittances,invert_flag)
    elif(invert_flag==0 and degree_flag==1):
        if(denom1.is_polynomial(s)):
            Cauer_2_RL(imittances,invert_flag)
    elif(invert_flag==1 and degree_flag==1):
        if(num0.is_polynomial(s)):
            Cauer_2_RC(imittances,invert_flag)
    elif(invert_flag==1 and degree_flag==1):
        if(denom0.is_polynomial(s)):
            Cauer_2_RL(imittances,invert_flag)

if(Zeroes[0].is_real and Poles[0].is_real):

    if( max(Poles)>max(Zeroes) and max(Poles)<=0 and input_form=="f1" or input_form=="f2"):
        if(input_form == "f1"):
            Foster_RC(partial_fraction)
        
        if(input_form == "f2"):
            Foster_RL(partial_fraction)

    elif(min(Poles)<min(Zeroes) and min(Poles)<=0 and input_form=="f1" or input_form=="f2"):
        if(input_form == "f1"):
            rational_function=rational_function/s
            partial_fraction=apart(rational_function)
            Foster_RL(partial_fraction)
        
        if(input_form == "f2"):
            Foster_RC(partial_fraction)
    
    elif(input_form=="c1"):
        num,denom=fraction(rational_function)
        num_poly =  num.as_poly(s)
        denom_poly = denom.as_poly(s)
        if(denom_poly.degree()<num_poly.degree()):
            degree_flag=0
            invert_flag=0
            Cauer_1(rational_function,invert_flag,degree_flag)
        elif(denom_poly.degree()>num_poly.degree()):
            degree_flag=0
            invert_flag=1
            Cauer_1(1/rational_function,invert_flag,degree_flag)
        elif(denom_poly.degree()==num_poly.degree()):
            degree_flag=1
            if(max(Zeroes)>max(Poles)):
                invert_flag=1
                Cauer_1(1/rational_function,invert_flag,degree_flag)
            else:
                Cauer_1(rational_function,invert_flag,degree_flag)

    
    elif(input_form=="c2"):
        num,denom=fraction(rational_function)
        num_poly =  num.as_poly(s)
        denom_poly = denom.as_poly(s)
        if(denom_poly.degree()>num_poly.degree()):
            invert_flag=0
            degree_flag=0
            Cauer_2(rational_function,invert_flag,degree_flag)
        elif(denom_poly.degree()<num_poly.degree()):
            degree_flag=0
            invert_flag=1
            Cauer_2(1/rational_function,invert_flag,degree_flag)
        elif(denom_poly.degree()==num_poly.degree()):
            degree_flag=1
            if(max(Zeroes)<max(Poles)):
                invert_flag=0
                Cauer_2(rational_function,invert_flag,degree_flag)
            else:
                invert_flag=1
                Cauer_2(1/rational_function,invert_flag,degree_flag)

    else:
        if(input_form=="f2"):
            partial_fraction=apart(rational_function/s)
            Foster_RC(partial_fraction)

        if(input_form=="f1"):
            partial_fraction=apart(rational_function/s)
            Foster_RL(partial_fraction)

else:
    if(input_form=="f1" or input_form=="f2"):
         Foster_LC(partial_fraction)
    
    elif(input_form=="c1"):
        num,denom=fraction(rational_function)
        num_poly =  num.as_poly(s)
        denom_poly = denom.as_poly(s)
        if(denom_poly.degree()<num_poly.degree()):
            invert_flag=0
            Cauer_1_LC(rational_function,invert_flag)
        elif(denom_poly.degree()>num_poly.degree()):
            invert_flag=1
            Cauer_1_LC(1/rational_function,invert_flag)
    
    elif(input_form=="c2"):
        num,denom=fraction(rational_function)
        num_poly =  num.as_poly(s)
        denom_poly = denom.as_poly(s)
        if(denom_poly.degree()>num_poly.degree()):
            invert_flag=0
            Cauer_2_LC(rational_function,invert_flag)
        elif(denom_poly.degree()<num_poly.degree()):
            invert_flag=1
            Cauer_2_LC(1/rational_function,invert_flag)


