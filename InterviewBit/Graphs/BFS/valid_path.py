import queue
class Solution:
    def solve(self, A, B, C, D, E, F):
        x = A
        y = B
        n = C
        r = D
        xarr = E
        yarr = F

        def check(cx, cy):
            if cx < 0 or cx > x or cy < 0 or cy > y:
                return False
            for k in range(len(xarr)):
                d = (xarr[k] - cx) ** 2 + (yarr[k] - cy) ** 2
                rs = r ** 2
                if d <= rs:
                    return False
            return True

        visited = [[False for i in range(y + 1)] for j in range(x + 1)]

        q = queue.Queue()
        f = 0
        q.put([0, 0])
        li = []
        i = 0
        while not q.empty():
            curr = q.get()
            currx = curr[0]
            curry = curr[1]
            visited[currx][curry] = True

            if not check(currx, curry):
                break

            if currx == x and curry == y:
                f = 1
                break

            if check(currx, curry + 1) and (not visited[currx][curry + 1]):
                q.put([currx, curry + 1])
                visited[currx][curry + 1] = True
                li.append([currx, curry + 1])

            if check(currx + 1, curry) and (not visited[currx + 1][curry]):
                q.put([currx + 1, curry])
                visited[currx + 1][curry] = True
                li.append([currx + 1, curry])

            if check(currx + 1, curry + 1) and (not visited[currx + 1][curry + 1]):
                q.put([currx + 1, curry + 1])
                visited[currx + 1][curry + 1] = True
                li.append([currx + 1, curry + 1])

            if check(currx, curry - 1) and (not visited[currx][curry - 1]):
                q.put([currx, curry - 1])
                visited[currx][curry - 1] = True
                li.append([currx, curry - 1])

            if check(currx + 1, curry - 1) and (not visited[currx + 1][curry - 1]):
                q.put([currx + 1, curry - 1])
                visited[currx + 1][curry - 1] = True
                li.append([currx + 1, curry - 1])

            if check(currx - 1, curry - 1) and (not visited[currx - 1][curry - 1]):
                q.put([currx - 1, curry - 1])
                visited[currx - 1][curry - 1] = True
                li.append([currx - 1, curry - 1])

            if check(currx - 1, curry) and (not visited[currx - 1][curry]):
                q.put([currx - 1, curry])
                visited[currx - 1][curry] = True
                li.append([currx - 1, curry])

            if check(currx - 1, curry + 1) and (not visited[currx - 1][curry + 1]):
                q.put([currx - 1, curry + 1])
                visited[currx - 1][curry + 1] = True
                li.append([currx - 1, curry + 1])
            i += 1
            if i == 2:
                temp = []
                while not q.empty():
                    t = q.get()
                    print(t)
                    # print("LOST")
                    temp.append(t)
                print("why not here?")
                print([temp, li, visited])

        # return li
        if f:
            return "YES"
        else:
            return "NO"



so = Solution()
print(so.solve(2,3,1,1,[2],[3]))