def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# tr6->  [tr6,tr5,t4,tr3,tr2,tr1,tr0]     r->0

# result->0->1->

