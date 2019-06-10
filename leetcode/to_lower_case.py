class Solution:
    def toLowerCase(self, str: str) -> str:
        new_list = list()
        for i in str:
            if i == "A":
                new_list.append("a")
            elif i == "B":
                new_list.append("b")
            elif i == "C":
                new_list.append("c")
            elif i == "D":
                new_list.append("d")
            elif i == "E":
                new_list.append("e")
            elif i == "F":
                new_list.append("f")
            elif i == "G":
                new_list.append("g")
            elif i == "H":
                new_list.append("h")
            elif i == "I":
                new_list.append("i")
            elif i == "J":
                new_list.append("j")
            elif i == "K":
                new_list.append("k")
            elif i == "L":
                new_list.append("l")
            elif i == "M":
                new_list.append("m")
            elif i == "N":
                new_list.append("n")
            elif i == "O":
                new_list.append("o")
            elif i == "P":
                new_list.append("p")
            elif i == "Q":
                new_list.append("q")
            elif i == "R":
                new_list.append("r")
            elif i == "S":
                new_list.append("s")
            elif i == "T":
                new_list.append("t")
            elif i == "U":
                new_list.append("u")
            elif i == "V":
                new_list.append("v")
            elif i == "W":
                new_list.append("w")
            elif i == "X":
                new_list.append("x")
            elif i == "Y":
                new_list.append("y")
            elif i == "Z":
                new_list.append("z")
            else:
                new_list.append(i)
        # return new list as a string.
        return "".join(new_list)
            