a = "epfkenqweaylgjyphzixuefpszssvcxcnafcynxyvuvzxniwmdebtampnngxiooliwheswizebeziwsehwilooixgnnpmatbedmwinxzvuvyxnycfancxcvsszspfeuxizhpyjglyaewqnekfpe"
b = "ujesshzmxdpuzorrmaucbewvcnwiwefqpxgswwowapxsmfqslycbxxpvevuiprvgpqhgkboeyfxlqnkdzbalkleevczegnnqtdbhixwxshsvqdeliivqbfufbqviiledqvshsxwxihbdtqnngezcveelklabzdknqlxfyeobkghqpgvrpiuvevpxxbcylsqfmsxpawowwsgxpqfewiwncvwebcuamrrozupdxmzhsseju"
c = "liiyywwiyqqjnnnxdraaqwqxwlkkklnknlzcvuvuxvovoxnouocfncicvvvcicnfcouonxovovxuvuvczlnknlkkklwxqwqaardxnnnjqqyiwwyyiil"
b = list(b)

for i in range(int(len(b)/2)):
    print(b[i], b[-1 * (i+1)])
    if b[i] == b[-1*(i+1)]:
        b[i] = "z"
        b[-1 * (i+1)] = "z"

print("\nCurrent req - ",len(c))
print(len(a),len(b),int(len(a)/2),int(len(b)/2))
print(a[int(len(a)/2)])
print(b[int(len(b)/2)])
