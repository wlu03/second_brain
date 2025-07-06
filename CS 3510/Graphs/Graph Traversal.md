```
def explore(G, v):
	marked[v] = true
	previsit(v)
	for edge (v, u) in E:
		if not marked[u]
			explore(G, u)
	postvisit(v)
```
*Marked is a static set available in all calls to the routine. pre/post are two points in routine where modification allows for more applications.*
```
count = 1
def previsit(v):
	pre[v] = counter
	counter++
def postvisit(v):
	post[v] = counter
	counter++
```