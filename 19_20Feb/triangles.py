with open("triangles.in", "r") as f1:
    n = int(f1.readline().strip())
    posts = []
    for _ in range(n):
        post = f1.readline().strip().split(" ")
        post = [int(x) for x in post]
        posts.append(post)
    maxArea = 0
    print(posts)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                corner = posts[i]
                x = posts[j]
                y = posts[k]
                if corner[0] == x[0] and corner[1] == y[1]:
                    area = abs(x[1] - corner[1]) * abs(y[0] - corner[0])
                    if area > maxArea:
                        maxArea = area
    with open("triangles.out", "w") as f2:
        f2.write(str(maxArea))