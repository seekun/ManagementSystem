a = {

}

a['test'] = 1
a['tfdsf'] = 2
a['fd'] = 0
print(sorted(a.items(), key=lambda kv: kv[1]))
