class Quiz30:
    def quiz30(self) -> None:
        list1 = [1,2,3,4]
        print(list1, type(list1)) #[1,2,3,4], type: list
        print(list1[0], list1[-1], list1[-2], list1[1:3]) # 1, 4, 3, [2,3]

        list2 = ['math', 'english']
        print(list2[0]) # ['math']
        print(list2[0][1]) # [a]

        list3 = [1,'2',[1,2,3]]
        print(list3) # [1,2,[1,2,3]]

        list4 = [1,2,3]
        list5 = [4,5]
        print(list4 + list5) # [1,2,3,4,5]

        print(2*list4) # [1,2,3,1,2,3]
        list4.append(list5)
        print(list4) # [1,2,3,4,5]

        list4[-2:] = []
        print(list4) # [1,2,3]

        a=[1,2]
        b=[0,5]
        c= [a,b]
        print(c) # [[1,2],[0,5]]
        print(c[0][1]) # [2]

        c[0][1]=10
        print (c) # [[1,10],[0,5]]

        a=range(10)
        print(a) # range(0,10)
        print(sum(a)) # 45
        print(sorted(a)) # [0,1,2,3,4,5,6,7,8,9]

        b= [2,10,0,-2]
        print(sorted(b)) # -2, 0, 2, 10
        print(b.index(0),len(b))


    def quiz31(self) -> str: return None

    def quiz32(self) -> str: return None

    def quiz33(self) -> str: return None

    def quiz34(self) -> str: return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None
