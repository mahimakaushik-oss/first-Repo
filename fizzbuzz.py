def fizzbuzz():
	for i in range(1,51):
		if i%3==0:
			print("fizz")
		elif i%5==0:
			print("buzz")
		elif i%3==0 and i%5==0:
			print("fizzbuzz")
		else:
			print(i)

			
>>> fizzbuzz()
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizz
16
17
fizz
19
buzz
fizz
22
23
fizz
buzz
26
fizz
28
29
fizz
31
32
fizz
34
buzz
fizz
37
38
fizz
buzz
41
fizz
43
44
fizz
46
47
fizz
49
buzz
